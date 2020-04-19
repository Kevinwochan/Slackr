'''
A module for creating channels to group messages and slackr users
'''
from src.error import InputError, AccessError
from src.utils import check_token, set_reacted_messages, get_member_information
from src.global_variables import get_channels, get_users, get_slackr_owners


def is_valid_channel(channel_id):
    ''' returns true if the channel id is valid'''
    return channel_id in get_channels()


def is_user_a_member(channel_id, user_id):
    ''' returns true if the user_id is a member of the channel '''
    return user_id in get_channels()[channel_id]['members'] or is_user_a_owner(
        channel_id, user_id)


def is_user_a_owner(channel_id, user_id):
    ''' returns true if the user_id is an owner of the channel '''
    return user_id in get_channels()[channel_id]['owners']


def get_channel_owners(channel_id):
    ''' returns a list of owners of a channel '''
    return get_channels()[channel_id]['owners']


def get_channel_members(channel_id):
    ''' returns a list of channel members '''
    return get_channels()[channel_id]['members']


def is_valid_user(user_id):
    ''' returns true if user_id refers to an existing user '''
    return user_id in get_users()


def is_channel_public(channel_id):
    ''' returns true or false depending if channel is public'''
    return get_channels()[channel_id]['is_public']


def channel_invite(token, channel_id, user_id):
    '''
    invites a user (with user id u_id) to join a channel with ID channel_id.
    Once invited the user is added to the channel immediately
    An input error is thrown when the user_id/channel_id  is invalid
    Access error when the user is not a member of the channel
    '''
    host_user_id = check_token(token)
    if not is_valid_user(user_id):
        raise InputError

    if not is_valid_channel(channel_id):
        raise InputError

    if not is_user_a_member(channel_id, host_user_id):
        raise AccessError

    get_channels()[channel_id]['members'].append(user_id)
    return {}


def channel_details(token, channel_id):
    '''
        returns a dictionary of information about the channel and it's users
    '''
    user_id = check_token(token)
    if not is_valid_channel(channel_id):
        raise InputError(description="Invalid channel id")

    if not is_user_a_member(channel_id, user_id):
        raise AccessError(
            description="User does not have access to this channel")
    owner_members = []
    all_members = []
    for user_id in get_channel_owners(channel_id):
        member_info = get_member_information(user_id)
        owner_members.append(member_info)
        all_members.append(member_info)

    for user_id in get_channel_members(channel_id):
        member_info = get_member_information(user_id)
        all_members.append(member_info)
    return {
        'name': get_channels()[channel_id]['name'],
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

    if not is_user_a_member(channel_id, user_id):
        raise AccessError

    channel = get_channels()[channel_id]
    if start > len(channel['messages']):
        raise InputError

    end = start + 50
    if end > len(channel['messages']):
        end = -1
    set_reacted_messages(user_id, channel['messages'][start:start + 50])
    return {
        'messages': channel['messages'][start:start + 50],
        'start': start,
        'end': end,
    }


def channel_leave(token, channel_id):
    '''
    Removes a user from a channel
    '''
    user_id = check_token(token)

    if not is_valid_channel(channel_id):
        raise InputError

    if is_user_a_owner(channel_id, user_id):
        get_channel_owners(channel_id).remove(user_id)
    elif is_user_a_member(channel_id, user_id):
        get_channel_members(channel_id).remove(user_id)
    else:
        raise AccessError

    return {}


def channel_join(token, channel_id):
    '''
    Adds a user to a channel if they are authorised to join it
    '''
    user_id = check_token(token)

    if not is_valid_channel(channel_id):
        raise InputError(description="No channel found with that ID")

    if not is_channel_public(
            channel_id) and not user_id in get_slackr_owners():
        raise AccessError(description="This channel is private")

    get_channel_members(channel_id).append(user_id)

    return {}


def channel_addowner(token, channel_id, user_id):
    '''
        Makes a user a channel owner,
        The token must be of a channel owner or the slackr owner
    '''
    owner_id = check_token(token)

    if not is_valid_channel(channel_id):
        raise InputError

    if not is_user_a_owner(channel_id,
                           owner_id) and not owner_id in get_slackr_owners():
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

    if not is_user_a_owner(channel_id,
                           owner_id) and not owner_id in get_slackr_owners():
        raise AccessError

    if not is_user_a_owner(channel_id, user_id):
        raise InputError

    if is_user_a_owner(channel_id, user_id):
        get_channel_owners(channel_id).remove(user_id)
    get_channel_members(channel_id).append(user_id)

    return {}
