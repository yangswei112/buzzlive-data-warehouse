# standardize every columns
from buzzwh_helper_func import *
import pandas as pd
import emoji
import os
import pyodbc
from google.cloud import bigquery


def shopee_transform(trial):
    """
    converting and standardizing every column in shopee livestream
    """
    # STEP 1 - matching all the column names
    try:
        print('STEP 1 PROCESS STARTS')
        eng = 'Livestream Name'
        ind = 'Nama Livestream'
        if ind in trial.columns:
            shopee_rename_columns = {'Periode Data': 'DataPeriod',
                                     'User Id': 'UserId',
                                     'No.': 'No',
                                     'Nama Livestream': 'LivestreamName',
                                     'Start Time': 'StartTime',
                                     'Durasi': 'Duration',
                                     'Penonton Aktif': 'EngagedViewers',
                                     'Komentar': 'Comments',
                                     'Tambah ke Keranjang': 'ATC',
                                     'Durasi Rata-Rata Menonton': 'AvgViewingDuration',
                                     'Penonton': 'Viewers',
                                     'Pesanan(Pesanan Dibuat)': 'Orders_PlacedOrder',
                                     'Pesanan(Pesanan Siap Dikirim)': 'Orders_ConfirmedOrder',
                                     'Produk Terjual(Pesanan Dibuat)': 'ItemsSold_PlacedOrder',
                                     'Produk Terjual(Pesanan Siap Dikirim)': 'ItemsSold_ConfirmedOrder',
                                     'Penjualan(Pesanan Dibuat)': 'Sales_PlacedOrder',
                                     'Penjualan(Pesanan Siap Dikirim)': 'Sales_ConfirmedOrder'}
            trial = trial.rename(columns=shopee_rename_columns)
        else:
            shopee_rename_columns = {'Data Period': 'DataPeriod',
                                     'User Id': 'UserId',
                                     'No.': 'No',
                                     'Livestream Name': 'LivestreamName',
                                     'Start Time': 'StartTime',
                                     'Duration': 'Duration',
                                     'Engaged Viewers': 'EngagedViewers',
                                     'Comments': 'Comments',
                                     'ATC': 'ATC',
                                     'Avg. Viewing Duration': 'AvgViewingDuration',
                                     'Viewers': 'Viewers',
                                     'Orders(Placed Order)': 'Orders_PlacedOrder',
                                     'Orders(Confirmed Order)': 'Orders_ConfirmedOrder',
                                     'Items Sold(Placed Order)': 'ItemsSold_PlacedOrder',
                                     'Items Sold(Confirmed Order)': 'ItemsSold_ConfirmedOrder',
                                     'Sales(Placed Order)': 'Sales_PlacedOrder',
                                     'Sales(Confirmed Order)': 'Sales_ConfirmedOrder'}
            trial = trial.rename(columns=shopee_rename_columns)
        print('STEP 1 PROCESS DONE, CONTINUE TO STEP 2')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 1 PROCESS. THE ERROR IS: ', e)

    # STEP 2 - Livestream Name column: create host_id column by extracting the code in the column (#XXXX)
    try:
        print('STEP 2 PROCESS STARTS')
        trial['LivestreamName'] = trial['LivestreamName'].apply(lambda x: x.replace(",", ""))
        trial['live_host_id'] = trial['LivestreamName'].apply(
            lambda x: x.split("#")[-1].strip(" ").upper() if '#' in x else
            emoji.replace_emoji(x, replace=' ').split(' ')[-1].strip())
        trial['live_host_id'] = trial['live_host_id'].apply(lambda x: x.replace("", "NULL") if x == '' else x)
        print('STEP 2 PROCESS DONE, CONTINUE TO STEP 3')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 2 PROCESS. THE ERROR IS: ', e)

    # STEP 3 - Start Time column: create a new formatted and separated start date and start time
    try:
        print('STEP 3 PROCESS STARTS')
        trial['live_start'] = pd.to_datetime(trial['StartTime'])
        trial['live_start_date'] = pd.to_datetime(trial['StartTime'], format="%d-%m-%Y %H:%M").apply(lambda x: x.date())
        trial['live_start_time'] = pd.to_datetime(trial['StartTime']).apply(lambda x: round_to_nearest_hour(x).time())
        print('STEP 3 PROCESS DONE, CONTINUE TO STEP 4')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 3 PROCESS. THE ERROR IS: ', e)

    # STEP 4 - Duration column: create a new formatted duration column
    try:
        print('STEP 4 PROCESS STARTS')
        trial['live_duration'] = trial['Duration'].apply(
            lambda x: convert_into_minutes_duration(pd.to_datetime(x, format="%H:%M:%S").time()))
        print('STEP 4 PROCESS DONE, CONTINUE TO STEP 5')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 4 PROCESS. THE ERROR IS: ', e)

    # STEP 5 - Engaged Viewers, Comments, ATC, Viewers, Orders(Placed Order), Orders(Confirmed Order), Items Sold(Placed Order), Items Sold(Confirmed Order)
    try:
        print('STEP 5 PROCESS STARTS')
        trial['live_engaged_viewers'] = trial['EngagedViewers'].apply(lambda x: convert_floated_numbers(x))
        trial['live_comments'] = trial['Comments'].apply(lambda x: convert_floated_numbers(x))
        trial['live_atc'] = trial['ATC'].apply(lambda x: convert_floated_numbers(x))
        trial['live_viewers'] = trial['Viewers'].apply(lambda x: convert_floated_numbers(x))
        trial['live_placed_orders'] = trial['Orders_PlacedOrder'].apply(lambda x: convert_floated_numbers(x))
        trial['live_confirmed_orders'] = trial['Orders_ConfirmedOrder'].apply(lambda x: convert_floated_numbers(x))
        trial['live_placed_items_sold'] = trial['ItemsSold_PlacedOrder'].apply(lambda x: convert_floated_numbers(x))
        trial['live_confirmed_items_sold'] = trial['ItemsSold_ConfirmedOrder'].apply(
            lambda x: convert_floated_numbers(x))
        print('STEP 5 PROCESS DONE, CONTINUE TO STEP 6')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 5 PROCESS. THE ERROR IS: ', e)

    # STEP 6 - Avg. Viewing Duration: create a new formatted duration column
    try:
        print('STEP 6 PROCESS STARTS')
        trial['live_avg_viewing_duration'] = trial['AvgViewingDuration'].apply(
            lambda x: convert_into_seconds_duration(pd.to_datetime(x, format="%H:%M:%S").time()))
        print('STEP 6 PROCESS DONE, CONTINUE TO STEP 7')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 6 PROCESS. THE ERROR IS: ', e)

    # STEP 7 - Sales(Placed Order), Sales(Confirmed Order)
    try:
        print('STEP 7 PROCESS STARTS')
        trial["live_placed_sales"] = trial['Sales_PlacedOrder'].apply(lambda x: convert_sales(x))
        trial["live_confirmed_sales"] = trial['Sales_ConfirmedOrder'].apply(lambda x: convert_sales(x))
        print('STEP 7 PROCESS DONE, CONTINUE TO THE LAST STEP')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 7 PROCESS. THE ERROR IS: ', e)

    # STEP 8 - Add new column 'Studio'
    try:
        print('STEP 8 PROCESS STARTS')
        trial["Studio"] = '-'
        print('STEP 8 PROCESS DONE, ALL STEPS DONE')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 8 PROCESS. THE ERROR IS: ', e)

    return trial


