import json

def lambda_handler(event, context):
    # TODO implement
    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        
        "messages": [{
            "type": "unstructured",
            "unstructured": {
                "id": "string",
                "text": "Application under development. Search functionality will be implemented in Assignment 2",
                "timestamp": "string"
            }
        }]
        
    }
