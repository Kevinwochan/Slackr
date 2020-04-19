'''
Function to change user permissions between user and admin/owner.
'''
from src.error import InputError, AccessError
from src.utils import check_token
from src.global_variables import get_slackr_owners, get_users, get_channels
from src.channel import is_valid_user, is_user_a_owner, is_user_a_member, get_channel_owners, get_channel_members
from src.channels import channels_list


def permission_change(token, u_id, permission_id):
    '''change a user's permissions on the server

    :param token: jwt token
    :type token: str
    :param u_id: User id corresponding to the target user
    :type u_id: int
    :param permission_id: ID of user new permissions
    :type permission_id: int
    :raises InputError: u_id does not correspond to a user
    :raises InputError: Invalid Permission ID
    :raises AccessError: User is not a slackr owner
    :return: empty dictionary
    :rtype: dict
    '''
    user_id = check_token(token)
    if not user_id in get_slackr_owners():
        raise AccessError(description='You are not permitted to perform this action')
    
    if not is_valid_user(u_id):
        raise InputError(description='User does not exist')
    if permission_id not in (1, 2):
        raise InputError(description='Invalid permission ID')
    # all possible errors raised.
    if permission_id == 1:
        get_users()[u_id]['is_owner'] = True
    elif permission_id == 2:
        get_users()[u_id]['is_owner'] = False

    return {}
    
def user_remove(token, u_id):
    '''
    Removes a user from a channel, only a slackr user can use this function
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
    return {}
