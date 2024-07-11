import json

def lambda_handler(event, context):
    # Hello from VS Code
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
