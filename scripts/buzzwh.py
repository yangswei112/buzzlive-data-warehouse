from clients.sqlserver import SQLServerConnection
from sqlalchemy import text
from utils.buzzwh_transform import shopee_transform, tiktok_transform_vers1
import pandas as pd
import os

from config import settings
from clients.sqlserver import SQLServerConnection

# Instantiate database manager using imported config
ss = SQLServerConnection(
    server=settings.DB_SERVER,
    database=settings.DB_NAME,
    username=settings.DB_USERNAME,
    password=settings.DB_PASSWORD,
    driver=settings.DB_DRIVER,
)

def load_to_db(start_date, end_date):
    procedures_no_params = [
        "EXEC bronze.load_info;",
        "EXEC bronze.load_tiktok;",
        "EXEC bronze.load_shopee;",
        "EXEC silver.load_info;",
        "EXEC silver.load_tiktok;",
        "EXEC silver.load_shopee;"
    ]
    
    # Define parameterized stored procedure queries
    silver_tiktok_query = text("EXEC silver.filter_brand_tiktok @start_date = :start, @end_date = :end;")
    silver_shopee_query = text("EXEC silver.filter_brand_shopee @start_date = :start, @end_date = :end;")
    
    # Dictionary of parameters passed to session execution
    date_params = {"start": start_date, "end": end_date}
    
    with ss.get_session() as session:
        # 1. Execute stored procedures without parameters
        for proc in procedures_no_params:
            session.execute(text(proc))
            
        # 2. Execute stored procedures with parameters
        session.execute(silver_tiktok_query, date_params)
        session.execute(silver_shopee_query, date_params)
        
        # Context manager automatically commits upon exiting without errors

