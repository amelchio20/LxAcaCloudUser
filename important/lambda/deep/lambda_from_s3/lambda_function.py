import json

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])  
    return { 
        'message' : message
    }
