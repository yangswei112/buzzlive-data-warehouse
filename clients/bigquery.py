import os
from google.cloud import bigquery
import pandas as pd
from config.settings import GOOGLE_APPLICATION_CREDENTIALS

class BigQueryWarehouse:
    def __init__(self, project_id = 'hashent-410002', dataset_id = 'buzzwh'):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.client = bigquery.Client(project=self.project_id)
        self.dataset_ref = f"{self.project_id}.{self.dataset_id}"
        print(f"Connected to BigQuery project: {self.project_id}, dataset: {self.dataset_id}")

    def load_dataframe_to_bigquery(self, df: pd.DataFrame):
        table_id = f"{self.dataset_ref}.raw_data_livestreaming"
        job = self.client.load_table_from_dataframe(df, table_id)
        job.result()  # Wait for the job to complete.
        print(f"Loaded {job.output_rows} rows into {table_id}.")