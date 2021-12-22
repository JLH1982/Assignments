import boto3
dynamo = boto3.resource('dynamodb', region_name = 'us-east-1')

#Create DB table
dynamo.create_table(
    TableName = 'Table-Name',
    KeySchema = [
        {
            'AttributeName': 'XXXX',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions = [
       { 
        'AttributeName': 'XXXX',
        'AttributeType': 'S'
       }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)