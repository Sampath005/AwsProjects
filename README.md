# Schema Validation Using Amazon S3 and AWS Lambda

## Overview

This project is designed to perform schema validation on CSV files uploaded to an S3 bucket using AWS Lambda. The validation process checks whether the uploaded CSV file adheres to a specified schema. If the validation is successful, the file is moved to a "Stage" folder; otherwise, it is moved to an "Error" folder.

## Architecture

![Architeture](https://github.com/Sampath005/AwsProjects/assets/97429122/0208500f-968a-44a9-807b-d585a616b4cb)

## Components

1. **AWS Lambda Function:** Responsible for executing the schema validation and moving files to appropriate folders.

2. **Amazon S3 Bucket:** Used to store and manage the CSV files uploaded by users.

## Setup Instructions

#### [1.Lambda Function Configure](https://github.com/Sampath005/AwsProjects/blob/Project-3/Configure-Lambda.md) 
#### [2.S3 Bucket Configuration](https://github.com/Sampath005/AwsProjects/blob/Project-3/S3%20Bucket%20Configuration.md)

## Schema Validation

1. **Define Schema:**
   - Modify the schema validation logic in your Lambda function according to the specific requirements of your CSV files.
     
## Monitoring and Logging

- Set up CloudWatch Logs to monitor the execution logs of your Lambda function.

## Author
   - Sampath. V
