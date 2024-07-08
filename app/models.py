from . import db
from flask_login import UserMixin

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    mail = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    packages = db.Column(db.JSON, nullable=False, default="[]")
    admin = db.Column(db.Boolean, nullable=False)

# Package model
class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    version = db.Column(db.String(20), nullable=False)
    dependencies = db.Column(db.JSON, nullable=False, default=[])

    __table_args__ = (db.UniqueConstraint(
        'name', 'version', name='_name_version_uc'),)