def tiktok_transform_vers1(trial):
    """
    converting and standardizing every column in tiktok livestream version I
    """
    # tiktok I
    # STEP 1 - matching all the column names
    try:
        print('STEP 1 PROCESS STARTS')
        drop_col_tiktok1 = ['Nama panggilan', 'Produk yang ditambahkan',
                            'Produk Terjual', 'Pesanan SKU yang dibuat']
        tiktok1_rename_columns = {'ID Kreator': 'CreatorId',
                                  'Rasio pesanan per klik (LIVE)': 'CTOR',
                                  'Klik Produk': 'ProductClicks',
                                  'Produk Dilihat': 'ProductImpressions',
                                  'Live Dibagikan': 'Shares',
                                  'Komentar': 'Comments',
                                  'Suka pada LIVE': 'Likes',
                                  'Durasi menonton rata-rata (Siaran LIVE)': 'AvgViewDuration',
                                  'Pengikut baru (Video kreator)': 'NewFollowers',
                                  'Penonton': 'Viewers',
                                  'Live Stream Dilihat': 'Views',
                                  'Pesanan SKU dari LIVE': 'OrdersPaidFor',
                                  'Harga Rata-Rata (Rp)': 'live_avg_price',
                                  'Pembeli unik': 'Customers',
                                  'Produk yang terjual dari LIVE': 'ItemsSold',
                                  'Nilai bruto barang dagangan dari LIVE (Rp)': 'live_direct_gmv',
                                  'GMV yang didapat dari LIVE (Rp)': 'live_gross_revenue',
                                  'Durasi': 'Duration',
                                  'Waktu Live': 'StartTime',
                                  'Kreator': 'LivestreamCreator'}
        trial = trial.drop(drop_col_tiktok1, axis=1)
        trial = trial.rename(columns=tiktok1_rename_columns)
        print('STEP 1 PROCESS DONE, CONTINUE TO NEXT STEP')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 1 PROCESS. THE ERROR IS: ', e)

    # STEP 2 - Start time column
    try:
        print('STEP 2 PROCESS STARTS')
        trial['live_start_date'] = pd.to_datetime(trial['StartTime']).apply(lambda x: x.date())
        trial['live_start_time'] = pd.to_datetime(trial['StartTime']).apply(lambda x: round_to_nearest_hour(x).time())
        print('STEP 2 PROCESS DONE, CONTINUE TO NEXT STEP')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 2 PROCESS. THE ERROR IS: ', e)

    # STEP 3 - duration
    try:
        print('STEP 3 PROCESS STARTS')
        trial['live_duration'] = trial['Duration'].apply(lambda x: convert_duration_tiktok(x))
        print('STEP 3 PROCESS DONE, CONTINUE TO NEXT STEP')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 3 PROCESS. THE ERROR IS: ', e)

    # STEP 4 - CTOR & CTR
    try:
        print('STEP 4 PROCESS STARTS')
        trial['live_ctor'] = trial['CTOR'].apply(lambda x: float(x.strip("%")))
        trial['live_ctr'] = trial['CTR'].apply(lambda x: float(x.strip("%")))
        print('STEP 4 PROCESS DONE, CONTINUE TO NEXT STEP')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 4 PROCESS. THE ERROR IS: ', e)

    # STEP 5 - Add new column 'Studio'
    try:
        print('STEP 5 PROCESS STARTS')
        trial["Studio"] = '-'
        print('STEP 5 PROCESS DONE, ALL STEPS DONE')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 5 PROCESS. THE ERROR IS: ', e)

    return trial


