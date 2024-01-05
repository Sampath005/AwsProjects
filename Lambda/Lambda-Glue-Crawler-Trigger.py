from __future__ import print_function
import json
import boto3

print('Loading function')

glue = boto3.client(service_name='glue', region_name='<region>')

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    result = None
    try:
        result = glue.start_crawler(Name='<Crawler Name>')
    except Exception as e:
        print(e)
        print('Error starting crawler')
        raise e
    finally:
        return {
            'statusCode': 200,
            'body': json.dumps(result, default=str)
        }
