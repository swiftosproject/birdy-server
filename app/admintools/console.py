from os import system, name
from werkzeug.security import generate_password_hash
from .. import db, create_app
from ..models import User, Package
from flask import current_app
from pynput import keyboard
from .helpmessages import HelpMessages

app = create_app()

def interpreter():
    command = input("> ")
    execute_command(command)

def help(command):
    if command == "users.add":
        print(HelpMessages.users_add_help_message)
    elif command == "users.remove":
        print(HelpMessages.users_remove_help_message)
    elif command == "users.edit":
        print(HelpMessages.users_edit_help_message)
    elif command == "users.list":
        print(HelpMessages.users_list_help_message)
    elif command in ["users", "users.*"]:
        print(HelpMessages.user_managment_help)
    else:
        print(HelpMessages.help_message)

def execute_command(command):
    try:
        parts = command.split()
        if not parts:
            raise ValueError("No command provided")

        command = parts[0]

        if command == "users.add":
            if len(parts) != 5:
                raise ValueError("Invalid number of arguments")
            _, username, email, password, admin = parts
            add_user(username, email, password, admin)

        elif command == "users.remove":
            if len(parts) != 2:
                raise ValueError("Invalid number of arguments")
            _, username = parts
            remove_user(username)

        elif command == "users.edit":
            if len(parts) != 4:
                raise ValueError("Invalid number of arguments")
            _, username, attribute, new_value = parts
            edit_user(username, attribute, new_value)

        elif command == "users.list":
            list_users()

        elif command == "help":
            if len(parts) == 2:
                help(parts[1])
            else:
                help("all")

        elif command == "exit":
            exit(0)

        elif command == "clear":
            clear()

        else:
            print("Unknown command")

    except ValueError as ve:
        print(f"Error: {ve}")
        help(command)

    except Exception as e:
        print(f"Error: {e}")

def add_user(username, mail, password, admin):
    with app.app_context():
        if admin.lower() == "true":
            admin = True
        else:
            admin = False
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
                user.password = generate_password_hash(new_value)
            else:
                setattr(user, attribute, new_value)
            db.session.commit()
            print(f"User {username}'s {attribute} updated successfully.")
        else:
            print(f"User {username} not found.")

def list_users():
    with app.app_context():
        users = User.query.all()
        for user in users:
            print("--------------------")
            print(f"User ID: {user.id}")
            print(f"Username: {user.username}")
            print(f"Email: {user.mail}")
            print(f"Packages: {user.packages}")
            print(f"Admin: {user.admin}")
            print("--------------------")


def clear():
    if name == 'nt':
        system("cls")
    else:
        system("clear")
