from flask import jsonify, render_template, request, abort, current_app, send_from_directory
from flask_login import login_required, current_user
import json
import os
import re
from . import main
from ..models import User, Package
from .. import db
from .publish import publish

@main.route('/packages/<package_name>/<package_version>.tar.xz', methods=['GET'])
def install_route(package_name, package_version):
    package_dir = os.path.join(current_app.root_path, 'packages', package_name)
    filename = f"{package_name}-{package_version}.tar.xz"
    return send_from_directory(package_dir, filename)

@main.route('/publish', methods=['POST'])
@login_required
def publish_route():
    if not current_app.config['ALLOW_PUBLISHING']:
        return 'Publishing is disabled on this server.', 403

    if current_app.config['REQUIRE_ADMIN_TO_PUBLISH']:
        if not current_user.admin:
            return 'You must be an administrator of this server to publish!', 403
    
    return publish()

@main.route('/userinfo', methods=['GET'])
@login_required
def getownuserinfo():
    user_data = {
        "id": current_user.id,
        "username": current_user.username,
        "mail": current_user.mail
    }
    return jsonify(user_data), 200

@main.route('/userinfo', methods=['POST'])
def getuserinfo():
    data = request.get_json()
    id = data['id']
    user = User.query.filter_by(id=id).first()

    if not user:
        abort(404)

    user_data = {
        "id": user.id,
        "username": user.username,
        "mail": user.mail
    }

    return jsonify(user_data), 200
