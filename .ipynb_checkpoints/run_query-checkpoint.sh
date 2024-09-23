#!/bin/bash

# Check if the project name is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <GCP_PROJECT_NAME>"
  exit 1
fi

# Set the GCP project name
GCP_PROJECT=$1

# Run the Python script with the project name as an argument
python3 bigquery_input.py $GCP_PROJECT
