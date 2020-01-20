#!/bin/bash

# Run in root of folder
# requires aws cli v2

# TODO: maybe quiet this up?
aws2 dynamodb batch-write-item --table-name dog_table_test_melatonin_2357111317 --request-items file://db/dog_metadata.json
aws2 dynamodb batch-write-item --table-name dog_table_test_melatonin_2357111317 --request-items file://db/test_user_metadata.json