# n26_lead_AE_interview
Repo for the self_service data ingestion platform


Project diagram 

├── api_connectors/
│   ├── __init__.py
│   ├── facebook_ads_connector.py
│   ├── google_ads_connector.py
│   ├── twitter_ads_connector.py
│   ├── kafka_producer.py
│   └── kafka_publisher.py
│
├── etl/
│   ├── __init__.py
│   ├── transformations.py
│   └── dbt/
│       ├── models/
│       │   ├── facebook_ads_transformed.sql
│       │   ├── google_ads_transformed.sql
│       ├── dbt_project.yml
│       └── profiles.yml
│
├── data_validation/
│   ├── __init__.py
│   ├── polars_data_validation.py
│   ├── validation_config/
│   │   ├── facebook_ads_expectations.yml
│   │   └── google_ads_expectations.yml
│
├── error_handling/
│   ├── __init__.py
│   ├── error_logger.py
│   └── retry_handler.py
│
├── kafka_connect/
│   ├── bigquery_sink_connector.json
│   ├── deploy_connector.sh
│   └── credentials/
│       └── service_account.json
│
├── docker/
│   ├── Dockerfile.api_connectors
│   ├── Dockerfile.etl
│   └── Dockerfile.data_validation
│
├── scripts/
│   ├── start_kafka_connect.sh
│   ├── run_etl_with_dbt.sh
│   ├── run_data_validation.sh
│   └── run_error_monitoring.sh
│
├── config/
│   ├── dev.env
│   └── prod.env
└── README.md


External links used for this project are: 

Tech stack used in N26 - overview of architecture 
- https://medium.com/insiden26/engineering-at-n26-a-tour-of-our-tech-stack-and-architecture-9e58ce96f889

Interview to Analytics Engineer in N26.
- https://www.youtube.com/watch?v=kqm3VcyWS3o

Characteristics of a Self Serving Data Lake
-https://medium.com/engineered-publicis-sapient/characteristics-and-architecture-of-a-self-service-data-lake-a3eb61aac032

For streaming data into GBQ 
- https://medium.com/myheritage-engineering/kafka-to-bigquery-load-a-guide-for-streaming-billions-of-daily-events-cbbf31f4b737

Transformations using Polars
-https://towardsdatascience.com/improving-code-quality-during-data-transformation-with-polars-92997e67c8a9

