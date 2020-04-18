'''
Function to change user permissions between user and admin/owner.
'''
from src.error import InputError, AccessError
from src.utils import check_token
from src.global_variables import get_slackr_owners, get_users
from src.channel import is_valid_user


def permission_change(token, u_id, permission_id):
    '''change a user's permissions on the server'''
    user_id = check_token(token)

    if not is_valid_user(u_id):
        raise InputError

    if permission_id not in (1, 2):
        raise InputError

    if not user_id in get_slackr_owners():
        raise AccessError
    # all possible errors raised.
    if permission_id == 1:
        get_users()[u_id]['is_owner'] = True
    elif permission_id == 2:
        get_users()[u_id]['is_owner'] = False

    return {}
