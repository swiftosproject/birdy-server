from flask import current_app
import os
from ..models import User, Package
from .. import db

def start():
    while True:
        command = input()
        try:
            eval(command)
        except Exception as e:
            print(f"{e}")