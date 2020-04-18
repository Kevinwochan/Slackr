"""
Auth functions. Allows users to be registered, logged in and logged out of slackr
This file uses helper functions which are located in the file auth_py
"""
import os
from hashlib import sha256
from src.utils import generate_token, invalidate_token
from src.auth_helper import check_login_inputs, check_registration_inputs, create_handle
from src.global_variables import get_users


# Auth functions
def auth_login(email, password):
    '''Given a valid email and password, logs a user in and returns a valid corresponding token

    :param email: user's email
    :type email: str
    :param password: user's password
    :type password: str
    :return: users token and user id
    :rtype: dict
    '''
    u_id = check_login_inputs(email, password)
    token = generate_token(u_id)
    return {
        'u_id': u_id,
        'token': token,
    }


def auth_logout(token):
    '''invalidates a user's token, logging them out

    :param token: jwt token
    :type token: str
    :return: whether logging out the user was successful
    :rtype: dict
    '''
    return {
        'is_success': invalidate_token(token),
    }


def auth_register(email, password, name_first, name_last):
    '''Registers a user, saves their information, and logs them in.
    Note: The first user is set as a slackr owner by default

    :param email: user's email
    :type email: str
    :param password: user's password
    :type password: str
    :param name_first: user's first name
    :type name_first: str
    :param name_last: user's last name
    :type name_last: str
    :return: user's token and user id
    :rtype: dict
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
        'email': email,
        'name_first': name_first,
        'name_last': name_last,
        'handle_str': handle_str,
        'password_hash': password_hash,
        'is_owner': is_owner,
        'profile_img_url': '/imgurl/default.png'
    }
    token = generate_token(u_id)
    return {
        'u_id': u_id,
        'token': token,
    }