def tiktok_transform_vers2(trial):
    """
    converting and standardizing every column in tiktok livestream version II
    """
    # tiktok II
    # STEP 1 - matching all the column names
    try:
        print('STEP 1 PROCESS STARTS')
        drop_col_tiktok2 = ['GMV/1K shows', 'GMV/1K views', 'Peak viewers']
        tiktok2_rename_columns = {'Creator Id': 'CreatorId',
                                  'Product clicks': 'ProductClicks',
                                  'Product impressions': 'ProductImpressions',
                                  'Avg. view duration': 'AvgViewDuration',
                                  'New followers': 'NewFollowers',
                                  'Orders paid for': 'OrdersPaidFor',
                                  'Avg. price': 'AvgPrice',
                                  'Items sold': 'ItemsSold',
                                  'Direct GMV': 'DirectGMV',
                                  'Gross revenue': 'GrossRevenue',
                                  'Start time': 'StartTime',
                                  'Livestream': 'LivestreamCreator',
                                  'CTOR (SKU orders)': 'CTOR'}
        trial = trial.drop(drop_col_tiktok2, axis=1)
        trial = trial.rename(columns=tiktok2_rename_columns)
        print('STEP 1 PROCESS DONE, CONTINUE TO NEXT STEP')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 1 PROCESS. THE ERROR IS: ', e)

    # Livestream Creator: create host_id column by extracting the code
    #     trial['host_id'] = trial['LivestreamCreator'].apply(lambda x: x.split("#")[-1].upper())

    # STEP 2 - Start time column
    try:
        print('STEP 2 PROCESS STARTS')
        # same as tiktok I
        trial['live_start_date'] = pd.to_datetime(trial['StartTime']).apply(lambda x: x.date())
        trial['live_start_time'] = pd.to_datetime(trial['StartTime']).apply(lambda x: round_to_nearest_hour(x).time())
        print('STEP 2 PROCESS DONE, CONTINUE TO NEXT STEP')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 2 PROCESS. THE ERROR IS: ', e)

    # STEP 3 - Duration column
    try:
        print('STEP 3 PROCESS STARTS')
        trial['live_duration'] = trial['Duration'].apply(lambda x: round(x / 60))
        print('STEP 3 PROCESS DONE, CONTINUE TO NEXT STEP')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 3 PROCESS. THE ERROR IS: ', e)

    # STEP 4 - Direct GMV, Gross GMV, Avg. Price column
    try:
        print('STEP 4 PROCESS STARTS')
        trial['live_direct_gmv'] = trial['DirectGMV'].apply(lambda x: convert_sales(x))
        trial['live_gross_revenue'] = trial['GrossRevenue'].apply(lambda x: convert_sales(x))
        trial['live_avg_price'] = trial['AvgPrice'].apply(lambda x: convert_sales(x))
        print('STEP 4 PROCESS DONE, CONTINUE TO NEXT STEP')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 4 PROCESS. THE ERROR IS: ', e)

    # STEP 5 - CTR & CTOR column
    try:
        print('STEP 5 PROCESS STARTS')
        trial['live_ctr'] = trial['CTR'].apply(lambda x: round(x * 100, 2))
        trial['live_ctor'] = trial['CTOR'].apply(lambda x: round(x * 100, 2))
        print('STEP 5 PROCESS DONE, CONTINUE TO NEXT STEP')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 5 PROCESS. THE ERROR IS: ', e)

    # STEP 6 - Add new column 'Studio'
    try:
        print('STEP 6 PROCESS STARTS')
        trial["Studio"] = '-'
        print('STEP 6 PROCESS DONE, ALL STEPS DONE')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 6 PROCESS. THE ERROR IS: ', e)

    return trial


