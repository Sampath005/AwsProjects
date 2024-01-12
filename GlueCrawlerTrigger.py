from __future__ import print_function
import json
import boto3

print('Loading function')

glue = boto3.client(service_name='glue', region_name='ap-south-1')

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    result = None
    try:
        result = glue.start_crawler(Name='StageSchemaCrawler')
    except Exception as e:
        print(e)
        print('Error starting crawler')
        raise e
    result={}
    result['crawler_name']='StageSchemaCrawler'
    return(result)
