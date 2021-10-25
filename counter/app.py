import json
import boto3
import os

# Initialize dynamodb boto3 object
dynamodb = boto3.resource('dynamodb')
# Set dynamodb table name variable from env
# ddbTableName = os.environ['databaseName']
ddbTableName = 'cloud-resume-counter'
table = dynamodb.Table(ddbTableName)
ddbResponse = None

def lambda_handler(event, context):
    #Update item in table or add if doesn't exist
    try:
        ddbResponse = table.update_item(
            Key={
                'id': 'count'
            },
            UpdateExpression='SET visitor_count = visitor_count + :value',
            ExpressionAttributeValues={
                ':value':1
            },
            ReturnValues="UPDATED_NEW"
        )
        # Format dynamodb response into variable
        responseBody = json.dumps({'count': int(ddbResponse["Attributes"]["visitor_count"])})
    except:
        table.put_item(Item={'id':'count','visitor_count':1})
        responseBody = json.dumps({'count': 1)
 


   


    print(responseBody)
    # Create api response object
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
        },
        "body": responseBody
    }

    return apiResponse
