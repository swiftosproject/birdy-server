from flask import jsonify, render_template, request, abort, current_app
from flask_login import login_required, current_user
import json
import os
import re
from . import main
from ..models import User, Package
from .. import db

# TODO Add regex for versions to prevent exploitation
allowed_package_names = re.compile(r'^[0-9A-Za-z-]{3,30}$')

def get_package_info(package_name, package_version=None):
    if package_version:
        return Package.query.filter_by(name=package_name, version=package_version).first()
    else:
        return Package.query.filter_by(name=package_name).all()

def save_package_info(package_info):
    package = Package(
        name=package_info['name'],
        description=package_info['description'],
        version=package_info['version'],
        dependencies=package_info['dependencies']
    )
    db.session.add(package)
    db.session.commit()

def publish():
    data = json.loads(request.form.get('json'))
    if allowed_package_names.match(data['name']):
        package_info_list = get_package_info(data['name'])
        if package_info_list:
            if data['name'] not in current_user.packages:
                return f'You are not the original owner of {data["name"]}.', 401
        
        new_version = data['version']
        if not package_info_list or new_version > max([pkg.version for pkg in package_info_list]):
            package_data = {
                'name': data['name'],
                'author': current_user.username,
                'description': data['description'],
                'version': new_version,
                'dependencies': data.get('dependencies', [])
            }
            file = request.files['file']
            file_path = f'{current_app.root_path}/packages/{data['name']}/{data['name']}-{new_version}.tar.xz'
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            file.save(file_path)
            package_data['file'] = file_path
            save_package_info(package_data)
            return 'Package published successfully!', 200
        else:
            return f'Version {new_version} already exists for {data["name"]}.', 400
    else:
        return 'Invalid package name', 400