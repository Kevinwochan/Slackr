from src.channels import CHANNELS
from src.error import InputError, AccessError
from src.utils import check_token
from src.auth import SLACKR_OWNER, USERS
'''
    Helper functions for writing less code
'''


def is_valid_channel(channel_id):
    ''' returns true if the channel id is valid'''
    return channel_id in CHANNELS


def is_user_a_member(channel_id, user_id):
    ''' returns true if the user_id is a member of the channel '''
    return user_id in CHANNELS[channel_id]['members']


def is_user_a_owner(channel_id, user_id):
    ''' returns true if the user_id is an owner of the channel '''
    return user_id in CHANNELS[channel_id]['owners']


def get_channel_owners(channel_id):
    ''' returns a list of owners of a channel '''
    return CHANNELS[channel_id]['owners']


def get_channel_members(channel_id):
    ''' returns a list of channel members '''
    return CHANNELS[channel_id]['members']


'''
    Main Channel functions
'''


def channel_invite(token, channel_id, user_id):
    '''
    invites a user (with user id u_id) to join a channel with ID channel_id.
    Once invited the user is added to the channel immediately
    An input error is thrown when the user_id/channel_id  is invalid
    Access error when the user is not a member of the channel
    '''
    try:
        host_user_id = check_token(token)
    except AccessError:  #TODO:  find cleaner solution to this
        raise InputError

    if not is_valid_channel(channel_id):
        raise InputError

    if not is_user_a_member(channel_id, host_user_id):
        raise AccessError

    CHANNELS[channel_id]['members'].append(user_id)
    return {}


def channel_details(token, channel_id):
    '''
        returns a dictionary of information about the channel and it's users
    '''
    user_id = check_token(token)
    if not is_valid_channel(channel_id):
        raise InputError

    if not is_user_a_member(channel_id, user_id) and not is_user_a_owner(
            channel_id, user_id):
        raise AccessError

    owner_members = []
    all_members = []
    for user_id in get_channel_owners(channel_id):
        owner_members.append({
            'user_id': user_id,
            'name_first': USERS[user_id]['name_first'],
            'name_last': USERS[user_id]['name_last']
        })
        all_members.append({
            'user_id': user_id,
            'name_first': USERS[user_id]['name_first'],
            'name_last': USERS[user_id]['name_last']
        })

    for user_id in get_channel_members(channel_id):
        all_members.append({
            'user_id': user_id,
            'name_first': USERS[user_id]['name_first'],
            'name_last': USERS[user_id]['name_last']
        })
    return {
        'name': CHANNELS[channel_id]['name'],
        'owner_members': owner_members,
        'all_members': all_members
    }


def channel_messages(token, channel_id, start):
    '''
        returns a dictionary containing:
            messages: a list of messages starting with the most recent at index 0
            start: the index of the starting message 
            end: the index of the last message
    '''
    user_id = check_token(token)

    if not is_valid_channel(channel_id):
        raise InputError

    if not is_user_a_member(channel_id, user_id) and not is_user_a_owner(
            channel_id, user_id):
        raise AccessError

    channel = CHANNELS[channel_id]
    if start > len(channel['messages']):
        raise InputError

    end = start + 50
    if end > len(channel['messages']):
        end = -1

    return {
        'messages': channel['messages'][start:start + 50],
        'start': start,
        'end': end,
    }


def channel_leave(token, channel_id):
    return {}


def channel_join(token, channel_id):

    return {}


def channel_addowner(token, channel_id, user_id):
    ''' 
        Makes a user a channel ower, 
        The token must be of a channel owner or the slackr owner
    '''
    owner_id = check_token(token)

    if not is_valid_channel(channel_id):
        raise InputError

    if not is_user_a_owner(channel_id, owner_id) and owner_id != SLACKR_OWNER:
        raise AccessError

    if is_user_a_owner(channel_id, user_id):
        raise InputError

    if is_user_a_member(channel_id, user_id):
        get_channel_members(channel_id).remove(user_id)
    get_channel_owners(channel_id).append(user_id)

    return {}


def channel_removeowner(token, channel_id, user_id):
    '''
        Makes a channel owner a regular channel member
        the token must be one of the channel owners or the slackr owner
    '''
    owner_id = check_token(token)

    if not is_valid_channel(channel_id):
        raise InputError

    if not is_user_a_owner(channel_id, owner_id) and owner_id != SLACKR_OWNER:
        raise AccessError

    if is_user_a_owner(channel_id, user_id):
        raise InputError

    get_channel_owners(channel_id).remove(user_id)
    return {}
