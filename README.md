# N26 Lead Analytics Engineer - Marketing 

## Case Study 

This repository contains a **Self-Serve Data Ingestion Platform** for ingesting data from multiple marketing APIs (e.g., Facebook Ads, Google Ads, Twitter Ads) into **Google BigQuery**. The platform uses **Kafka Connect** for streaming data and **dbt** for transforming raw data into meaningful insights. All infrastructure, including BigQuery tables and Kafka Connectors, is managed using **Terraform**.

## Project Overview

### Key Components

- **API Connectors**: Fetches data from marketing APIs (e.g., Facebook Ads, Google Ads, Twitter Ads) and streams it into Kafka topics.
- **Kafka Connect**: Streams data from Kafka topics into BigQuery.
- **BigQuery**: Stores both raw and transformed marketing data.
- **dbt**: Transforms raw data into processed tables for analysis, such as calculating click-through rates (CTR).
- **Data Validation**: Ensures data quality using **Polars**.
- **Error Handling**: Logs errors and implements retry mechanisms.
- **Terraform**: Manages infrastructure as code, including BigQuery datasets, tables, and Kafka Connect configurations.
- **CI/CD Integration**: Ensures continuous integration with test coverage and automated infrastructure deployment.

## Project Structure

```bash
self_serve_data_ingestion_platform/
├── api_connectors/
│   ├── __init__.py
│   ├── facebook_ads_connector.py
│   ├── google_ads_connector.py
│   ├── twitter_ads_connector.py
│   ├── kafka_producer.py
│   └── kafka_publisher.py
├── etl/
│   ├── __init__.py
│   ├── transformations.py
│   └── dbt/
│       ├── models/
│       │   ├── facebook_ads/
│       │   │   ├── facebook_ads_raw.sql
│       │   │   ├── facebook_ads_transformed.sql
│       │   ├── google_ads/
│       │   │   ├── google_ads_raw.sql
│       │   │   ├── google_ads_transformed.sql
│       │   ├── twitter_ads/
│       │   │   ├── twitter_ads_raw.sql
│       │   │   ├── twitter_ads_transformed.sql
│       ├── dbt_project.yml
│       └── profiles.yml
├── data_validation/
│   ├── __init__.py
│   ├── polars_data_validation.py
├── error_handling/
│   ├── __init__.py
│   ├── error_logger.py
│   └── retry_handler.py
├── kafka_connect/
│   ├── deploy_connector.sh
│   └── credentials/
│       └── service_account.json
├── docker/
│   ├── Dockerfile.api_connectors
│   ├── Dockerfile.etl
│   └── Dockerfile.data_validation
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── bigquery.tf
│   ├── kafka_connect.tf
│   ├── schemas/
│   │   ├── facebook_ads_schema.json
│   │   ├── facebook_ads_transformed_schema.json
│   │   ├── google_ads_schema.json
│   │   ├── google_ads_transformed_schema.json
│   │   ├── twitter_ads_schema.json
│   │   ├── twitter_ads_transformed_schema.json
├── tests/
│   ├── __init__.py
│   ├── test_api_connectors.py
│   ├── test_etl.py
│   ├── test_data_validation.py
│   ├── test_error_handling.py
│   ├── test_kafka_connect.py
├── scripts/
│   ├── start_kafka_connect.sh
│   ├── run_etl_with_dbt.sh
│   ├── run_data_validation.sh
│   └── run_error_monitoring.sh
├── docker-compose.yml
└── README.md
```


## How to Use

### 1. API Connectors
- **Purpose**: Fetches data from marketing APIs (e.g., Facebook Ads, Google Ads) and streams it into Kafka.
- **Files**: Located in `api_connectors/`.

### 2. ETL
- **Purpose**: Transforms data using **dbt** and handles data processing with **Polars**. This includes both raw and transformed tables stored in BigQuery.
- **Files**: Located in `etl/`.

### 3. Data Validation
- **Purpose**: Validates data using **Polars** and ensures data quality based on defined expectations and validation rules.
- **Files**: Located in `data_validation/`.

### 4. Kafka Connect
- **Purpose**: Streams data from Kafka topics into Google BigQuery using the **Kafka Connect BigQuery Sink** connector. Managed by Terraform for easy scaling and configuration.
- **Files**: Located in `kafka_connect/`.

### 5. Error Handling
- **Purpose**: Provides error logging and retry mechanisms for transient issues, ensuring stability in the platform.
- **Files**: Located in `error_handling/`.

### 6. Docker
- **Purpose**: Containerizes different components of the platform for consistency, repeatability, and ease of deployment. 
- **Files**: Dockerfiles are located in `docker/`.

### 7. Scripts
- **Purpose**: Automates the execution and deployment of the various components in the data pipeline, including Kafka Connect setup, ETL, data validation, and error monitoring.
- **Files**: Located in `scripts/`.

### 8. Tests
- **Purpose**: Ensures all components are functioning as expected with 100% test coverage across the codebase. Unit tests cover API connectors, ETL processes, data validation, error handling, and Kafka integration.
- **Files**: Located in `tests/`.

### 9. Terraform
- **Purpose**: Manages infrastructure as code, including provisioning and configuration of BigQuery datasets, tables, and Kafka Connect connectors. It ensures that infrastructure is consistently deployed and managed.
- **Files**: Located in `terraform/`.

## Environments

This platform supports multiple environments (e.g., `dev`, `prod`). Environment-specific configurations are stored in the `config/` directory.

- **dev.env**: Development environment configuration.
- **prod.env**: Production environment configuration.

To switch between environments, load the appropriate environment configuration from the `config/` directory. Each environment configuration contains the necessary environment variables and settings to adjust the behavior of the platform components.




## External Resources Used in This Project

This project is inspired by various concepts and tools related to the self-service data ingestion platform and the tech stack at N26. Below are some key references used during the development of this platform:

1. **Tech Stack Used in N26 - Overview of Architecture**  
   Gain insight into the technology and architecture used at N26:
   - [Engineering at N26: A Tour of Our Tech Stack and Architecture](https://medium.com/insiden26/engineering-at-n26-a-tour-of-our-tech-stack-and-architecture-9e58ce96f889)

2. **Interview with Analytics Engineer at N26**  
   Watch an interview with an Analytics Engineer at N26 to understand the role's responsibilities and expectations:
   - [Interview with Analytics Engineer at N26](https://www.youtube.com/watch?v=kqm3VcyWS3o)

3. **Characteristics of a Self-Service Data Lake**  
   Explore the characteristics and architecture of a self-service data lake:
   - [Characteristics and Architecture of a Self-Service Data Lake](https://medium.com/engineered-publicis-sapient/characteristics-and-architecture-of-a-self-service-data-lake-a3eb61aac032)

4. **Streaming Data into BigQuery**  
   Learn how to stream billions of daily events from Kafka to BigQuery:
   - [Kafka to BigQuery Load: A Guide for Streaming Billions of Daily Events](https://medium.com/myheritage-engineering/kafka-to-bigquery-load-a-guide-for-streaming-billions-of-daily-events-cbbf31f4b737)

5. **Transformations Using Polars**  
   Discover how Polars can improve data transformation and code quality:
   - [Improving Code Quality During Data Transformation with Polars](https://towardsdatascience.com/improving-code-quality-during-data-transformation-with-polars-92997e67c8a9)

