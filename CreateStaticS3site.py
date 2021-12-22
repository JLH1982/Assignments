import boto3
s3 = boto3.client('s3', region_name = 'us-east-1')

#Website configuration
website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'}
}
#Putting website configuration with bucket
s3.put_bucket_website(
    Bucket = 'Bucket-Name',
    WebsiteConfiguration = website_configuration
)