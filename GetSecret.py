import boto3 
import json 

def get_secret():

#connecting to service
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(
#Asking for which secret        
        SecretId='XXXX'
    )

    database_secrets = json.loads(response['SecretString'])
#Asking for the Value of the secret
    get_secret = (database_secrets['Value'])
    return get_secret
    
def main(secret):
   print(f"Finally, our secret is: {secret}")

our_secret = get_secret()

main(our_secret)