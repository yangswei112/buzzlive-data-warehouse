from scripts.buzzwh import *
from clients.google_sheets import GoogleSheetsConn
import utils.buzzwh_transform as bt


def update_monthly():
    shopee_report_path = 'C:/datasets/shopee seller center/update/'
    tiktok_report_path = 'C:/datasets/tiktok seller center/update/'

    update_shopee_sales(shopee_report_path)
    update_tiktok_sales(tiktok_report_path)

def update_monthly_2():
    shopee_report_path = 'C:/datasets/shopee seller center/update/'
    tiktok_report_path = 'C:/datasets/tiktok seller center/update/'
    # SET UP THE DATABASE CONNECTION
    connection_string = ("DRIVER={SQL Server};PORT=1433;SERVER=LAPTOP-Q4096V85\SQLEXPRESS;DATABASE=BuzzliveWarehouse;UID=buzzlive;PWD=Speakup40!;Encrypt=No;")

    bt.update_shopee_sales(shopee_path=shopee_report_path, connection_db=connection_string)
    bt.update_tiktok_sales(tiktok_path=tiktok_report_path, connection_db=connection_string)

def load_raw_komisi_shopee_all(start_date, end_date, monthyear):
    """
    monthyear = 'aug-2026'
    """
    gs = GoogleSheetsConn()
    brands = ['Ortuseight','Deltomed','Heavenly Yogurt',
              'Samyang','Herbana','Herbamojo']
    for brand in brands:
        FOLDER_ID_shopee = "1j0Zrd0PzQWhm6tkG-JvJylTFKH5z3KLA"
        sheet_name_shopee = f"{brand}-gmv-shopee-{monthyear}"
        df_shopee = get_silver_data_shopee(start_date=start_date, end_date=end_date, brand_name=brand)
        gs.create_sheet_in_folder(title=sheet_name_shopee, folder_id=FOLDER_ID_shopee)
        gs.load_dataframe_to_sheet(df = df_shopee, spreadsheet_name=sheet_name_shopee)

def load_raw_komisi_tiktok_all(start_date, end_date, monthyear):
    """
    monthyear = 'aug-2026'
    """
    gs = GoogleSheetsConn()
    brands = ['Ortuseight','Deltomed',
              'Medikon','Samyang','Herbana','Herbamojo']
    for brand in brands:
        FOLDER_ID_tiktok = "1Gbnl0Nfvq89geo80fjT-1xYhA9kYK1xZ"
        sheet_name_tiktok = f"{brand}-gmv-tiktok-{monthyear}"
        df_tiktok = get_silver_data_shopee(start_date=start_date, end_date=end_date, brand_name=brand)
        gs.create_sheet_in_folder(title=sheet_name_tiktok, folder_id=FOLDER_ID_tiktok)
        gs.load_dataframe_to_sheet(df = df_tiktok, spreadsheet_name=sheet_name_tiktok)

def load_shopee_seller_to_sheet(start_date_monthly, end_date_monthly):
    gs = GoogleSheetsConn()
    shopee_seller_df = get_shopee_seller_data(start_date=start_date_monthly, end_date=end_date_monthly)
    gs.load_dataframe_to_sheet(shopee_seller_df, 'monthlyreport_shopee', 'from_db_shopee')

def backup_db(month: str):
    backup_database(monthyear=month)