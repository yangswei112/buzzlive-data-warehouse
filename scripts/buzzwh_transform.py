# standardize every columns
from buzzwh_helper_func import *
import pandas as pd
import emoji


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
        print('STEP 6 PROCESS DONE, CONTINUE TO THE LAST STEP')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 6 PROCESS. THE ERROR IS: ', e)

    # STEP 7 - Sales(Placed Order), Sales(Confirmed Order)
    try:
        print('STEP 7 PROCESS STARTS')
        trial["live_placed_sales"] = trial['Sales_PlacedOrder'].apply(lambda x: convert_sales(x))
        trial["live_confirmed_sales"] = trial['Sales_ConfirmedOrder'].apply(lambda x: convert_sales(x))
        print('STEP 7 PROCESS DONE')
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
        print('STEP 3 PROCESS DONE, CONTINUE TO LAST STEP')
    except Exception as e:
        print('ERROR OCCURED DURING STEP 3 PROCESS. THE ERROR IS: ', e)

    # STEP 4 - CTOR & CTR
    try:
        print('STEP 4 PROCESS STARTS')
        trial['live_ctor'] = trial['CTOR'].apply(lambda x: float(x.strip("%")))
        trial['live_ctr'] = trial['CTR'].apply(lambda x: float(x.strip("%")))
        print('STEP 4 PROCESS DONE')
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
        print('STEP 5 PROCESS DONE')
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
