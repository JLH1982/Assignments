import boto3
# #creating two instances
ec2 = boto3.resource('ec2', region_name = 'us-east-1')
instance = ec2.create_instances(
#OS image to use    
    ImageId = 'ami-04902260ca3d33422',
#instance type
    InstanceType = 't2.micro',
#number of instances
    MinCount = 2,
    MaxCount = 2,
#adding tags    
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Server-Name'
                },
            ]
        },
    ],
#associating IAM profile    
    IamInstanceProfile = {'Arn' : 'arn:aws:iam::XXXXXXXXX:instance-profile/NameRole'},
#Network Interface    
    NetworkInterfaces=[
        {
            'AssociatePublicIpAddress' : False,
            'DeviceIndex': 0
        },
    ],
)

#DELAY because printing happening before instances even reached pending
x = 999000
while x > 0:
    x = x - 1
    if x == 0:
        continue
    
#Printing the instances ID and tags to know instances ID and which instances to use
for instance in ec2.instances.filter(Filters = [{'Name': 'instance-state-name', 'Values': ['pending', 'running']}]):
    for tag in instance.tags:
        if tag['Key'] == 'Name':
            print(instance.id, tag['Value'])