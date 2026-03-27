from buzzwh_transform import *
import pandas as pd
import os
import pyodbc

# SET UP THE DATABASE CONNECTION
connection_string = ("DRIVER={SQL Server};PORT=1433;SERVER=LAPTOP-Q4096V85\SQLEXPRESS;DATABASE=BuzzliveWarehouse;Trusted_Connection=yes;")

# SET UP THE FILE PATH
shopee_report_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/datasets/shopee seller center/adds/'
tiktok_report_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/datasets/tiktok seller center/adds/'
result_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/datasets/result/'

# SET UP DATE RANGE
start_date = '2024-02-23'
end_date = '2024-02-28'

# # TRANSFORM DATA
shopee_transform_action(shopee_report_path, result_path)
tiktok_transform_action(tiktok_report_path, result_path)

# # LOAD DATA TO DATABASE
# load_to_db(connection_string, start_date, end_date)

# # LOAD RAW DATA TO BIGQUERY FROM DATABASE
# df_raw = get_raw_data_from_db(connection_string, start_date, end_date)
# load_to_bigquery(df_raw, 'buzzwh.raw_data_livestreaming')

# UPDATE MONTHLY SALES
# # UPDATE SHOPEE MONTHLY SALES
# update_shopee_sales(shopee_report_path, connection_string)

# # UPDATE TIKTOK MONTHLY SALES
# update_tiktok_sales(tiktok_report_path, connection_string)

