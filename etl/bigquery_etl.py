import polars as pl
from google.cloud import storage, bigquery
import transformations

def load_data_from_gcs(bucket_name, blob_name):
    """Loads data from a GCS bucket into a Polars DataFrame."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    data = blob.download_as_string()

    # Load data into Polars DataFrame
    return pl.read_json(data)

def insert_data_into_bigquery(df, dataset_id, table_id):
    """Inserts data into a BigQuery table."""
    bq_client = bigquery.Client()
    table_ref = bq_client.dataset(dataset_id).table(table_id)

    # Convert Polars DataFrame to Pandas DataFrame for BigQuery insertion
    df_pandas = df.to_pandas()

    # Insert the data from Pandas DataFrame into BigQuery
    job = bq_client.load_table_from_dataframe(df_pandas, table_ref)
    job.result()  # Wait for the job to complete

    if job.errors:
        raise Exception(f"Errors occurred while inserting data into BigQuery: {job.errors}")
    else:
        print(f"Data successfully inserted into {dataset_id}.{table_id}")

def run_bigquery_etl(gcs_bucket_name, gcs_blob_name, dataset_id, table_id):
    """Runs the ETL process for loading data from GCS, transforming it, and inserting it into BigQuery."""
    
    # Step 1: Load data from GCS into a Polars DataFrame
    df = load_data_from_gcs(gcs_bucket_name, gcs_blob_name)
    
    # Step 2: Apply transformations using Polars
    transformed_df = transformations.transform_data(df)
    
    # Step 3: Insert the transformed data into BigQuery
    insert_data_into_bigquery(transformed_df, dataset_id, table_id)

