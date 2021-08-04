import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))    

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("S3 context.memory_limit_in_mb Print Memory Limit: ", context.memory_limit_in_mb)
        print("CloudWatch log stream name:", context.log_stream_name)
        print("CloudWatch log group name:",  context.log_group_name)
        print("Lambda Request ID:", context.aws_request_id)
        print("S3 CONTENT TYPE: " + response['ContentType'])
        print("S3 CONTENT LENGTH: ", response['ContentLength'])
        print("S3 LAST MODIFIED: ", response['LastModified'])
        return response['ContentType', bucket, key, response['ContentLength']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

