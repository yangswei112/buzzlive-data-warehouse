# config/settings.py
import os
from dotenv import load_dotenv

# Automatically locate and load .env file from the project root
load_dotenv()

DB_SERVER = os.getenv("DB_SERVER", r"LAPTOP-Q4096V85\SQLEXPRESS")
DB_NAME = os.getenv("DB_NAME", "BuzzliveWarehouse")
DB_USERNAME = os.getenv("DB_USERNAME", "de_project")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')