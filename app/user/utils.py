import json

from app.utils.logger import get_logger

log = get_logger(__name__)

def parse_user_info(user_info):
    response_user_info = {'emailId': user_info['Email_Id']}
    if 'First_Name' in user_info:
        response_user_info['firstName'] = user_info['First_Name']
    if 'Last_Name' in user_info:
        response_user_info['lastName'] = user_info['Last_Name']
    if 'Organization_Name' in user_info:
        response_user_info['organizationName'] = user_info['Organization_Name']
    if 'Type' in user_info:
        response_user_info['type'] = user_info['Type']
    if 'Title' in user_info:
        response_user_info['title'] = user_info['Title']
    if 'Degree' in user_info:
        _degree_set = []
        for _degree in user_info['Degree']:
            _degree_set.append(_degree)
        response_user_info['degree'] = _degree_set
    if 'Additional_Degree' in user_info:
        response_user_info['additionalDegree'] = user_info['Additional_Degree']
    if 'Role' in user_info:
        response_user_info['role'] = user_info['Role']
    if 'Research_Area' in user_info:
        response_user_info['researchArea'] = user_info['Research_Area']
    if 'Accepted_ToS' in user_info:
        response_user_info['acceptedToS'] = user_info['Accepted_ToS']
    if 'Last_Accepted' in user_info:
        response_user_info['lastAccepted'] = user_info['Last_Accepted']
    if 'Last_Login_Time' in user_info:
        response_user_info['lastLogin'] = user_info['Last_Login_Time']
    if 'Last_Login_Authentication' in user_info:
        response_user_info['lastLoginAuthentication'] = user_info['Last_Login_Authentication']
    if 'Is_AHA_Member' in user_info:
        response_user_info['ahaMember'] = user_info['Is_AHA_Member']
    if 'account_locked' in user_info:
        response_user_info['accountLocked'] = user_info['account_locked']
    if 'creation_date' in user_info:
        response_user_info['creationDate'] = user_info['creation_date']
    if 'Dataset_Requests' in user_info:
        data_set_requests = json.loads(user_info['Dataset_Requests'])
        response_user_info['datasetRequestList'] = data_set_requests
    if 'unsuccessful_login_times' in user_info:
        _login_times = []
        for _time in user_info['unsuccessful_login_times']:
            _login_times.append(_time)
        response_user_info['unsuccessfulLoginTimes'] = _login_times
    return response_user_info


def format_user_info(user_info):
    log.info(user_info)
    formatted_user_info = {'Email_Id': user_info['emailId']}
    if 'firstName' in user_info and user_info['firstName']:
        formatted_user_info['First_Name'] = {'Value': user_info['firstName'], 'Action': 'PUT'}
    if 'lastName' in user_info and user_info['lastName']:
        formatted_user_info['Last_Name'] = {'Value': user_info['lastName'], 'Action': 'PUT'}
    if 'organizationName' in user_info and user_info['organizationName']:
        formatted_user_info['Organization_Name'] = {'Value': user_info['organizationName'], 'Action': 'PUT'}
    if 'type' in user_info and user_info['type']:
        formatted_user_info['Type'] = {'Value': user_info['type'], 'Action': 'PUT'}
    if 'title' in user_info and user_info['title']:
        formatted_user_info['Title'] = {'Value': user_info['title'], 'Action': 'PUT'}
    if 'degree' in user_info and user_info['degree']:
        formatted_user_info['Degree'] = {'Value': user_info['degree'], 'Action': 'PUT'}
    if 'additionalDegree' in user_info:
        formatted_user_info['Additional_Degree'] = {'Value': user_info['additionalDegree'], 'Action': 'PUT'}
    if 'role' in user_info and user_info['role']:
        formatted_user_info['Role'] = {'Value': user_info['role'], 'Action': 'PUT'}
    if 'researchArea' in user_info and user_info['researchArea']:
        formatted_user_info['Research_Area'] = {'Value': user_info['researchArea'], 'Action': 'PUT'}
    if 'acceptedToS' in user_info and user_info['acceptedToS']:
        formatted_user_info['Accepted_ToS'] = {'Value': user_info['acceptedToS'], 'Action': 'PUT'}
    if 'acceptedPTFIToS' in user_info and user_info['acceptedPTFIToS']:
        formatted_user_info['Accepted_PTFI_ToS'] = {'Value': user_info['acceptedPTFIToS'], 'Action': 'PUT'}
    if 'lastAccepted' in user_info and user_info['lastAccepted']:
        formatted_user_info['Last_Accepted'] = {'Value': user_info['lastAccepted'], 'Action': 'PUT'}
    if 'lastLogin' in user_info and user_info['lastLogin']:
        formatted_user_info['Last_Login_Time'] = {'Value': user_info['lastLogin'], 'Action': 'PUT'}
    if 'lastLoginAuthentication' in user_info and user_info['lastLoginAuthentication']:
        formatted_user_info['Last_Login_Authentication'] = {'Value': user_info['lastLoginAuthentication'],
                                                            'Action': 'PUT'}
    if 'ahaMember' in user_info and user_info['ahaMember']:
        formatted_user_info['Is_AHA_Member'] = {'Value': user_info['ahaMember'], 'Action': 'PUT'}
    if 'accountLocked' in user_info and user_info['accountLocked']:
        formatted_user_info['account_locked'] = {'Value': user_info['accountLocked'], 'Action': 'PUT'}
    if 'creationDate' in user_info and user_info['creationDate']:
        formatted_user_info['creation_date'] = {'Value': user_info['creationDate'], 'Action': 'PUT'}
    if 'datasetRequestList' in user_info and user_info['datasetRequestList'] is not None and len(user_info['datasetRequestList']) > 0:
        formatted_user_info['Dataset_Requests'] = {'Value': json.dumps(user_info['datasetRequestList']),
                                                   'Action': 'PUT'}
    if 'unsuccessfulLoginTimes' in user_info and user_info['unsuccessfulLoginTimes']:
        formatted_user_info['unsuccessful_login_times'] = {'Value': user_info['unsuccessfulLoginTimes'], 'Action': 'PUT'}
    return formatted_user_info