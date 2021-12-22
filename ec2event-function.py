import boto3
import json

def lambda_handler(event, context):
    #receiving message from controller function
    client = boto3.client('lambda', region_name = 'us-east-1')
    #Print the message
    print(event)

    #Sending SNS message to email. 

    client = boto3.client('sns', region_name = 'us-east-1')
    response = client.publish(
        TopicArn = 'arn:aws:sns:us-east-1:XXXXXXXXX:ops-notify',
        Subject = 'EC2 Critical Event',
        Message = json.dumps(event)
    )
