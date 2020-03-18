CHANNELS = []
''' 
    a list of channels
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

def channels_list(token):
    return {
        'channels': [
        	{
        		'channel_id': 1,
        		'name': 'My Channel',
        	}
        ],
    }

def channels_listall(token):
    return {
        'channels': [
        	{
        		'channel_id': 1,
        		'name': 'My Channel',
        	}
        ],
    }

def channels_create(token, name, is_public):
    return {
        'channel_id': 1,
    }
