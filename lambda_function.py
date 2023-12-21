from datetime import datetime

import boto3
import pandas as pd
from cerberus import Validator


def lambda_handler(event, context):
    print("event", event)
    s3_resource = boto3.resource('s3')
    # Extract information from the S3 event record
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    # print(bucket_name)
    key_name = event['Records'][0]['s3']['object']['key']
    # source_folder = key_name
    # print(key_name)
    file_name = key_name.split('/')[-1]

    # Define the folder names
    source_folder = f"Source/{file_name}"
    stage_folder = f"Stage/{file_name}"
    error_folder = f"Error/{file_name}"

    result_log = {}
    schema = {
        'Name': {'type': 'string', 'required': True},
        'Age': {'type': 'integer', 'required': True},
        'Salary': {'type': 'float', 'required': True},
        'JoiningDate': {'type': 'date', 'required': True, 'coerce': lambda s: datetime.strptime(s, '%Y-%m-%d')},
        'Active': {'type': 'boolean', 'required': True},
    }

    v = Validator(schema)

    # Load the CSV file from S3
    s3_object = s3_resource.Object(bucket_name, key_name)
    csv_content = s3_object.get()['Body'].read().decode('utf-8')
    df = pd.read_csv(pd.io.common.StringIO(csv_content))

    converted_json = df.to_dict(orient='records')
    for index, row in enumerate(converted_json):
        # print(index, row)
        val = v.validate(row)
        if not val:
            # Copy to the Error folder
            result_log['Validation'] = "FAILURE"
            result_log['Reason'] = str(v.errors) + " in record number " + str(index)
            result_log['From'] = source_folder
            result_log['To'] = error_folder
            s3_resource.Object(bucket_name, error_folder).copy_from(
                CopySource={'Bucket': bucket_name, 'Key': source_folder})
            s3_object.delete()
            return result_log

    result_log['Validation'] = "Success"
    result_log['From'] = source_folder
    result_log['To'] = stage_folder
    # Copy to the Stage folder
    s3_resource.Object(bucket_name, stage_folder).copy_from(
        CopySource={'Bucket': bucket_name, 'Key': source_folder})
    # Delete the original file
    s3_object.delete()
    print("result", result_log)

    return result_log
