resource "google_storage_bucket_object" "function_zip" {
  name   = "cloud_function_code.zip"
  bucket = google_storage_bucket.data_ingestion_bucket.name
  source = "path/to/your/cloud_function_code.zip"  # Replace with actual path
}

resource "google_cloudfunctions_function" "data_processing_function" {
  name        = "data_processing_function"
  runtime     = "python39"
  trigger_http = true
  entry_point = "main"
  
  source_archive_bucket = google_storage_bucket.data_ingestion_bucket.name
  source_archive_object = google_storage_bucket_object.function_zip.name

  environment_variables = {
    BIGQUERY_DATASET = google_bigquery_dataset.marketing_dataset.dataset_id
    FACEBOOK_ADS_TABLE = google_bigquery_table.facebook_ads_table.table_id
    GOOGLE_ADS_TABLE = google_bigquery_table.google_ads_table.table_id
  }
}
