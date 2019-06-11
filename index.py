import json
import boto3

def lambda_handler(event, context):
    # TODO implement
   dynamodb = boto3.resource('dynamodb')
   table = dynamodb.Table('Table1')
   print("Creation time" + str(table.creation_date_time))
   return {
       
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
