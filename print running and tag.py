import boto3
ec2 = boto3.resource('ec2')

#instance = ec2.instances.filter(Filters = [{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in ec2.instances.filter(Filters = [{'Name': 'instance-state-name', 'Values': ['running', 'pending']}]):
    for tag in instance.tags:
        if tag['Key'] == 'Name':
            print(instance.id, tag['Value'])