from utils.buzzwh_transform import *


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
def load():
        pass   
