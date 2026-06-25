import pandas as pd
import pyodbc
from buzzwh_transform import shopee_transform, tiktok_transform_vers1
import os

class BuzzliveWarehouse:
    CONNECTION_STRING = "DRIVER={SQL Server};PORT=1433;SERVER=LAPTOP-Q4096V85\SQLEXPRESS;DATABASE=BuzzliveWarehouse;Trusted_Connection=yes;"
    def __init__(self, connection_string = None):
        if connection_string is None:
            connection_string = BuzzliveWarehouse.CONNECTION_STRING
        self.connection_string = connection_string
        self.conn = pyodbc.connect(self.connection_string)
        self.cursor = self.conn.cursor()
    
    def load_to_db(self, start_date: str, end_date: str):
        """
        To load shopee & tiktok data to database using a Medallion architecture.
        """
        # 1. Define independent, static stored procedures
        procedures_no_params = [
            "EXEC bronze.load_info;",
            "EXEC bronze.load_tiktok;",
            "EXEC bronze.load_shopee;",
            "EXEC silver.load_info;",
            "EXEC silver.load_tiktok;",
            "EXEC silver.load_shopee;"
        ]
        
        try:
            # 2. Execute procedures that don't need parameters
            for proc in procedures_no_params:
                self.cursor.execute(proc)
            
            # 3. Execute parameterized procedures safely (Assuming standard pyodbc/SQL Server style '?')
            # Note: If using pymssql, replace '?' with '%s'
            silver_tiktok_query = "EXEC silver.filter_brand_tiktok @start_date = ?, @end_date = ?;"
            self.cursor.execute(silver_tiktok_query, (start_date, end_date))
            
            silver_shopee_query = "EXEC silver.filter_brand_shopee @start_date = ?, @end_date = ?;"
            self.cursor.execute(silver_shopee_query, (start_date, end_date))
            
            # 4. Commit all operations only if EVERYTHING succeeded
            self.conn.commit()
            print('Data has been successfully loaded to database.')
            
        except Exception as e:
            # 5. Rollback changes if anything goes wrong to prevent partial data corruption
            self.conn.rollback()
            print(f"Database error encountered: {e}")
            raise e
    
    def get_raw_data_from_db(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        to get raw data from database
        """
        query_raw_shopee = f"""
                SELECT * FROM gold.ShopeeRawDataForHR
                WHERE live_start_date BETWEEN '{start_date}' AND '{end_date}';
        """

        query_raw_tiktok = f"""
                SELECT * FROM gold.TiktokRawDataForHR
                WHERE live_start_date BETWEEN '{start_date}' AND '{end_date}';
        """

        df_raw_shopee = pd.read_sql_query(query_raw_shopee, self.conn)
        df_raw_tiktok = pd.read_sql_query(query_raw_tiktok, self.conn)
        df_raw_tiktok.rename(columns={'LivestreamCreator':'LivestreamName'}, inplace=True)
        df_raw = pd.concat([df_raw_shopee,df_raw_tiktok])
        
        print('raw data has been retrieved from database')

        return df_raw
    
    def get_gold_silver_data(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        to get gold silver data from database
        """
        query_gold_silver_shopee = f"""
            SELECT * FROM gold.WeeklyShopeeLive
            WHERE Date BETWEEN '{start_date}' AND '{end_date}'
            AND Studio = 'Klaten'
            ORDER BY Brand, Date, StartLive ASC;
            """
        query_gold_silver_tiktok = f"""
            SELECT * FROM gold.WeeklyTiktokLive
            WHERE Date BETWEEN '{start_date}' AND '{end_date}'
            AND Studio = 'Klaten'
            ORDER BY Brand, Date, StartLive ASC;
            """
        df_gold_silver_shopee = pd.read_sql_query(query_gold_silver_shopee, self.conn)
        df_gold_silver_tiktok = pd.read_sql_query(query_gold_silver_tiktok, self.conn)
        df_gold_silver = pd.concat([df_gold_silver_shopee, df_gold_silver_tiktok])

        print('gold silver data has been retrieved from database')

        return df_gold_silver
    
    def get_silver_data_shopee(self, start_date: str, end_date: str, brand_name: str) -> pd.DataFrame:
        """
        to get silver data from database
        """
        query_silver_shopee = f"""
            SELECT * FROM silver.shopee_livestreaming
            WHERE live_start_date BETWEEN '{start_date}' AND '{end_date}'
            AND UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='{brand_name}' AND platform='Shopee')
            AND Studio = 'Klaten'
            ORDER BY StartTime;
            """
        df_silver_shopee = pd.read_sql_query(query_silver_shopee, self.conn)

        print(f'silver shopee data for {brand_name} has been retrieved from database')

        return df_silver_shopee
    
    def get_silver_data_tiktok(self, start_date: str, end_date: str, brand_name: str) -> pd.DataFrame:
        """
        to get silver data from database
        """
        query_silver_tiktok = f"""
            SELECT * FROM silver.tiktok_livestreaming
            WHERE live_start_date BETWEEN '{start_date}' AND '{end_date}'
            AND CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='{brand_name}' AND platform='Tiktok')
            AND Studio = 'Klaten'
            ORDER BY StartTime;
            """
        df_silver_tiktok = pd.read_sql_query(query_silver_tiktok, self.conn)

        print(f'silver tiktok data for {brand_name} has been retrieved from database')

        return df_silver_tiktok
    
    def get_shopee_seller_data(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        to get shopee seller data from database
        """
        query_shopee_seller = f"""
            SELECT * FROM silver.shopee_livestreaming
            LEFT JOIN silver.brand_info ON silver.shopee_livestreaming.UserId = silver.brand_info.brand_id
            WHERE live_start_date BETWEEN '{start_date}' AND '{end_date}'
            AND Studio = 'Klaten'
            AND brand_category = 'Shopee SMS'
            ORDER BY brand_name, live_start_date, live_start_time;
            """
        df_shopee_seller = pd.read_sql_query(query_shopee_seller, self.conn)

        print(f'shopee seller data has been retrieved from database')

        return df_shopee_seller
    
    def update_shopee_sales(self, shopee_path: str):
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

        for index, row in ready_to_update_shopee_silver.iterrows():
            query_update_sales_shopee = f"""
                            UPDATE silver.shopee_livestreaming
                            SET live_confirmed_sales = {row['live_confirmed_sales']},
                                live_placed_sales = {row['live_placed_sales']},
                                live_confirmed_items_sold = {row['live_confirmed_items_sold']},
                                live_placed_items_sold = {row['live_placed_items_sold']},
                                live_confirmed_orders = {row['live_confirmed_orders']},
                                live_placed_orders = {row['live_placed_orders']}
                            WHERE UserId = {row['UserId']}
                            AND live_start = '{row['live_start']}'
                        """
            # update
            self.cursor.execute(query_update_sales_shopee)
            self.conn.commit()

        print("ALL THE SHOPEE SALES DATA HAVE BEEN UPDATED ON DATABASE")

    def update_tiktok_sales(self, tiktok_path: str):
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

        for index, row in ready_to_update_tiktok.iterrows():
            query_update_sales_tiktok = f"""
                            UPDATE silver.tiktok_livestreaming
                            SET live_direct_gmv = {row['live_direct_gmv']},
                                OrdersPaidFor = {row['OrdersPaidFor']},
                                ItemsSold = {row['ItemsSold']},
                                Customers = {row['Customers']}
                            WHERE CreatorId = {row['CreatorId']}
                            AND StartTime = '{row['StartTime']}'
                        """
            # update
            self.cursor.execute(query_update_sales_tiktok)
            self.conn.commit()

        print("ALL THE TIKTOK SALES DATA HAVE BEEN UPDATED ON DATABASE")
    
    def backup_database(self, monthyear: str):
        """
        to backup the database
        """
        query_backup = f"""
                BACKUP DATABASE BuzzliveWarehouse
                TO DISK = 'C:\SQLBackups\BuzzliveWarehouse-{monthyear}.bak'
                WITH FORMAT,
                MEDIANAME = 'SQLServerBackups',
                NAME = 'Full Backup of BuzzliveWarehouse';
                """
        self.cursor.execute(query_backup)
        self.conn.commit()

        print('database has been backed up')
    
    def close_connection(self):
        """
        to close the connection to the database
        """
        self.cursor.close()
        self.conn.close()

        print('connection to database has been closed')