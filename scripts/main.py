from buzzwh_transform import *
import pandas as pd
import os

# SET UP THE FILE PATH

shopee_report_path = 'C:/Users/ASUS/Downloads/reporting/shopee seller center/adds/'
tiktok_report_path = 'C:/Users/ASUS/Downloads/reporting/tiktok seller center/jan-week3/'
tiktok_report_path_2 = 'C:/Users/ASUS/Downloads/reporting/tiktok seller center 2/jan-week3/'
result_path = 'C:/Users/ASUS/Downloads/reporting/result/'

shopee_file_names = os.listdir(shopee_report_path)
tiktok_file_names = os.listdir(tiktok_report_path)
tiktok_file_names_2 = os.listdir(tiktok_report_path_2)

# TRANSFORM SHOPEE LIVESTREAMING

transformed_shopee_lst = []

print('SHOPEE TRANSFORMING PROCESS STARTS')

for file in shopee_file_names:
    loaded_file = pd.read_csv(shopee_report_path+file)
    print(file + " " + "is loaded")
    transformed_file = shopee_transform(loaded_file)
    print(file + " " + "is transformed")
    transformed_shopee_lst.append(transformed_file)
    print("############################################################")
    
print('all the shopee files have been transformed')
print('SHOPEE TRANSFORMING PROCESS DONE')

ready_to_db_shopee_silver = pd.concat(transformed_shopee_lst)
ready_to_db_shopee_silver.to_csv(result_path+'ready_to_db_shopee_silver.csv', index=False)
# ready_to_db_shopee_silver[ready_to_db_shopee_silver['live_start_date'] >= datetime(2026, 1, 1).date()].to_csv(result_path+'ready_to_db_shopee_silver.csv', index=False)

shopee_bronze_db = ['DataPeriod', 'UserId', 'No', 'LivestreamName', 'StartTime', 'Duration',
                   'EngagedViewers', 'Comments', 'ATC', 'AvgViewingDuration', 'Viewers',
                   'Orders_PlacedOrder', 'Orders_ConfirmedOrder', 'ItemsSold_PlacedOrder',
                   'ItemsSold_ConfirmedOrder', 'Sales_PlacedOrder', 'Sales_ConfirmedOrder',
                   'live_host_id', 'live_start', 'live_start_date','live_viewers']

ready_to_db_shopee_silver[shopee_bronze_db].to_csv(result_path+'ready_to_db_shopee_bronze.csv', index=False)
# ready_to_db_shopee_silver[shopee_bronze_db][ready_to_db_shopee_silver['live_start_date'] >= datetime(2026, 1, 1).date()].to_csv(result_path+'ready_to_db_shopee_bronze.csv', index=False)

print('all the shopee files are ready to be loaded to database')


# TRANSFORM TIKTOK LIVESTREAMING

transformed_tiktok_lst = []

print('TIKTOK 1 TRANSFORMING PROCESS STARTS')
# TRANSFORM TIKTOK 1
for file in tiktok_file_names:
    loaded_file = pd.read_excel(tiktok_report_path+file, skiprows=2)
    print(file + " " + "is loaded")
    transformed_file = tiktok_transform_vers1(loaded_file)
    print(file + " " + "is transformed")
    transformed_tiktok_lst.append(transformed_file)
    print("############################################################")
print('TIKTOK 1 TRANSFORMING PROCESS DONE')    

print('TIKTOK 2 TRANSFORMING PROCESS STARTS')
# TRANSFORM TIKTOK 2    
## khusus bloomlab tiktok ####
for file in tiktok_file_names_2:
    brand_info = pd.read_csv('C:/Users/ASUS/Downloads/reporting/brand data/brand_table.csv')
    bloomlab_tiktok = pd.read_excel(tiktok_report_path_2+file, skiprows=2)
    # get the id
    bloomlab_id = brand_info[brand_info['brand_name'] == 'Bloomlab']['brand_id'].values[0]
    # add id column to df
    bloomlab_tiktok['Creator Id'] = bloomlab_id
    # transform file
    transformed_file = tiktok_transform_vers2(bloomlab_tiktok)
    transformed_file = transformed_file.drop(['GrossRevenue', 'DirectGMV', 'AvgPrice'], axis=1)
    # append file
    transformed_tiktok_lst.append(transformed_file)
print('TIKTOK 2 TRANSFORMING PROCESS DONE')

print('all the tiktok files have been transformed')

ready_to_db_tiktok = pd.concat(transformed_tiktok_lst)
ready_to_db_tiktok.to_csv(result_path+'ready_to_db_tiktok.csv', index=False)
# ready_to_db_tiktok[ready_to_db_tiktok['live_start_date'] >= datetime(2026, 1, 1).date()].to_csv(result_path+'ready_to_db_tiktok.csv', index=False)

print('all the tiktok files are ready to be loaded to database')

