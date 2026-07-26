from dotenv import load_dotenv
import os

load_dotenv()

DB_SERVER = os.getenv('DB_SERVER')
DB_NAME = os.getenv('BuzzliveWarehouse')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DRIVER = os.getenv('DB_DRIVER')
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')