import boto3

sqs = boto3.client('sqs', region_name = 'us-east-1')
#creating Queue with name and delay
queue = sqs.create_queue(
        QueueName = 'name-queue',
        Attributes = {
            "DelaySeconds": '10'
        }
    ),
#Printing just the URl of created Queue
queue = sqs.get_queue_url(QueueName = 'namel-queue')
print(queue['QueueUrl'])