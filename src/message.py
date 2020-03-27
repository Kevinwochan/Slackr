'''
Message module for sending. editing and removing messages
'''
from src.error import AccessError, InputError
from src.global_variables import get_channels
from src.utils import check_token
from src.global_variables import get_slackr_owners
import time

num_messages = 0

def get_message_by_msgID(message_id):
    """
    Get the corresponding message by message_id
    """
    channels_data = get_channels()
    for channel_id in channels_data.keys():
        for message in channels_data[channel_id]['messages']:
            if message_id == message['message_id']:
                return message
    raise InputError("Message_id is not valid")

def get_channel_by_msgID(message_id):
    """
    Get the channel dictionary by message_id
    """
    channels_data = get_channels()
    for channel_id in channels_data.keys():
        for message in channels_data[channel_id]['messages']:
            if message_id == message['message_id']:
                return channels_data[channel_id]
    raise InputError("channel is not found")

def user_in_channel_by_msgID(message_id, token):
    """
    Determine whether or not the user is in that channel which contains message_id
    """
    
    u_id = check_token(token)
    channels = get_channel_by_msgID(message_id)

    if u_id in channels['members']:
        return True
    else:
        return False
    
def is_channel_owner(token, channel):

    """
    Determine whether the user is the owner of the channel
    """
    u_id = check_token(token)
    if u_id in channel['owners']:
        return True
    else:
        return False

def is_message_owner(token, message_id):

    """
    Determine whether the user is the owner of the message
    """
    message = get_message_by_msgID(message_id)
    u_id = check_token(token)
    if u_id in message['u_id']:
        return True
    else:
        return False

def is_slackr_owner(token):
    """
    Determine whether the user owns the slackr
    """
    owners = get_slackr_owners()
    u_id = check_token(token)
    if u_id in owners:
        return True
    else:
        return False


    



def message_send(token, channel_id, message):
    # Check if the token is valid and get the u_id
    u_id = check_token(token)

    # Check if the message is valid
    if len(message) > 1000:
        raise InputError(description = 'Your message should be less than 1000')
    
    global num_messages
    num_messages += 1
    glob_channels = get_channels()
    channel = glob_channels[channel_id]
    channel['messges'].append({
        'u_id': u_id,
        'message_id': num_messages,
        'timestamp': str(time.strftime("%Y%m%d%H%M")),
        'message': message,
        'reacts': [{
            'u_ids':[],
            'emoji':[]  
        }],
        'is_pinned':False
    })
    
    return {
        'message_id': num_messages
    }


def message_react(token, message_id, react_id):
    message = get_message_by_msgID(message_id)
    u_id = check_token(token)

    if react_id != 1:
        raise InputError(description = 'Invalid react id')
    if user_in_channel_by_msgID(message_id, token) is False:
        raise InputError(description = 'User is not in channel')
    if u_id in message['reacts'][0]['u_ids']:
        raise InputError(description = 'Already reacted')
    
    message['reacts'][0]['u_ids'].append(u_id)

    return {}


def message_unreact(token, message_id, react_id):
    message = get_message_by_msgID(message_id)
    channel_id = get_channel_by_msgID(message_id)
    u_id = check_token(token)

    if react_id != 1:
        raise InputError(description = 'Invalid react id')
    if user_in_channel_by_msgID(message_id, token) is False:
        raise InputError(description = 'User is not in channel')
    if u_id in message['reacts'][0]['u_ids']:
        raise InputError(description = 'Already reacted')

    message['reacts'][0]['u_ids'].remove(u_id)

    return {}

def message_remove(token, message_id):
    return {}


def message_edit(token, message_id, message):
    channel_specific = get_channel_by_msgID(message_id)
    message_specific = get_message_by_msgID(message_id)
    if is_channel_owner(token, channel_specific) == False:
        if is_message_owner(token, message_id) == False:
            if is_slackr_owner(token) == False:
                raise AccessError(description = 'Not qualified to edit')
    if len(message) == 0:
        channel_specific['messages'].remove(message_specific)
    else:
        message_specific['message'] = message
    return {}

    def message_pin(token, message_id):
        message_specific = get_message_by_msgID(message_id)
        u_id = check_token(token)
        if u_id not in message_specific['u_id']:
            raise InputError(description = 'The authorised user is not an owner')
        if message_specific['is_pined'] == True:
            raise InputError(description = 'Message with ID message_id is already pinned')
        channel_specific = get_channel_by_msgID(message_id)
        if u_id not in channel_specific['members']:
            raise AccessError(description = 'The authorised user is not a member of the channel that the message is within')

        message_specific['is_pined'] == True
        return {}

    def message_unpin(token, message_id):
        message_specific = get_message_by_msgID(message_id)
        u_id = check_token(token)
        if u_id not in message_specific['u_id']:
            raise InputError(description = 'The authorised user is not an owner')
        if message_specific['is_pined'] == False:
            raise InputError(description = 'Message with ID message_id is already unpinned')
        channel_specific = get_channel_by_msgID(message_id)
        if u_id not in channel_specific['members']:
            raise AccessError(description = 'The authorised user is not a member of the channel that the message is within')

        message_specific['is_pined'] == False
        return {}