def shopee_transform_action(shopee_path: str, result_path: str):
    """
    to transform and save shopee live data to csv
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

    ready_to_db_shopee_silver = pd.concat(transformed_shopee_lst)
    ready_to_db_shopee_silver.to_csv(result_path+'ready_to_db_shopee_silver.csv', index=False)

    shopee_bronze_db = ['DataPeriod', 'UserId', 'No', 'LivestreamName', 'StartTime', 'Duration',
                        'EngagedViewers', 'Comments', 'ATC', 'AvgViewingDuration', 'Viewers',
                        'Orders_PlacedOrder', 'Orders_ConfirmedOrder', 'ItemsSold_PlacedOrder',
                        'ItemsSold_ConfirmedOrder', 'Sales_PlacedOrder', 'Sales_ConfirmedOrder',
                        'live_host_id', 'live_start', 'live_start_date','live_viewers']

    ready_to_db_shopee_bronze = ready_to_db_shopee_silver[shopee_bronze_db]
    ready_to_db_shopee_silver[shopee_bronze_db].to_csv(result_path+'ready_to_db_shopee_bronze.csv', index=False)

    print('all the shopee files are ready to be loaded to database')
    print('the shape of new shopee bronze data: ', ready_to_db_shopee_bronze.shape)
    print('the shape of new shopee silver data: ', ready_to_db_shopee_silver.shape)


def tiktok_transform_action(tiktok_path: str, result_path: str):
    """
    to transform and save tiktok live to csv
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

    ready_to_db_tiktok = pd.concat(transformed_tiktok_lst)
    ready_to_db_tiktok.to_csv(result_path+'ready_to_db_tiktok.csv', index=False)

    print('all the tiktok files are ready to be loaded to database')
    print('the shape of new tiktok data: ', ready_to_db_tiktok.shape)


