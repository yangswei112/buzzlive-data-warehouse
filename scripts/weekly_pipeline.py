from utils.buzzwh_transform import *
from scripts.buzzwh import *
from clients.bigquery import BigQueryConn
from clients.google_sheets import GoogleSheetsConn


# EXTRACT
def extract():
    """
    to extract data from source (shopee & tiktok seller center)
    """
    # Extract livestreaming data from shopee and tiktok seller center
    shopee_report_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/buzzlive-data-warehouse/datasets/shopee seller center/to-trf/'
    tiktok_report_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/buzzlive-data-warehouse/datasets/tiktok seller center/to-trf/'

    return shopee_report_path, tiktok_report_path

# TRANSFORM
def transform():
    """
    to tansform extracted data to match the database schema
    """
    result_path = 'C:/Users/ASUS/Documents/Data Engineering/BuzzliveWarehouse/buzzlive-data-warehouse/datasets/result/'
    shopee_transform_action(extract()[0], result_path)
    tiktok_transform_action(extract()[1], result_path)

 # LOAD
def load_to_database(start_date_weekly, end_date_weekly):
    """
    to load the transformed data to the database
    """
    # load the transformed data to database
    load_to_db(start_date=start_date_weekly, end_date=end_date_weekly)

    print("data successfully loaded into database")

def load_to_bigquery(start_date_weekly, end_date_weekly):
    bq = BigQueryConn()
    # load the gold bronze data to bigquery
    gold_bronze_df = get_raw_data_from_db(start_date=start_date_weekly, end_date=end_date_weekly)
    gold_bronze_df['live_start_date'] = gold_bronze_df['live_start_date'].astype("string")
    bq.load_dataframe_to_bigquery(gold_bronze_df)

    print("data successfully loaded to bigquery")

def load_to_gsheet(start_date_weekly, end_date_weekly):
    gs = GoogleSheetsConn()
    # load the gold silver data to google sheet
    gold_silver_df = get_gold_silver_data(start_date=start_date_weekly, end_date=end_date_weekly)
    gs.load_dataframe_to_sheet(gold_silver_df, spreadsheet_name='data-to-dashboard', worksheet_name='from_db')

    print("data successfully loaded to 'data-to-dashboard' google sheet")

def load_silver_to_sheets(start_date_weekly, end_date_weekly):
    brand_gsheet_dct = {
    'Ortuseight': 'ORTUSEIGHT REPORT 2026 (NEW)',
    'Beeme': "BEEME REPORT 2026 (NEW)",
    'Bloomlab': 'BLOOMLAB REPORT 2026 (NEW)',
    'Deltomed': 'DELTOMED REPORT 2026',
    'Everbest': 'EVERBEST REPORT 2026 (NEW)',
    'Heavenly Yogurt': 'HEAVENLY YOGURT REPORT 2026 (NEW)',
    'Medikon': 'MEDIKON REPORT 2026 (NEW)',
    'Ona Indonesia': 'ONA INDONESIA REPORT 2026 (NEW)',
    'Pafle': 'PAFLE REPORT 2026 (NEW)',
    'Samyang': 'SAMYANG FOOD INDONESIA REPORT 2026 (NEW)',
    'Tataruma': 'TATARUMA REPORT 2026 (NEW)',
    'Wund+': 'WUND+ REPORT 2026 (NEW)',
    'Skinflair': 'SKINFLAIR REPORT 2026 (NEW)'}
    gs = GoogleSheetsConn()
    for brand, gsheet in brand_gsheet_dct.items():
        silver_shopee_df = get_silver_data_shopee(start_date=start_date_weekly, end_date=end_date_weekly, brand_name=brand)
        silver_tiktok_df = get_silver_data_tiktok(start_date=start_date_weekly, end_date=end_date_weekly, brand_name=brand)
        gs.load_dataframe_to_sheet(df=silver_shopee_df, spreadsheet_name=gsheet, worksheet_name='from_db_shopee')
        gs.load_dataframe_to_sheet(df=silver_tiktok_df, spreadsheet_name=gsheet, worksheet_name='from_db_tiktok')
        print(f"{brand} data has been loaded to google sheets")

    print("data successfully loaded to each brand gsheets")