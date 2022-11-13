import boto3
import os
import json

client = boto3.client('cognito-idp')

def handler(event, context):
    try:
        data = json.loads(event['body'])
        username = data['email']
        password = data['password']
        print(username, password)
        response = client.admin_initiate_auth(
            UserPoolId=os.getenv('COGNITO_POOL_ID'),
            ClientId=os.getenv('CLIENT_ID'),
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password,
            },
        )
        return {
            'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
              'body': json.dumps({
                    'data': response,   
                }, sort_keys=True)
        }
    except Exception as e:
        print('Error handler() => ', e)
        return e