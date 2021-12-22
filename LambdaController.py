import boto3
import json
    
# Create SQS client
sqs = boto3.client('sqs')

# Receive message from SQS queue
queue = sqs.receive_message(
    QueueUrl = 'https://sqs.us-east-1.amazonaws.com/XXXXXX/Name-queue',
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

#Calling the first message to be printed
message = queue['Messages'][0]
jmess = json.loads(queue['Messages'][0]['Body'])
receipt_handle = message['ReceiptHandle']
ec2 = jmess['source']

#Print the message
print('Receipt Handle:', message.get('ReceiptHandle'),'\n')
print('Source:        ', jmess['source'])
print('Instance-ID:   ', jmess['detail']['instance-id'])
print('State:         ', jmess['detail']['state'], '\n')

client = boto3.client('lambda', region_name = 'us-east-1')
MESSAGE = {'Source': jmess['source'], 'Instance-ID': jmess['detail']['instance-id'], 'State': jmess['detail']['state']}
print(MESSAGE)

if ec2 in 'aws.ec2':
    def lambda_handler(event, context):
        response = client.invoke(
            FunctionName = 'arn:aws:lambda:us-east-1:XXXXXXXX:function:ec2events-functions',
            InvocationType = 'Event',
            Payload = json.dumps(MESSAGE)
        )
    print('EC2 event detected! Invoking ec2events-function\n') 
    
else:
    print('BROKE')
    
  
#Delete received message from queue
sqs.delete_message(
    QueueUrl = 'https://sqs.us-east-1.amazonaws.com/XXXXXXXXXX/Name-queue',
    ReceiptHandle=receipt_handle
)