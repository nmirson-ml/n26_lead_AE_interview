provider "google" {
  project = "your-gcp-project-id"  # Replace with your Google Cloud project ID
  region  = "us-central1"
}

# Create GCS bucket for data storage
resource "google_storage_bucket" "data_ingestion_bucket" {
  name     = "marketing-data-ingestion"
  location = "US"
}

# Create BigQuery dataset
resource "google_bigquery_dataset" "marketing_dataset" {
  dataset_id = "marketing_dataset"
  location   = "US"
}

# Create BigQuery table for Facebook Ads
resource "google_bigquery_table" "facebook_ads_table" {
  dataset_id = google_bigquery_dataset.marketing_dataset.dataset_id
  table_id   = "facebook_ads"
  schema     = <<EOF
[
  {
    "name": "campaign_name",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "clicks",
    "type": "INTEGER",
    "mode": "NULLABLE"
  },
  {
    "name": "impressions",
    "type": "INTEGER",
    "mode": "NULLABLE"
  },
  {
    "name": "ctr",
    "type": "FLOAT",
    "mode": "NULLABLE"
  },
  {
    "name": "date",
    "type": "DATE",
    "mode": "NULLABLE"
  }
]
EOF
}

# Create BigQuery table for Google Ads
resource "google_bigquery_table" "google_ads_table" {
  dataset_id = google_bigquery_dataset.marketing_dataset.dataset_id
  table_id   = "google_ads"
  schema     = <<EOF
[
  {
    "name": "ad_group_name",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "clicks",
    "type": "INTEGER",
    "mode": "NULLABLE"
  },
  {
    "name": "impressions",
    "type": "INTEGER",
    "mode": "NULLABLE"
  },
  {
    "name": "cost",
    "type": "FLOAT",
    "mode": "NULLABLE"
  },
  {
    "name": "date",
    "type": "DATE",
    "mode": "NULLABLE"
  }
]
EOF
}

# Create BigQuery table for Twitter Ads
resource "google_bigquery_table" "twitter_ads_table" {
  dataset_id = google_bigquery_dataset.marketing_dataset.dataset_id
  table_id   = "twitter_ads"
  schema     = <<EOF
[
  {
    "name": "ad_group_name",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "clicks",
    "type": "INTEGER",
    "mode": "NULLABLE"
  },
  {
    "name": "impressions",
    "type": "INTEGER",
    "mode": "NULLABLE"
  },
  {
    "name": "cost",
    "type": "FLOAT",
    "mode": "NULLABLE"
  },
  {
    "name": "date",
    "type": "DATE",
    "mode": "NULLABLE"
  }
]
EOF
}
