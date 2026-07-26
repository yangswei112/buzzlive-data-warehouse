from buzzwh import *
from clients.google_sheets import GoogleSheetsConn


def update_monthly():
    shopee_report_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/datasets/shopee seller center/update/'
    tiktok_report_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/datasets/tiktok seller center/update/'

    update_shopee_sales(shopee_report_path)
    update_tiktok_sales(tiktok_report_path)

def load_shopee_seller_to_sheet(start_date_monthly, end_date_monthly):
    gs = GoogleSheetsConn()
    shopee_seller_df = get_shopee_seller_data(start_date=start_date_monthly, end_date=end_date_monthly)
    gs.load_dataframe_to_sheet(shopee_seller_df, 'monthlyreport_shopee', 'from_db_shopee')

def backup_db(month: str):
    backup_database(monthyear=month)
