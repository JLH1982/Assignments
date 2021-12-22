import boto3
#Creating bucket
s3 = boto3.client('s3', region_name = 'us-east-1')
s3.create_bucket(Bucket = 'Bucket-Name')
bucket_name = 'Bucket-Name'
#Policy json file
policy_file = open('./s3policy.json', 'r')

#setup bucket policy
s3.put_bucket_policy(
    Bucket = 'Bucket-Name',
    Policy = policy_file.read()
)
#Uploading data to bucket
filename = 'sample-data.txt'
s3.upload_file(filename, bucket_name, 'sample-data.txt', ExtraArgs = {'ContentType': 'text/html', 'CacheControl': 'max-age=0'})
#listing bucket and contents
s3 = boto3.resource('s3')
name = s3.Bucket(bucket_name)
for file in name.objects.all():
    print(name)
    print(file.key)
