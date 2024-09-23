import polars as pl
from google.cloud import bigquery
from datetime import timedelta, datetime, date
from dateutil.relativedelta import relativedelta
import glob
import os

client = bigquery.Client()

run_table = pl.from_arrow(client.query(f"SELECT * FROM `github-actions-testing-435312.test_run.run_table`").to_arrow())

run_table.write_parquet('run_table.parquet')

run_table_id = f"github-actions-testing-435312.test_run.run_table_new"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.PARQUET,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)

with open("run_table.parquet", "rb") as f:
    job = client.load_table_from_file(f, run_table_id, job_config=job_config)

job.result()
