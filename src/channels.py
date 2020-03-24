'''
Functions to create and list channels
channels_list and channels_listall are written using list comprehension.
For the previous versions which used for loops, see git log.
'''

from src.utils import check_token
from src.error import InputError
from src.global_variables import get_channels


def channels_list(token):
    '''
    Loops through CHANNELS and generates a list of only the channels which
    contain the user as a member
    '''
    u_id = check_token(token)
    glob_channels = get_channels()

    return {'channels': [
        {
            'channel_id': channel_id,
            'name': glob_channels[channel_id]['name']
        } for channel_id in glob_channels
        if u_id in glob_channels[channel_id]['owners']\
        or u_id in glob_channels[channel_id]['members']
    ]}


def channels_listall(token):
    '''
    loops through CHANNELS and generates a list of all channel_ids and
    their associated names.
    '''
    check_token(token)
    glob_channels = get_channels()

    return {
        'channels': [
            {
                'channel_id': channel_id,
                'name': glob_channels[channel_id]['name']
            } for channel_id in glob_channels
        ]
    }


def channels_create(token, name, is_public):
    '''
    creates a new channel and stores it in CHANNELS
    user who creates channel is set as owner of the channel
    '''
    u_id = check_token(token)

    if len(name) > 20:
        raise InputError(description="Channel name must be less that 20 characters long")

    glob_channels = get_channels()
    channel_id = create_channel_id()

    # adding an empty channel with one owner: u_id
    glob_channels[channel_id] = {
        'name': name,
        'owners': [u_id],
        'members': [],
        'messages' : [],
        'is_public' : is_public
    }
    return {
        'channel_id': channel_id
    }
