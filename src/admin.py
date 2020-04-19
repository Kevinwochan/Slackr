'''
Function to change user permissions between user and admin/owner.
'''
from src.error import InputError, AccessError
from src.utils import check_token
from src.global_variables import get_slackr_owners, get_users, get_channels
from src.channel import is_valid_user, is_user_a_owner, is_user_a_member, get_channel_owners, get_channel_members
from src.channels import channels_list


def permission_change(token, u_id, permission_id):
    '''change a user's permissions on the server'''
    user_id = check_token(token)

    if not is_valid_user(u_id):
        raise InputError

    if permission_id not in (1, 2):
        raise InputError

    if not u_id in get_slackr_owners():
        raise AccessError
    # all possible errors raised.
    if permission_id == 1:
        get_users()[u_id]['is_owner'] = True
    elif permission_id == 2:
        get_users()[u_id]['is_owner'] = False

    return {}

def user_remove(token, u_id):
    '''
    Removes a user from a channel, only a slackr Owner can use this function
    '''
    host_user_id = check_token(token)

    if not is_valid_user(u_id):
        raise InputError

    if not host_user_id in get_slackr_owners():
        raise AccessError

    for channel_id in get_channels():
        if is_user_a_owner(channel_id, u_id):
            get_channel_owners(channel_id).remove(u_id)
        elif is_user_a_member(channel_id, u_id):
            get_channel_members(channel_id).remove(u_id)

    glob_users = get_users()
    glob_users[u_id]['disabled'] = True
    return {}
