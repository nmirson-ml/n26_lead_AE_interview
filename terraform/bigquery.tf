resource "google_bigquery_dataset" "marketing_data" {
  dataset_id = "marketing_data"
  project    = var.gcp_project_id
  location   = var.gcp_region
}

resource "google_bigquery_table" "facebook_ads" {
  dataset_id = google_bigquery_dataset.marketing_data.dataset_id
  table_id   = "facebook_ads_raw"
  schema     = file("schemas/facebook_ads_schema.json")
  project    = var.gcp_project_id
}

resource "google_bigquery_table" "google_ads" {
  dataset_id = google_bigquery_dataset.marketing_data.dataset_id
  table_id   = "google_ads_raw"
  schema     = file("schemas/google_ads_schema.json")
  project    = var.gcp_project_id
}


resource "google_bigquery_table" "twitter_ads" {
  dataset_id = google_bigquery_dataset.marketing_data.dataset_id
  table_id   = "twitter_ads_raw"
  schema     = file("schemas/twitter_ads_schema.json")
  project    = var.gcp_project_id
}


resource "google_bigquery_table" "facebook_ads_transformed" {
  dataset_id = google_bigquery_dataset.marketing_data.dataset_id
  table_id   = "facebook_ads_transformed"
  schema     = file("schemas/facebook_ads_transformed_schema.json")
  project    = var.gcp_project_id
}

resource "google_bigquery_table" "google_ads_transformed" {
  dataset_id = google_bigquery_dataset.marketing_data.dataset_id
  table_id   = "google_ads_transformed"
  schema     = file("schemas/google_ads_transformed_schema.json")
  project    = var.gcp_project_id
}

resource "google_bigquery_table" "twitter_ads_transformed" {
  dataset_id = google_bigquery_dataset.marketing_data.dataset_id
  table_id   = "twitter_ads_transformed"
  schema     = file("schemas/twitter_ads_transformed_schema.json")
  project    = var.gcp_project_id
}