from src.channels import CHANNELS
from src.error import InputError, AccessError

''' 
    use CHANNELS to store your info
    if you want channnel information you can access it using it's channel id like
    channel = CHANNELS[channel_id]

    each channel is a dictionary 
    { 
        'owners': [user_id1, user_id2],
        'members': [user_id2, user_id3]
        'messages' : [message1, message2] 
    }

    each message is a dictionary with a unix timestamp
    {
        'timestamp': 1584538791 ,
        'content' : 'this is the message content',
        'reacts' : [ 
                    'user_id': user_id1,
                     'emoji' : U+1F600  # this is a s mily face in unicode
                   ]
    }

'''


def channel_invite(token, channel_id, u_id):
    return {
    }

def channel_details(token, channel_id):
    return {
        'name': 'Hayden',
        'owner_members': [
            {
                'u_id': 1,
                'name_first': 'Hayden',
                'name_last': 'Jacobs',
            }
        ],
        'all_members': [
            {
                'u_id': 1,
                'name_first': 'Hayden',
                'name_last': 'Jacobs',
            }
        ],
    }

def channel_messages(token, channel_id, start):
    # TODO: verify token
    if not channel_id in CHANNELS:
        raise InputError

    if start > len(CHANNELS[channel_id]['messages']):
        raise InputError
   
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
    return {
    }

def channel_removeowner(token, channel_id, u_id):
    return {
    }
