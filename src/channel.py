from src.channels import CHANNELS

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
    return {
        'messages': [
            {
                'message_id': 1,
                'u_id': 1,
                'message': 'Hello world',
                'time_created': 1582426789,
            }
        ],
        'start': 0,
        'end': 50,
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
