'''
Contains miscellaneous helper functions.
'''
#needs pip3 install pyjwt
# Assumption: Users are logged out after a server restart (presuming they are not also unregistered)
from jwt import encode, decode
from src.error import AccessError, InputError
from src.global_variables import get_valid_tokens, get_channels, get_slackr_owners

SECRET = 'F FOR HAYDEN'

def generate_token(user_id):
    '''
    Returns a JWT token based on the users id and a secret message.
    if a user is already logged in, it does not add the token to curr_users
    '''
    curr_users = get_valid_tokens()

    token = encode({'id': user_id}, SECRET, algorithm='HS256').decode('utf-8')
    if token not in curr_users:
        curr_users.append(token)
    return token


def check_token(token):
    '''
    Checks if the token matches a logged in user (is containted in curr_users),
    and then returns that users id. raises AccessError if token does not match logged in user.
    '''
    curr_users = get_valid_tokens()

    if not token in curr_users:
        raise AccessError(description="You do not have a valid token")
    return decode(token.encode('utf-8'), SECRET, algorithms=['HS256'])['id']


def invalidate_token(token):
    '''
    Invalidates token by removing it from curr_users. raises AccessError if token is not in
    curr_users.
    Returns true if token is successfully invalidated.
    '''
    curr_users = get_valid_tokens()

    try:
        curr_users.remove(token)
    except ValueError:
        raise AccessError(description="Token is already invalid")
    return True
    

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


    


