# Serverless Data Lake with AWS Glue, Amazon S3, AWS Lambda, EventBridge, and SNS

## 1. Objective

The objective of this project is to create a serverless data lake on AWS, leveraging services such as AWS Glue, Amazon S3, AWS Lambda, Amazon EventBridge, and Amazon SNS. This architecture enables efficient data processing, transformation, and storage in a scalable and cost-effective manner.

## 2. Architecture

The architecture of the project involves the following components:

- **AWS Glue:** Used for data cataloging, ETL (Extract, Transform, Load) jobs.
- **Amazon S3:** Serves as the storage layer for the data lake, organizing data in a scalable and durable manner.
- **AWS Lambda:** Responsible for executing serverless functions triggered by events to automate various processes.
- **Amazon EventBridge:** Manages events and event rules to trigger Lambda functions based on defined conditions.
- **Amazon SNS:** Used for event notifications, allowing for timely alerts and communication.

![Architecture Diagram](./docs/architecture-diagram.png)

## 3. How This Project Works

The project workflow can be summarized as follows:

1. Upload the file to the Source Folder. It will trigger the 1st Lambda function.
2. The Lambda function executes and validate the schema. Based on the validation it moves to either Stage/ or Error/ Folder.
3. If the files land into the Error folder it will trigger an SNS notification.
4. When the files land into Stage folder it will trigger the 2nd Lambda function.
5. The Lambda function executes and start the glue crawler.
6. When glue crawler completes with success. The event rule trigger the 3rd Lambda function.
7. The Lambda function executes and start the Glue ETL job.
8. The Glue ETL job to process and transform the data. Processed data is stored back in Amazon S3 on the Transform folder. 
9. When the files land into Transform folder it will trigger the 4th Lambda function to start the Glue Crawler.
10. Once the tables are populated we could use Athena to write SQL queries on top of it.


## 4. Setup Instructions

1. Lambda
2. S3
3. Sns
4. EventBridge
5. Glue
6. Athena: Just choose the Query result location

## Test

1. Upload file with right schema on the source folder and checks the final populated tables in Glue catalog
2. Upload file with wrong schema on the source folder and check the SNS notification

## Author

Sampath. V