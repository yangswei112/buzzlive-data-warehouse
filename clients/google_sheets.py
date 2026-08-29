import gspread
import google.auth
from gspread_dataframe import set_with_dataframe
import pandas as pd
from config.settings import GOOGLE_APPLICATION_CREDENTIALS
from googleapiclient.discovery import build

class GoogleSheetsConn:
    def __init__(self):
        self.gc = gspread.service_account(filename=GOOGLE_APPLICATION_CREDENTIALS)
        print("Connected to Google Sheets API")
    
    def load_dataframe_to_sheet(self, df: pd.DataFrame, spreadsheet_name: str, worksheet_name='Sheet1'):
        sh = self.gc.open(spreadsheet_name)
        worksheet = sh.worksheet(worksheet_name)
        worksheet.clear()  # Clear existing data
        set_with_dataframe(worksheet, df, row=1, col=1)
        print(f"Loaded dataframe to Google Sheet: {spreadsheet_name}, Worksheet: {worksheet_name}")

    def create_sheet_in_folder(self, title: str, folder_id: str):
        # Authenticate with Drive scope
        credentials, project = google.auth.default(
            scopes=['https://www.googleapis.com/auth/drive']
        )
        drive_service = build('drive', 'v3', credentials=credentials)

        # Define metadata with MIME type for Google Sheets and parent folder ID
        file_metadata = {
            'name': title,
            'mimeType': 'application/vnd.google-apps.spreadsheet',
            'parents': [folder_id]
        }

        # Create the file in Google Drive
        file = drive_service.files().create(
            body=file_metadata,
            supportsAllDrives=True,
            fields='id, name'
        ).execute()

        print(f"Created '{file.get('name')}' in Folder ID: {folder_id}")
        print(f"File ID: {file.get('id')}")
        return file.get('id')