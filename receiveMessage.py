import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Receive message from SQS queue
queue = sqs.receive_message(
    QueueUrl = 'https://sqs.us-east-1.amazonaws.com/XXXXXXXX/backend-queue',
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)
#Calling the first message to be printed
message = queue['Messages'][0]
#Print the message
print('Message ID:   ', message.get('MessageId'))
print('Message Body: ', message.get('Body'))