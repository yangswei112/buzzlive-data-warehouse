import gspread
from gspread_dataframe import set_with_dataframe
import pandas as pd
from config.settings import GOOGLE_APPLICATION_CREDENTIALS

class GoogleSheetsConn:
    def __init__(self):
        self.gc = gspread.service_account(filename=GOOGLE_APPLICATION_CREDENTIALS)
        print("Connected to Google Sheets API")
    
    def load_dataframe_to_sheet(self, df: pd.DataFrame, spreadsheet_name: str, worksheet_name: str):
        sh = self.gc.open(spreadsheet_name)
        worksheet = sh.worksheet(worksheet_name)
        worksheet.clear()  # Clear existing data
        set_with_dataframe(worksheet, df, row=1, col=1)
        print(f"Loaded dataframe to Google Sheet: {spreadsheet_name}, Worksheet: {worksheet_name}")