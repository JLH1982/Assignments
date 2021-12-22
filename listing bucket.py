import boto3

s3 = boto3.resource('s3', region_name = 'us-east-1')
bucketname =s3.Bucket('Bucket-Name')

for file in bucketname.objects.all():
    print(bucketname)
    print(file.key)