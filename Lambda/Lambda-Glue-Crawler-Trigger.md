## Policies

1. AWSLambdaBasicExecutionRole
2. AWSGlueServiceRole
3.S3 Permissions:
s3:GetObject: Allows the Lambda function to read objects in the S3 bucket.
s3:PutObject: Allows the Lambda function to write objects to the S3 bucket.
s3:ListBucket: Allows the Lambda function to list objects in the S3 bucket.
Resource: Replace "arn:aws:s3:::your-s3-bucket-name/*" 

## Note: Increase the timeout period to 2 minutes to stay at safer side