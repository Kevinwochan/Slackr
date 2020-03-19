from src.channels import CHANNELS
from src.error import InputError, AccessError

'''
    Helper functions for writing less code
'''
def is_valid_channel(channel_id)
    ''' returns true if the channel id is valid'''
    return CHANNELS.get(channel_id, -1) != -1

def is_user_a_member(channel_id, u_id):
    ''' returns true if the u_id is a member of the channel '''
    for user in CHANNELS[channel_id]['all_members']
        if user['u_id'] == u_id:
            return True
    return False

def is_user_a_owner(channel_id, u_id):
    ''' returns true if the u_id is an owner of the channel '''
    for user in CHANNELS[channel_id]['members']
        if user['u_id'] == u_id and user['is_owner']:
            return True
    return False

def get_channel_owners(channel_id);
    ''' returns a new list of owners of a channel '''
    return [for user in CHANNELS[channel_id]['members'] if user['is_owner']]

def get_channel_users(channel_id):
    ''' returns a list of channel members '''
    return  CHANNELS[channel_id]['members']

'''
    Main Channel functions
'''
def channel_invite(token, channel_id, u_id):
    return {
    }

def channel_details(token, channel_id):
    if not is_valid_channel(channel_id):
        raise InputError
    # TODO: verify token
    return {
        'name': CHANNELS[channel_id]['name']
        'owner_members': get_channel_owners(channel_id)
        'all_members': get_channel_users(channel_id)
    }

def channel_messages(token, channel_id, start):
    if not is_valid_channel(channel_id)
        raise InputError

    if start > len(CHANNELS[channel_id]['messages']):
        raise InputError
   
    # TODO: verify token
    channel = CHANNELS[channel_id]
    end = start+50
    if end > len(channel['messages']):
        end = -1

    return {
        'messages': channel['messages'][start:start+50],
        'start': start,
        'end': end,
    }

def channel_leave(token, channel_id):
    return {
    }

def channel_join(token, channel_id):
    return {
    }

def channel_addowner(token, channel_id, u_id):
    ''' 
        makes a user a channel ower, 
        if the user is not already a member the user is added to the channel first
    '''
    #TODO: authennticate token
    if not is_valid_channel(channel_id):
        raise InputError

    if u_id in get_channel_owners(channel_id):
        raise InputError

    if not u_id in get_channel_users(channel_id):
        channel_join(token, channel_id, u_id)

    for user in get_channel_users(channel_id):
        if user['u_id'] == u_id:
            user['is_owner'] = True

    return {
    }

def channel_removeowner(token, channel_id, u_id):
    return {
    }
