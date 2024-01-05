## Policies

1. AWSGlueServiceRole
2. S3-Permission
s3:GetObject: Allows the Lambda function to read objects in the S3 bucket.
s3:PutObject: Allows the Lambda function to write objects to the S3 bucket.
s3:ListBucket: Allows the Lambda function to list objects in the S3 bucket.
Resource: Replace "arn:aws:s3:::your-s3-bucket-name/*"  


# Configue on S3

1. Temp dir
2. Scripts dir
3. SparkHistoryLogs dir