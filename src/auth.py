"""
Auth functions. Allows users to be registered, logged in and logged out of slackr
This file uses helper functions which are located in the file auth_py
"""

from hashlib import sha256
from src.utils import generate_token, invalidate_token
from src.auth_helper import check_login_inputs, check_registration_inputs, create_handle
from src.global_variables import get_users

# Auth functions
def auth_login(email, password):
    '''
    Checks the user has valid email and password.
    Finds the users u_id and generates a token for them.
    '''
    u_id = check_login_inputs(email, password)
    token = generate_token(u_id)
    return {
        'u_id': u_id,
        'token': token,
    }


def auth_logout(token):
    '''
    logs a user out by calling invalidate_token()
    '''
    return {
        'is_success': invalidate_token(token),
    }


def auth_register(email, password, name_first, name_last):
    '''
    Registers a user by saving their information to the global variable USERS.
    Checks if their email, password and names are valid (according to the specifications).
    assigns them a user id and generates a token for them from that id using the function
    generate_token() from src.utils.py. u_id's start from 0.
    Note: USER WITH ID 0 is default Slackr owner
    '''
    # Checking inputs
    check_registration_inputs(email, password, name_first, name_last)
    glob_users = get_users()
    u_id = len(glob_users)
    password_hash = sha256(password.encode()).hexdigest()
    handle_str = create_handle(name_first, name_last)

    is_owner = False
    if u_id == 0:
        is_owner = True

    glob_users[u_id] = {
        'email' : email,
        'name_first': name_first,
        'name_last' : name_last,
        'handle_str': handle_str,
        'password_hash': password_hash,
        'is_owner': is_owner
    }
    token = generate_token(u_id)
    return {
        'u_id': u_id,
        'token': token,
    }

def auth_permission_change(token, user_id, permssion_id):
    return {}