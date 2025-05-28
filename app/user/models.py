import os
from app.utils.dynamodb import USER_TABLE, get_table
import boto3

from app.utils.logger import get_logger
from .utils import format_user_info


table = get_table(USER_TABLE)
log = get_logger(__name__)

def get_user_with_email(email):
    response = table.get_item(
        Key={
            'Email_Id': email
        }
    )
    log.info(response['Item'])
    return response['Item']


def get_all_user():
    response = table.scan()
    log.info("User_Info items count  {0}".format(len(response['Items'])))
    return response['Items']


def upsert_user(user_info):
    formatted_user_info = format_user_info(user_info)
    email = formatted_user_info['Email_Id']
    formatted_user_info.pop('Email_Id', None)
    table.update_item(
        Key={
            'Email_Id': email
        },
        AttributeUpdates=formatted_user_info
    )
    return


def get_user_count():
    _count = 0
    response = table.scan()
    if response['Items']:
        _count = len(response['Items'])
    log.info("Total user count {0}".format(_count))
    return _count


def delete_attribute(email, attributes):
    table.update_item(
        Key={
            'Email_Id': email
        },
        UpdateExpression='REMOVE '+attributes
    )