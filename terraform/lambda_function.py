import json

def lambda_handler(event, context):
    print("Event:", json.dumps(event))
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        file_name = record['s3']['object']['key']
        
        print(f"File {file_name} uploaded to {bucket}")
    
    return {
        'statusCode': 200,
        'body': 'Success'
    }
