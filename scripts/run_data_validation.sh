#!/bin/bash

# Run the data validation process
docker run --rm \
    -v $(pwd)/data_validation:/app/data_validation \
    your-docker-repo/data-validation:latest

echo "Data validation completed."
