import json
import logging
from facebook_ads_connector import fetch_facebook_ads_data
from google_ads_connector import fetch_google_ads_data
from twitter_ads_connector import fetch_twitter_ads_data
from google.cloud import storage

# Initialize the GCS client
storage_client = storage.Client()

def upload_to_gcs(bucket_name, destination_blob_name, data):
    """Uploads data to the GCS bucket."""
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(json.dumps(data), content_type="application/json")
    logging.info(f"Data uploaded to {destination_blob_name} in bucket {bucket_name}")


def main(event=None, context=None):
    """Main function to fetch data and upload it to GCS."""

    gcs_bucket_name = "marketing-data-ingestion"

    try:
        # Example: Fetch data from Facebook Ads API
        facebook_data = fetch_facebook_ads_data(ad_account_id="12345", access_token="<ACCESS_TOKEN>")
        upload_to_gcs(gcs_bucket_name, "facebook_ads_data.json", facebook_data)
        logging.info("Facebook Ads data uploaded successfully to GCS")

        # Example: Fetch data from Google Ads API
        google_data = fetch_google_ads_data(client_customer_id="12345", developer_token="<DEVELOPER_TOKEN>", access_token="<ACCESS_TOKEN>")
        upload_to_gcs(gcs_bucket_name, "google_ads_data.json", google_data)
        logging.info("Google Ads data uploaded successfully to GCS")

        # Example: Fetch data from Twitter Ads API
        twitter_data = fetch_twitter_ads_data(account_id="12345", access_token="<ACCESS_TOKEN>")
        upload_to_gcs(gcs_bucket_name, "twitter_ads_data.json", twitter_data)
        logging.info("Twitter Ads data uploaded successfully to GCS")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

