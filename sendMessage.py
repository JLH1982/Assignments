import boto3

sqs = boto3.client('sqs', region_name = 'us-east-1')

message = sqs.send_message(
    QueueUrl = 'https://queue.amazonaws.com/XXXXXXXXXX/Name-queue',
    MessageBody = ('Hello, here is a message from the queue!')
)
print(message.get('MessageId'))
