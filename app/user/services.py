from app.utils.logger import get_logger
from .utils import  parse_user_info
from .models import get_user_with_email
from werkzeug.exceptions import NotFound


log = get_logger(__name__)
def get_user(email):
    log.info('Attempting to retrieve profile with email=' + email)
    try:
        response = get_user_with_email(email)
        return parse_user_info(response)
    except KeyError:
        log.error("No Record found for emailId:{0}".format(email))
        raise NotFound("No record found for emailId=%s" % email)
def reset_password(data):
    # Logic to reset password
    pass

def update_user_profile(data):
    # Logic to update user profile
    pass

def get_workspace_request_details():
    # Logic to get workspace request details
    return {'details': 'example details'}