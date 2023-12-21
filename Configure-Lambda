## Create Iam Role

**Include Policies**

1. AWSLambdaBasicExecutionRole
2. AWSLambdaS3ExecutionRole
3. Inline policy - Lambda-s3-put

`    {
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "VisualEditor0",
			"Effect": "Allow",
			"Action": "s3:PutObject",
			"Resource": "<target-s3-bucket-Arn>"
		}
	]
}`

## Lambda Layer

    -- Create new directory 
        `mkdir python` and `cd python`
    -- Install dependency
        `pip install pandas cerberus -t .'
    -- zip the python folder
    -- upload to the layer
    -- Add the layer to the Lambda function
