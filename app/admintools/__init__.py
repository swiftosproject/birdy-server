from flask import Blueprint

main = Blueprint('admintools', __name__)

from . import console
