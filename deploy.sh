#!/bin/bash

echo "Running Aws Version"

docker run --rm -it amazon/aws-cli --version


echo "Running deploy script"

docker run --rm -it amazon/aws-cli ssm send-command \
    --document-name "AWS-RunRemoteScript" \
    --targets "Key=instanceids,Values=i-0881ef84752782ea2" \
    --parameters '{"sourceType":["S3"],"sourceInfo":["{\"path\":\"https://s3.amazonaws.com/springs-bucket/scripts/shell/deploy.sh\"}"],"commandLine":["deploy.sh"]}'