import unittest
from unittest.mock import patch, MagicMock
from api_connectors.facebook_ads_connector import fetch_facebook_ads_data
from api_connectors.google_ads_connector import fetch_google_ads_data
from api_connectors.twitter_ads_connector import fetch_twitter_ads_data
from api_connectors.kafka_producer import create_kafka_producer, send_data_to_kafka

class TestAPIConnectors(unittest.TestCase):

    @patch('api_connectors.facebook_ads_connector.requests.get')
    def test_fetch_facebook_ads_data(self, mock_get):
        # Setup the mock response
        mock_get.return_value = MagicMock(status_code=200)
        mock_get.return_value.json.return_value = {"data": "test"}
        
        # Test the function
        data = fetch_facebook_ads_data("account_id", "access_token")
        
        # Assertions
        mock_get.assert_called_once()
        self.assertEqual(data, {"data": "test"})

    @patch('api_connectors.google_ads_connector.requests.post')
    def test_fetch_google_ads_data(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200)
        mock_post.return_value.json.return_value = {"data": "test"}
        
        data = fetch_google_ads_data("customer_id", "dev_token", "access_token")
        
        mock_post.assert_called_once()
        self.assertEqual(data, {"data": "test"})

    @patch('api_connectors.twitter_ads_connector.requests.get')
    def test_fetch_twitter_ads_data(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200)
        mock_get.return_value.json.return_value = {"data": "test"}
        
        data = fetch_twitter_ads_data("account_id", "access_token")
        
        mock_get.assert_called_once()
        self.assertEqual(data, {"data": "test"})

    @patch('api_connectors.kafka_producer.KafkaProducer')
    def test_create_kafka_producer(self, mock_kafka_producer):
        producer = create_kafka_producer(["localhost:9092"])
        self.assertIsNotNone(producer)
        mock_kafka_producer.assert_called_once()

    @patch('api_connectors.kafka_producer.KafkaProducer.send')
    def test_send_data_to_kafka(self, mock_send):
        producer = MagicMock()
        send_data_to_kafka(producer, "test_topic", {"key": "value"})
        mock_send.assert_called_once_with("test_topic", value={"key": "value"})

if __name__ == '__main__':
    unittest.main()
