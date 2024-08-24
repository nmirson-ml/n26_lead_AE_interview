#!/bin/bash

# Run dbt transformations
docker run --rm \
    -v $(pwd)/etl/dbt:/app/dbt \
    -e DBT_PROFILES_DIR=/app/dbt/profiles.yml \
    your-docker-repo/dbt-etl:latest \
    dbt run

echo "dbt transformations completed."