def update_shopee_sales(shopee_path: str, connection_db: str):
    """
    updating shopee live sales monthly on database
    """
    shopee_file_names = os.listdir(shopee_path)
    # declare PYODBC connection with the string
    conn = pyodbc.connect(connection_db)
    # declaring cursor
    cursor = conn.cursor()

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
        cursor.execute(query_update_sales_shopee)
        conn.commit()
        
    cursor.close()

    print("ALL THE SHOPEE SALES DATA HAVE BEEN UPDATED ON DATABASE")


def update_tiktok_sales(tiktok_path: str, connection_db: str):
    """
    updating tiktok live sales monthly on database
    """
    tiktok_file_names = os.listdir(tiktok_path)
    # declare PYODBC connection with the string
    conn = pyodbc.connect(connection_db)
    # declaring cursor
    cursor = conn.cursor()

    # TRANSFORM TIKTOK LIVESTREAMING
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
    ready_to_update_tiktok = ready_to_db_tiktok_update[['CreatorId','StartTime','live_direct_gmv']]
    # ready_to_update_tiktok.head()

    for index, row in ready_to_update_tiktok.iterrows():
        query_update_sales_tiktok = f"""
                        UPDATE silver.tiktok_livestreaming
                        SET live_direct_gmv = {row['live_direct_gmv']}
                        WHERE CreatorId = {row['CreatorId']}
                        AND StartTime = '{row['StartTime']}'
                    """
        # update
        cursor.execute(query_update_sales_tiktok)
        conn.commit()
        
    cursor.close()

    print("ALL THE TIKTOK SALES DATA HAVE BEEN UPDATED ON DATABASE")


def load_to_db(connection_string: str, start_date: str, end_date: str):
    """
    to load shopee & tiktok data to database
    """
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    query = f"""
            EXEC bronze.load_info;
            EXEC bronze.load_tiktok;
            EXEC bronze.load_shopee;
            EXEC silver.load_info;
            EXEC silver.load_tiktok;
            EXEC silver.load_shopee;
            EXEC silver.filter_brand_tiktok @start_date={start_date}, @end_date={end_date};
            EXEC silver.filter_brand_shopee @start_date={start_date}, @end_date={end_date};
        """
    cursor.execute(query)
    conn.commit()
    cursor.close()

    print('data has been loaded to database')


def get_raw_data_from_db(connection_string: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    to get raw data from database
    """
    conn = pyodbc.connect(connection_string)
    query_raw_shopee = f"""
            SELECT * FROM gold.ShopeeRawDataForHR
            WHERE live_start_date BETWEEN '{start_date}' AND '{end_date}';
    """

    query_raw_tiktok = f"""
            SELECT * FROM gold.TiktokRawDataForHR
            WHERE live_start_date BETWEEN '{start_date}' AND '{end_date}';
    """

    df_raw_shopee = pd.read_sql_query(query_raw_shopee, conn)
    df_raw_tiktok = pd.read_sql_query(query_raw_tiktok, conn)
    df_raw_tiktok.rename(columns={'LivestreamCreator':'LivestreamName'}, inplace=True)
    df_raw = pd.concat([df_raw_shopee,df_raw_tiktok])
    
    conn.close()

    print('raw data has been retrieved from database')

    return df_raw

def load_to_bigquery(df: pd.DataFrame, table_id: str):
    """
    to load dataframe to bigquery
    """
    client = bigquery.Client()
    job = client.load_table_from_dataframe(df, table_id)
    job.result()  # Wait for the job to complete.
    print(f"Loaded {job.output_rows} rows into {table_id}.")