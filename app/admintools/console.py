from werkzeug.security import generate_password_hash
from .. import db, create_app
from ..models import User
from flask import current_app

app = create_app()

help_message = """
Available commands:
1. users.add <username> <email> <password> <admin>
2. users.remove <username>
3. users.edit <username> <attribute> <new_value>
"""

def start():
    while True:
        try:
            command = input("> ")

            if command.startswith("users.add"):
                parts = command.split(" ")
                if len(parts) != 5:
                    raise ValueError("Invalid number of arguments for users.add")
                _, username, mail, password, admin = parts
                add_user(username, mail, password, admin)

            elif command.startswith("users.remove"):
                parts = command.split(" ")
                if len(parts) != 2:
                    raise ValueError("Invalid number of arguments for users.remove")
                _, username = parts
                remove_user(username)

            elif command.startswith("users.edit"):
                parts = command.split(" ")
                if len(parts) != 4:
                    raise ValueError("Invalid number of arguments for users.edit")
                _, username, attribute, new_value = parts
                edit_user(username, attribute, new_value)

            else:
                print("Invalid command")
                print(help_message)

        except ValueError as ve:
            print(f"Error: {ve}")
            print(help_message)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print(help_message)

def add_user(username, mail, password, admin):
    with app.app_context():
        hashed_password = generate_password_hash(password)
        user = User(username=username, mail=mail, password=hashed_password, admin=admin)
        db.session.add(user)
        db.session.commit()
        print(f"User {username} added successfully.")

def remove_user(username):
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            print(f"User {username} removed successfully.")
        else:
            print(f"User {username} not found.")

def edit_user(username, attribute, new_value):
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if user:
            if attribute == "password":
                user.password = generate_password_hash(new_value, method='sha256')
            else:
                setattr(user, attribute, new_value)
            db.session.commit()
            print(f"User {username}'s {attribute} updated successfully.")
        else:
            print(f"User {username} not found.")
