"""
I want to create a separate file user_data to store the information of the 
user, like their token, u_id, names, emails etc. 
Because it is easier to fetch the information like u_id by user's token

"""
from error import InputError
import user_data

## Initialize the state
user_data = {}
CHANNELS = {}
channel_id = 0


def uid_from_token(token):
    for users in user_data['users']:
        if token == users['token']:
            return users['u_id']

def get_CHANNELS():
    global CHANNELS
    return CHANNELS

def get_channel_id():
    global channel_id
    return channel_id

def channels_create(token, name, is_public):
    if len(name) < 21:
        dic_channel = {}
        dic_channel['name'] = name
        dic_channel['owners'] = ['uid_from_token(token)']
        dic_channel['members'] = ['uid_from_token(token)']
        dic_channel['message'] = []
        dic_channel['is_public'] = [is_public]
        CHANNELS = get_CHANNELS()
        channel_id = get_channel_id
        channel_id += 1
        CHANNELS['channel_id'] = channel_id
        return {"channel_id": channel_id}
    else:
        raise InputError("THE LENGTH OF NAME SHOULD BE LESS THAN 20")