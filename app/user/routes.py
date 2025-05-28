from flask import Blueprint, request, jsonify, render_template
from .services import get_user, get_workspace_request_details, reset_password, update_user_profile
from app.middleware.auth_middleware import require_authorization
from werkzeug.exceptions import BadRequest
from app.utils.logger import get_logger


user_bp = Blueprint('user', __name__)
log = get_logger(__name__)

@user_bp.route('/getUser', methods=['GET'])
@require_authorization
def get_user_route():
    user_email = request.args.get('emailId')
    if not user_email:
        log.error("No EmailId on the request. Raise BadRequest")
        raise BadRequest(description="Email parameter is required.")
    user = get_user(user_email)
    return jsonify(user)

@user_bp.route('/resetPassword', methods=['PUT'])
def reset_password_route():
    request_data = request.get_json()
    reset_password(request_data)
    return jsonify({'message': 'success'})

@user_bp.route('/updateUserProfile', methods=['POST'])
def update_user_profile_route():
    request_data = request.get_json()
    update_user_profile(request_data)
    return jsonify({'message': 'success'})

@user_bp.route('/getWorkspaceRequestDetails', methods=['GET'])
def get_workspace_request_details_route():
    details = get_workspace_request_details()
    return jsonify(details)
