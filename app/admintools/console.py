from flask import current_app
import os
from ..models import User, Package
from .. import db

def start():
    while True:
        command = input()
        eval(command)