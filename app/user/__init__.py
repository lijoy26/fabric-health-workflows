from flask import Blueprint

user_bp = Blueprint('user', __name__)

# Import routes to register them
from . import routes
