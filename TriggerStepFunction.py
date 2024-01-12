from datetime import datetime, timedelta

import boto3
from airflow import DAG
from airflow.operators.python import PythonOperator

# AWS credentials and region
aws_access_key_id = 'AKIAW4FX3MV5W2EBIFRT'
aws_secret_access_key = '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'
aws_region_name = 'ap-south-1'

# Step Functions parameters
state_machine_arn = 'arn:aws:states:ap-south-1:472831976827:stateMachine:MyStateMachine-4g941tt6n'

input_data = """
                {
                    "bucket_name": "sam-glue-practice-bucket-delete",
                    "bucket_arn": "arn:aws:s3:::sam-glue-practice-bucket-delete",
                    "key_name": "data/Source/Error-Schema.csv",
                    "file_name": "Error-Schema.csv"
                
                }
            """

def trigger_step_function(**kwargs):
    client = boto3.client('stepfunctions', aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key, region_name=aws_region_name)

    response = client.start_execution(
        stateMachineArn=state_machine_arn,
        input=input_data
    )

    execution_arn = response['executionArn']
    print(f"Step Functions execution started with ARN: {execution_arn}")


# Airflow DAG configuration
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.utcnow() + timedelta(seconds=10),
    'email_on_failure': 'sampath300500@gmail.com',
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

dag = DAG(
    'trigger_step_function_dag',
    default_args=default_args,
    schedule_interval="@once",  # Set your desired schedule interval
)

# Define the PythonOperator to trigger the Step Functions state machine
trigger_step_function_task = PythonOperator(
    task_id='trigger_step_function',
    python_callable=trigger_step_function,
    provide_context=True,
    dag=dag,
)

# Set task dependencies if needed
trigger_step_function_task


if __name__ == "__main__":
    dag.cli()
