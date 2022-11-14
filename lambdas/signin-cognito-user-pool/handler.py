import boto3
import os
import json

client = boto3.client('cognito-idp')
identity = boto3.client('cognito-identity')

logins = 'cognito-idp.{}.amazonaws.com/{}'.format(os.getenv('AWS_REGION'), os.getenv('COGNITO_POOL_ID'))

def handler(event, context):
    try:
        data = json.loads(event['body'])
        username = data['email']
        password = data['password']

        response = client.admin_initiate_auth(
            UserPoolId=os.getenv('COGNITO_POOL_ID'),
            ClientId=os.getenv('CLIENT_ID'),
            AuthFlow='ADMIN_USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password,
            },
        )
        
        print(response)
        
        id_token = response['AuthenticationResult']['IdToken']
        
        identityId = identity.get_id(
            IdentityPoolId=os.getenv('IDENTITY_POOL_ID'),
            Logins={
                logins: id_token
            }
        )['IdentityId']
        
        aws_cred = identity.get_credentials_for_identity(
            IdentityId=identityId,
            Logins={
                logins: id_token
            }
        )['Credentials']
        
        print(aws_cred)
        
        return {
            'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
              'body': json.dumps({
                    'token': id_token,
                    'accessKeyId': aws_cred['AccessKeyId'],
                    'secretKey': aws_cred['SecretKey']
                }, sort_keys=True)
        }
    except Exception as e:
        print('Error handler() => ', e)
        return e