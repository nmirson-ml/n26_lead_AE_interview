#!/bin/bash

# Deploy Kafka Connect BigQuery Sink Connector
curl -X POST -H "Content-Type: application/json" \
    --data @kafka_connect/bigquery_sink_connector.json \
    http://localhost:8083/connectors

echo "Kafka Connect BigQuery Sink Connector deployed."
