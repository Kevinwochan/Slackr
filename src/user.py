'''
Allows users to edit and set their profile information
'''
import re
from src.utils import check_token
from src.error import InputError
from src.global_variables import get_users



def is_valid_email(email):
    ''' code from https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/'''
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not re.search(regex, email):
        return False
    for user in get_users():
        if user['email'] == email:
            return False
    return True


def user_profile(token, user_id):
    '''
    fetches a user profile, any valid user is able to do this
    '''
    check_token(token)
    if not user_id in get_users():
        raise InputError

    user = get_users()[user_id]
    return {
        'user': user_id,
        'email': user['email'],
        'name_first': user['name_first'],
        'name_list': user['name_last'],
        'handle_str': user['handle_str']
    }


def user_profile_setname(token, name_first, name_last):
    '''
    Sets the name of the profile using given strings
    name_first and name_last have size limits
    and only the user owner can change this
    '''
    user_id = check_token(token)
    if not user_id in get_users():
        raise InputError

    if len(name_first) < 1 or len(name_first) > 50:
        raise InputError
    if len(name_last) < 1 or len(name_last) > 50:
        raise InputError

    user = get_users()[user_id]
    user['name_first'] = name_first
    user['name_list'] = name_last

    return {}


def user_profile_setemail(token, email):
    '''
    Update the authorised user's email address
    '''
    user_id = check_token(token)
    if not user_id in get_users():
        raise InputError

    user = get_users()[user_id]
    user['email'] = email
    return {}


def user_profile_sethandle(token, handle_str):
    '''
    Update the authorised user's handle (i.e. display name)
    handle has a size limit
    '''
    user_id = check_token(token)
    if not user_id in get_users():
        raise InputError
    if len(handle_str) < 1 or len(handle_str) > 50:
        raise InputError

    user = get_users()[user_id]
    user['handle_str'] = handle_str
    return {}
