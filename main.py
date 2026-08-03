# from scripts.weekly_pipeline import *
# from scripts.monthly_pipeline import *

from utils.buzzwh_transform import *

# WEEKLY REPORT PIPELINE
# SET UP DATE RANGE
# start_date_weekly = '2026-07-13'
# end_date_weekly = '2026-07-26'

# extract()
# transform()
# load_to_db(start_date=start_date_weekly, end_date=end_date_weekly)
# load_to_bigquery(start_date_weekly=start_date_weekly, end_date_weekly=end_date_weekly)
# load_silver_to_sheets(start_date_weekly=start_date_weekly, end_date_weekly=end_date_weekly)
# load_to_gsheet(start_date_weekly=start_date_weekly, end_date_weekly=end_date_weekly)
# load_silver_to_sheets(start_date_weekly=start_date_weekly, end_date_weekly=end_date_weekly)

# MONTHLY REPORT PIPELINE
# SET UP DATE RANGE
# start_date_monthly = '2024-03-01'
# end_date_monthly = '2024-03-31'
# update_monthly()
# load_shopee_seller_to_sheet(start_date_monthly=start_date_monthly, end_date_monthly=end_date_monthly)
# backup_database()







# SET UP THE DATABASE CONNECTION
connection_string = ("DRIVER={SQL Server};PORT=1433;SERVER=LAPTOP-Q4096V85\SQLEXPRESS;DATABASE=BuzzliveWarehouse;Trusted_Connection=yes;")

# # SET UP THE FILE PATH
shopee_report_path = 'C:/datasets/shopee seller center/update/'
tiktok_report_path = 'C:/datasets/tiktok seller center/update/'
# result_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/datasets/result/'



# # TRANSFORM DATA
# shopee_transform_action(shopee_report_path, result_path)
# tiktok_transform_action(tiktok_report_path, result_path)

# # LOAD DATA TO DATABASE
# load_to_db(connection_string, start_date, end_date)

# # LOAD RAW DATA TO BIGQUERY FROM DATABASE
# df_raw = get_raw_data_from_db(connection_string, start_date, end_date)
# load_to_bigquery(df_raw, 'buzzwh.raw_data_livestreaming')

# UPDATE MONTHLY SALES
# UPDATE SHOPEE MONTHLY SALES
update_shopee_sales(shopee_report_path, connection_string)

# UPDATE TIKTOK MONTHLY SALES
update_tiktok_sales(tiktok_report_path, connection_string)