def get_raw_data_from_db(start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetches Shopee and TikTok raw data from DB and returns a single concatenated DataFrame.
    """
    query_raw_shopee = text("""
        SELECT * FROM gold.ShopeeRawDataForHR
        WHERE live_start_date BETWEEN :start AND :end;
    """)
    
    query_raw_tiktok = text("""
        SELECT * FROM gold.TiktokRawDataForHR
        WHERE live_start_date BETWEEN :start AND :end;
    """)
    
    params = {"start": start_date, "end": end_date}
    
    # 1. Added parentheses to get_connection()
    with ss.get_connection() as conn:
        # 2. Passed params dictionary to read_sql_query
        df_raw_shopee = pd.read_sql_query(query_raw_shopee, conn, params=params)
        df_raw_tiktok = pd.read_sql_query(query_raw_tiktok, conn, params=params)
        df_raw_tiktok.rename(columns={'LivestreamCreator':'LivestreamName'}, inplace=True)
        df_raw = pd.concat([df_raw_shopee,df_raw_tiktok])
        
    print('raw data has been retrieved from database')

    return df_raw

def get_gold_silver_data(start_date: str, end_date: str) -> pd.DataFrame:
    """
    to get gold silver data from database
    """
    query_gold_silver_shopee = text("""
        SELECT * FROM gold.WeeklyShopeeLive
        WHERE Date BETWEEN :start AND :end
        AND Studio = 'Klaten'
        ORDER BY Brand, Date, StartLive ASC;
        """)
    query_gold_silver_tiktok = text("""
        SELECT * FROM gold.WeeklyTiktokLive
        WHERE Date BETWEEN :start AND :end
        AND Studio = 'Klaten'
        ORDER BY Brand, Date, StartLive ASC;
        """)
    params = {"start": start_date, "end": end_date}
    with ss.get_connection() as conn:
        df_gold_silver_shopee = pd.read_sql_query(query_gold_silver_shopee, conn, params=params)
        df_gold_silver_tiktok = pd.read_sql_query(query_gold_silver_tiktok, conn, params=params)
        df_gold_silver = pd.concat([df_gold_silver_shopee, df_gold_silver_tiktok])

    print('gold silver data has been retrieved from database')

    return df_gold_silver

def get_silver_data_shopee(start_date: str, end_date: str, brand_name: str) -> pd.DataFrame:
    """
    to get silver data from database
    """
    query_silver_shopee = text("""
        SELECT * FROM silver.shopee_livestreaming
        WHERE live_start_date BETWEEN :start AND :end
        AND UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name= :brand AND platform='Shopee')
        AND Studio = 'Klaten'
        ORDER BY StartTime;
        """)
    params = {"start": start_date, "end": end_date, "brand": brand_name}
    with ss.get_connection() as conn:
        df_silver_shopee = pd.read_sql_query(query_silver_shopee, conn, params=params)

    print(f'silver shopee data for {brand_name} has been retrieved from database')

    return df_silver_shopee
    
def get_silver_data_tiktok(start_date: str, end_date: str, brand_name: str) -> pd.DataFrame:
    """
    to get silver data from database
    """
    query_silver_tiktok = text("""
        SELECT * FROM silver.tiktok_livestreaming
        WHERE live_start_date BETWEEN :start AND :end
        AND CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name=:brand AND platform='Tiktok')
        AND Studio = 'Klaten'
        ORDER BY StartTime;
        """)
    params = {"start": start_date, "end": end_date, "brand": brand_name}
    with ss.get_connection() as conn:
        df_silver_tiktok = pd.read_sql_query(query_silver_tiktok, conn, params=params)

    print(f'silver tiktok data for {brand_name} has been retrieved from database')

    return df_silver_tiktok

def get_shopee_seller_data(start_date: str, end_date: str) -> pd.DataFrame:
    """
    to get shopee seller data from database
    """
    query_shopee_seller = text("""
        SELECT * FROM silver.shopee_livestreaming
        LEFT JOIN silver.brand_info ON silver.shopee_livestreaming.UserId = silver.brand_info.brand_id
        WHERE live_start_date BETWEEN :start AND :end
        AND Studio = 'Klaten'
        AND brand_category = 'Shopee SMS'
        ORDER BY brand_name, live_start_date, live_start_time;
        """)
    params = {"start": start_date, "end": end_date}
    with ss.get_connection() as conn:
        df_shopee_seller = pd.read_sql_query(query_shopee_seller, conn, params=params)

    print(f'shopee seller data has been retrieved from database')

    return df_shopee_seller

def update_shopee_sales(shopee_path: str):
    """
    updating shopee live sales monthly on database
    """
    shopee_file_names = os.listdir(shopee_path)

    transformed_shopee_lst = []
    print('SHOPEE TRANSFORMING PROCESS STARTS')

    for file in shopee_file_names:
        loaded_file = pd.read_csv(shopee_path+file)
        print(file + " " + "is loaded")
        transformed_file = shopee_transform(loaded_file)
        print(file + " " + "is transformed")
        transformed_shopee_lst.append(transformed_file)
        print("############################################################")
    
    print('all the shopee files have been transformed')
    print('SHOPEE TRANSFORMING PROCESS DONE')

    ready_to_db_shopee_silver_update = pd.concat(transformed_shopee_lst)

    # Update Shopee Sales
    ready_to_update_shopee_silver = ready_to_db_shopee_silver_update[['UserId','live_start','live_placed_orders', 'live_confirmed_orders',
                                                                'live_placed_items_sold', 'live_confirmed_items_sold','live_placed_sales',
                                                                'live_confirmed_sales']]
    # ready_to_update_shopee_silver.head()
    # update
    with ss.get_session() as session:
        for index, row in ready_to_update_shopee_silver.iterrows():
            query_update_sales_shopee = text("""
                            UPDATE silver.shopee_livestreaming
                            SET live_confirmed_sales = :row1,
                                live_placed_sales = :row2,
                                live_confirmed_items_sold = :row3,
                                live_placed_items_sold = :row4,
                                live_confirmed_orders = :row5,
                                live_placed_orders = :row6
                            WHERE UserId = :row7
                            AND live_start = :row8
                        """)
            params = {'row1':row['live_confirmed_sales'],
                    'row2':row['live_placed_sales'],
                    'row3':row['live_confirmed_items_sold'],
                    'row4':row['live_placed_items_sold'],
                    'row5':row['live_confirmed_orders'],
                    'row6':row['live_placed_orders'],
                    'row7':row['UserId'],
                  'row8':row['live_start']}
       
            session.execute(query_update_sales_shopee, params=params)

    print("ALL THE SHOPEE SALES DATA HAVE BEEN UPDATED ON DATABASE")

def update_tiktok_sales(tiktok_path: str):
    """
    updating tiktok live sales monthly on database
    """
    tiktok_file_names = os.listdir(tiktok_path)

    transformed_tiktok_lst = []

    print('TIKTOK 1 TRANSFORMING PROCESS STARTS')
    # TRANSFORM TIKTOK 1
    for file in tiktok_file_names:
        loaded_file = pd.read_excel(tiktok_path+file, skiprows=2)
        print(file + " " + "is loaded")
        transformed_file = tiktok_transform_vers1(loaded_file)
        print(file + " " + "is transformed")
        transformed_tiktok_lst.append(transformed_file)
        print("############################################################")
    print('TIKTOK 1 TRANSFORMING PROCESS DONE')  
    
    print('all the tiktok files have been transformed')

    ready_to_db_tiktok_update = pd.concat(transformed_tiktok_lst)  
    
    # Update Tiktok Sales
    ready_to_update_tiktok = ready_to_db_tiktok_update[['CreatorId','StartTime','live_direct_gmv','OrdersPaidFor','ItemsSold','Customers']]
    # ready_to_update_tiktok.head()

    with ss.get_session() as session:
        for index, row in ready_to_update_tiktok.iterrows():
            query_update_sales_tiktok = text("""
                            UPDATE silver.tiktok_livestreaming
                            SET live_direct_gmv = :row1,
                                OrdersPaidFor = :row2,
                                ItemsSold = :row3,
                                Customers = :row4
                            WHERE CreatorId = :row5
                            AND StartTime = :row6
                        """)
            params = {'row1':row['live_direct_gmv'],
                      'row2':row['OrdersPaidFor'],
                      'row3':row['ItemsSold'],
                      'row4':row['Customers'],
                      'row5':row['CreatorId'],
                      'row6':row['StartTime']}
            session.execute(query_update_sales_tiktok, params=params)

    print("ALL THE TIKTOK SALES DATA HAVE BEEN UPDATED ON DATABASE")

def backup_database(monthyear: str):
    """
    Backs up the database to a specified file path.
    """
    # Build the file path in Python
    backup_file = f"C:/SQLBackups/BuzzliveWarehouse-{monthyear}.bak"
    
    # Raw SQL query with formatted path
    query_backup = text(f"""
        BACKUP DATABASE BuzzliveWarehouse
        TO DISK = :backup_file
        WITH FORMAT,
             MEDIANAME = 'SQLServerBackups',
             NAME = 'Full Backup of BuzzliveWarehouse';
    """)
    
    # Must use autocommit mode for SQL Server BACKUP statements
    with ss.get_connection().execution_options(isolation_level="AUTOCOMMIT") as conn:
        conn.execute(query_backup, {"backup_file": backup_file})

    print(f'Database has been backed up to {backup_file}')