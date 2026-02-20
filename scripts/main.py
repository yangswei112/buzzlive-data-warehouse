from buzzwh_transform import *
import pandas as pd
import os
import pyodbc

# SET UP THE DATABASE CONNECTION
connection_string = ("DRIVER={SQL Server};PORT=1433;SERVER=LAPTOP-Q4096V85\SQLEXPRESS;DATABASE=BuzzliveWarehouse;Trusted_Connection=yes;")

# SET UP THE FILE PATH
shopee_report_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/datasets/shopee seller center/feb-week2-2/'
tiktok_report_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/datasets/tiktok seller center/adds/'
result_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/datasets/result/'

# TRANSFORM SHOPEE LIVESTREAMING
shopee_transform_action(shopee_report_path, result_path)

# TRANSFORM TIKTOK LIVESTREAMING
tiktok_transform_action(tiktok_report_path, result_path)

# UPDATE SHOPEE MONTHLY SALES
update_shopee_sales(shopee_report_path, connection_string)

# UPDATE TIKTOK MONTHLY SALES
update_tiktok_sales(tiktok_report_path, connection_string)

