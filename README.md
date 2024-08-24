# N26 Lead Analytics Engineer - Marketing 

## Case Study 

This repository contains the implementation of a **Self-Service Data Ingestion Platform**. The platform enables ingestion of data from multiple marketing APIs, streaming into Kafka, transformation via dbt, and loading into Google BigQuery. It also includes automated data validation using Polars and Kafka Connect for streaming ingestion.

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

