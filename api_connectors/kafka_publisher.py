from kafka_producer import create_kafka_producer, send_data_to_kafka
from facebook_ads_connector import fetch_facebook_ads_data
from google_ads_connector import fetch_google_ads_data
from twitter_ads_connector import fetch_twitter_ads_data
import logging

logging.basicConfig(level=logging.INFO)

def main():
    """
    Main function to fetch data from various APIs and send it to Kafka topics.
    """
    try:
        # Create Kafka producer
        producer = create_kafka_producer(["localhost:9092"])

        # Fetch and send Facebook Ads data
        facebook_data = fetch_facebook_ads_data("your_ad_account_id", "your_facebook_access_token")
        send_data_to_kafka(producer, "facebook_ads_topic", facebook_data)

        # Fetch and send Google Ads data
        google_data = fetch_google_ads_data("your_client_customer_id", "your_google_ads_developer_token", "your_google_access_token")
        send_data_to_kafka(producer, "google_ads_topic", google_data)

        # Fetch and send Twitter Ads data
        twitter_data = fetch_twitter_ads_data("your_account_id", "your_twitter_access_token")
        send_data_to_kafka(producer, "twitter_ads_topic", twitter_data)

    except Exception as e:
        logging.error(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
