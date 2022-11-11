import boto3

def handler(event, context):
    try:
        print(event, context)
    except Exception as e:
        print('Error handler() => ', e)
        return e