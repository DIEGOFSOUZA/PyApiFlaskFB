from flask import Blueprint

user_bp = Blueprint('cliente', __name__)

from . import cliente
