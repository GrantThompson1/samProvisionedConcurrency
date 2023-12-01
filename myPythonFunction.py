import json

def handler(event, context):
    # TODO implement
    return {
        print('hello123')
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
