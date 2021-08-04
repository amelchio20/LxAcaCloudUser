from __future__ import print_function

import json

print('loading function')

# Our lambda handler function!
def lambda_handler(event, context):
    for record in event['Records']:
        print(record['eventID'])
        print(record['eventName'])
        print('DynamoDB record: ' + json.dumps(record['dynamodb'], indent=2))
    print('Successfully processed %s records.' % str(len(event['Records'])))

