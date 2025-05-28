import os
import boto3
from dotenv import load_dotenv

load_dotenv()
AWS_REGION = os.getenv('AWS_REGION')
DYNAMODB_ENDPOINT = os.getenv('DYNAMODB_ENDPOINT')


def get_dynamodb_resource():
    if os.getenv('ENV') == 'development':
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url=os.getenv('DYNAMODB_ENDPOINT', 'http://localhost:8000'),
            region_name=AWS_REGION  # Specify your region
        )
    else:
        dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
    
    return dynamodb

dynamodb = get_dynamodb_resource()

# Define table names as constants or load from environment variables
USER_TABLE = os.getenv('USER_TABLE_NAME', 'User_Info')

def get_table(table_name):
    """Retrieve a DynamoDB table resource by name."""
    return dynamodb.Table(table_name)