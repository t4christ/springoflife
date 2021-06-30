#!/bin/bash

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip" -o "awscliv2.zip"
unzip awscliv2.zip

echo "Installing Aws"
./aws/install


# echo "Running deploy script"

# aws ssm send-command \
#     --document-name "AWS-RunRemoteScript" \
#     --targets "Key=instanceids,Values=i-0881ef84752782ea2" \
#     --parameters '{"sourceType":["S3"],"sourceInfo":["{\"path\":\"https://s3.amazonaws.com/springs-bucket/scripts/shell/deploy.sh\"}"],"commandLine":["deploy.sh"]}'