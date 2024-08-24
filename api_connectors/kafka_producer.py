from kafka import KafkaProducer
import json
import logging

logging.basicConfig(level=logging.INFO)

def create_kafka_producer(bootstrap_servers):
    """
    Create and return a Kafka producer.

    Args:
    - bootstrap_servers (list): List of Kafka bootstrap servers.

    Returns:
    - KafkaProducer: Configured Kafka producer instance.
    """
    try:
        producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        return producer
    except Exception as e:
        logging.error(f"Error creating Kafka producer: {e}")
        raise

def send_data_to_kafka(producer, topic, data):
    """
    Send data to a Kafka topic.

    Args:
    - producer (KafkaProducer): The Kafka producer instance.
    - topic (str): The Kafka topic to send data to.
    - data (dict): Data to send to the Kafka topic.

    Raises:
    - Exception: If any error occurs during sending to Kafka.
    """
    try:
        producer.send(topic, value=data)
        producer.flush()
        logging.info(f"Data sent to Kafka topic {topic}")
    except Exception as e:
        logging.error(f"Error sending data to Kafka topic {topic}: {e}")
        raise
