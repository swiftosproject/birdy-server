from flask import Blueprint

admintools = Blueprint('admintools', __name__)

from . import console