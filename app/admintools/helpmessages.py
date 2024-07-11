class HelpMessages:
    users_add_help_message = """
    users.add
        Adds a new user to the database
        USAGE:
            users.add <username> <email> <password> <admin>
    """

    users_remove_help_message = """
    users.remove
        Removes a user from the database
        USAGE:
            users.remove <username>
    """
    
    users_edit_help_message = """
    users.edit
        Edits a users attribute
        USAGE:
            users.edit <username> <attribute> <new_value>
    """

    users_list_help_message = """
    users.list
        Lists all users and attributes
            users.list
    """
    user_managment_help = f"{users_add_help_message}{users_remove_help_message}{users_edit_help_message}{users_list_help_message}"
    help_message = f"Available commands:\n\nUSER MANAGMENT:\n{user_managment_help}"