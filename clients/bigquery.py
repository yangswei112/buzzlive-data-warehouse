import os
from google.cloud import bigquery
import pandas as pd
from config.settings import GOOGLE_APPLICATION_CREDENTIALS

class BigQueryConn:
    def __init__(self, project_id = 'hashent-410002', dataset_id = 'buzzwh'):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.client = bigquery.Client(project=self.project_id)
        self.dataset_ref = f"{self.project_id}.{self.dataset_id}"
        print(f"Connected to BigQuery project: {self.project_id}, dataset: {self.dataset_id}")

    def load_dataframe_to_bigquery(self, df: pd.DataFrame):
        df_to_load = df.copy()

        # 2. Safely cast date strings to datetime/date objects if column exists
        if 'live_start_date' in df_to_load.columns:
            df_to_load['live_start_date'] = pd.to_datetime(
                df_to_load['live_start_date'], errors='coerce'
            ).dt.date

        table_id = f"{self.dataset_ref}.raw_data_livestreaming"
        job = self.client.load_table_from_dataframe(df_to_load, table_id)
        job.result()  # Wait for the job to complete.
        print(f"Loaded {job.output_rows} rows into {table_id}.")