import boto3
import os
import json

client = boto3.client('cognito-idp')

def handler(event, context):
    try:
        data = json.loads(event['body'])
        username = data['email']
        confirmation_code = data['confirmation_code']
        print(username, confirmation_code)
        
        response = client.confirm_sign_up(
            ClientId=os.getenv('CLIENT_ID'),
            Username=username,
            ConfirmationCode=confirmation_code
        )
        
        message = 'Cannot verified User'
        
        print(response['ResponseMetadata']['HTTPStatusCode'])
        
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            message = 'User is verified'
        
        return {
            'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
              'body': json.dumps({
                    'message': message,
                }, sort_keys=True)
        }
    except Exception as e:
        print('Error handler() => ', e)
        return e