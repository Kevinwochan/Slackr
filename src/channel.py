def invite(token, channel_id, u_id):
    return {
    }

def details(token, channel_id):
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

def messages(token, channel_id, start):
    return {
        'messages': 
        'start': 0,
        'end': 50,
    }

def leave(token, channel_id):
    return {
    }

def channel_join(token, channel_id):
    return {
    }

def addowner(token, channel_id, u_id):
    return {
    }

def removeowner(token, channel_id, u_id):
    return {
    }