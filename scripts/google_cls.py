import os
from google.cloud import bigquery
import gspread
from gspread_dataframe import set_with_dataframe
import pandas as pd

class BigQueryWarehouse:
    PROJECT_ID = 'hashent-410002'
    DATASET_ID = 'buzzwh'
    KEY_PATH = 'gcp-keys\\hashent-410002-3e7f0c1d5b4e.json'

    def __init__(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = BigQueryWarehouse.KEY_PATH
        self.client = bigquery.Client(project=BigQueryWarehouse.PROJECT_ID)
        self.dataset_ref = f"{BigQueryWarehouse.PROJECT_ID}.{BigQueryWarehouse.DATASET_ID}"
        print(f"Connected to BigQuery project: {BigQueryWarehouse.PROJECT_ID}, dataset: {BigQueryWarehouse.DATASET_ID}")

    def load_dataframe_to_bigquery(self, df: pd.DataFrame):
        table_id = f"{self.dataset_ref}.example"
        job = self.client.load_table_from_dataframe(df, table_id)
        job.result()  # Wait for the job to complete.
        print(f"Loaded {job.output_rows} rows into {table_id}.")


class GoogleSheetsConn:
    def __init__(self):
        self.gc = gspread.service_account(filename='gcp-keys\\hashent-410002-3e7f0c1d5b4e.json')
        print("Connected to Google Sheets API")
    
    def load_dataframe_to_sheet(self, df: pd.DataFrame, spreadsheet_name: str, worksheet_name: str):
        sh = self.gc.open(spreadsheet_name)
        worksheet = sh.worksheet(worksheet_name)
        worksheet.clear()  # Clear existing data
        set_with_dataframe(worksheet, df, row=1, col=1)
        print(f"Loaded dataframe to Google Sheet: {spreadsheet_name}, Worksheet: {worksheet_name}")