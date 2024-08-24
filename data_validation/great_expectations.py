import polars as pl
import great_expectations as ge
from google.cloud import storage, bigquery
from ruamel.yaml import YAML
from io import StringIO

def load_validation_config(file_path):
    """Loads the validation configuration from a YAML file."""
    yaml = YAML()
    with open(file_path, 'r') as stream:
        config = yaml.load(stream)
    return config

def load_data_from_gcs(bucket_name, blob_name):
    """Loads data from a GCS bucket into a Polars DataFrame."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    data = blob.download_as_string()
    return pl.read_json(StringIO(data.decode('utf-8')))

def validate_data(df, validation_config):
    """Validates the data using Great Expectations."""
    # Convert Polars DataFrame to Great Expectations-compatible Polars DataFrame
    ge_df = ge.dataset.PolarsDataset(df)
    
    # Apply the validation expectations from the configuration
    validation_results = ge_df.validate(expectation_suite=validation_config)
    
    return validation_results

def run_data_validation(gcs_bucket_name, gcs_blob_name, validation_config_path):
    """Runs the full data validation process."""
    # Step 1: Load the validation config from YAML
    validation_config = load_validation_config(validation_config_path)

    # Step 2: Load the data from GCS into a Polars DataFrame
    df = load_data_from_gcs(gcs_bucket_name, gcs_blob_name)

    # Step 3: Validate the data using Great Expectations
    validation_results = validate_data(df, validation_config)

    # Print validation results summary
    if validation_results["success"]:
        print("Data validation passed successfully.")
    else:
        print("Data validation failed. Review the validation results.")
    
    return validation_results


if __name__ == "__main__":
    # Example usage - Replace with actual GCS bucket, file, and validation config
    gcs_bucket_name = "your-gcs-bucket-name"
    gcs_blob_name = "facebook_ads_data.json"
    validation_config_path = "data_validation/validation_config/facebook_ads_expectations.yml"
    
    run_data_validation(gcs_bucket_name, gcs_blob_name, validation_config_path)
