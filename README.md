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

## Key Features
### API Connectors:

- Fetches data from marketing APIs.
- Sends the data to Kafka topics.

### Terraform:

- **Infrastructure as Code**: Manages BigQuery datasets, tables, and Kafka Connect configuration.
- **Automated Deployment**: Ensures infrastructure is created and configured consistently.

### Kafka Connect:

- Streams raw data from Kafka topics to BigQuery tables.
- Managed through Terraform for easy scaling and management.

### ETL & dbt:

- **Raw Data Tables**: Data is initially stored in raw tables (e.g., facebook_ads_raw, google_ads_raw).
- **Transformed Data Tables**: dbt models transform the raw data into tables that calculate key metrics like CTR (facebook_ads_transformed, google_ads_transformed).
### Data Validation:

- Ensures the quality of the data using Polars to validate fields and identify inconsistencies.
### Error Handling:

- Logs errors and retries tasks automatically in case of transient failures.


### Terraform Infrastructure
Terraform is used to manage the infrastructure in Google Cloud and Confluent Cloud. The following resources are managed:

- **BigQuery Datasets & Tables**: Terraform provisions the necessary BigQuery datasets and tables for both raw and transformed data.
- **Kafka Connectors**: Kafka Connect is set up to stream data from Kafka topics to BigQuery tables.


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

## How to Use

### 1. API Connectors
- **Purpose**: Fetches data from marketing APIs (e.g., Facebook Ads, Google Ads) and streams it into Kafka.
- **Files**: Located in `api_connectors/`.

### 2. ETL
- **Purpose**: Transforms data using **dbt** and handles data processing with **Polars**.
- **Files**: Located in `etl/`.

### 3. Data Validation
- **Purpose**: Validates data using **Polars** and ensures data quality based on defined expectations.
- **Files**: Located in `data_validation/`.

### 4. Kafka Connect
- **Purpose**: Automatically streams data from Kafka into Google BigQuery using **Kafka Connect BigQuery Sink**.
- **Files**: Located in `kafka_connect/`.

### 5. Error Handling
- **Purpose**: Logs and handles errors, with retry mechanisms for transient issues.
- **Files**: Located in `error_handling/`.

### 6. Docker
- **Purpose**: Containerizes different components of the platform for consistency and ease of deployment.
- **Files**: Dockerfiles are located in `docker/`.

### 7. Scripts
- **Purpose**: Automates the execution and deployment of the different components in the pipeline.
- **Files**: Located in `scripts/`.

## Environments

This platform supports multiple environments (e.g., `dev`, `prod`). Environment-specific configurations are stored in the `config/` directory.

- **dev.env**: Development environment configuration.
- **prod.env**: Production environment configuration.

