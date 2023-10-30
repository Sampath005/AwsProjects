import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodbTableName = 'Student'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTableName)

getMethod = 'GET'
postMethod = 'POST'
patchMethod = 'PATCH'
deleteMethod = 'DELETE'
healthPath = '/healthy'
studentPath = '/student'
studentsPath = '/students'


def lambda_handler(event, contest):
    logger.info(event)
    http_method = event['httpMethod']
    path = event['path']
    if http_method == getMethod and path == healthPath:
        response = build_response(200)
    elif http_method == getMethod and path == studentPath:
        response = get_student(event['queryStringParameters']['StudentId'])
    elif http_method == getMethod and path == studentsPath:
        response = getStudents()
    elif http_method == postMethod and path == studentPath:
        response = save_student(json.loads(event['body']))
    elif http_method == patchMethod and path == studentPath:
        request_body = json.loads(event['body'])
        response = modify_student(request_body['StudentId'], request_body['update_key'], request_body['update_value'])
    elif http_method == deleteMethod and path == studentPath:
        request_body = json.loads(event['body'])
        response = delete_student(request_body['StudentId'])
    else:
        response = build_response(404, 'Not Found')
    print("res", response)
    return response


def get_student(StudentId):
    response = table.get_item(
        Key={
            'StudentId': StudentId
        }
    )
    # print('response', response)
    if 'Item' in response:
        return build_response(200, response['Item'])
    else:
        return build_response(404, {'Message': 'StudentId: %s not found' % StudentId})


def getStudents():
    try:
        response = table.scan()
        result = response['Items']

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            result.extend(response['Items'])

        body = {
            'students': result
        }
        return build_response(200, body)
    except:
        logger.exception('Log it here for now')

def save_student(request_body):
    table.put_item(Item=request_body)
    body = {
        'Operation': 'SAVE',
        'Message': 'SUCCESS',
        'Item': request_body
    }
    return build_response(200, body)


def modify_student(StudentId, update_key, update_value):
    response = table.update_item(
        Key={
            'StudentId': StudentId
        },
        UpdateExpression='set %s = :value' % update_key,
        ExpressionAttributeValues={
            ':value': update_value
        },
        ReturnValues='UPDATED_NEW'
    )
    body = {
        'Operation': 'UPDATE',
        'Message': 'SUCCESS',
        'UpdatedAttribute': response
    }
    return build_response(200, body)


def delete_student(StudentId):
    response = table.delete_item(
        Key={
            'StudentId': StudentId
        },
        ReturnValues='ALL_OLD'
    )
    body = {
        'Operation': 'DELETE',
        'Message': 'SUCCESS',
        'deletedItem': response
    }
    return build_response(200, body)


def build_response(status_code, body=None):
    response = {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        "isBase64Encoded": False
    }
    if body is not None:
        response['body'] = json.dumps(body)
    return response
