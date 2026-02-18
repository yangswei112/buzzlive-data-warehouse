from buzzwh_transform import *
import pandas as pd
import os

# SET UP THE FILE PATH

shopee_report_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/datasets/shopee seller center/feb-week2/'
tiktok_report_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/datasets/tiktok seller center/feb-week2/'
# tiktok_report_path_2 = 'C:/Users/ASUS/Downloads/reporting/tiktok seller center 2/jan-week3/'
result_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/datasets/result/'

# TRANSFORM SHOPEE LIVESTREAMING
shopee_transform_action(shopee_report_path, result_path)

# TRANSFORM TIKTOK LIVESTREAMING
tiktok_transform_action(tiktok_report_path, result_path)



