import boto3
import json

pattern = {
      "source": ["aws.ec2"],
      "detail-type": ["EC2 Instance State-change Notification"],
      "detail": {
        "state": ["shutting-down", "stopped"],
        "instance-id": ["i-xxxxxxxxxx","	i-xxxxxxxxxxx"]
      }
    }
    
client = boto3.client('events')
response = client.put_rule(
    Name = 'ec2event',
    State = "ENABLED",
    EventPattern = json.dumps(pattern)
)

response = client.put_targets(
  Rule = 'ec2event',
  Targets = [
    {
     'Id' : 'name-queue',
     'Arn' : 'arn:aws:sqs:us-east-1:XXXXXX:name-queue'
    }
  ],
)