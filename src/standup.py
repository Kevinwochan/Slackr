import threading
from utils import check_token
from global_variables import get_channels
from error import InputError,AccessError
from channel import is_valid_channel, is_user_a_member, is_user_a_owner
#helper stuff
global_standups = {}

def get_standups():
    '''
    returns global_standups
    '''
    global global_standups
    return global_standups

def is_standup_active(channel_id):
    '''
    finds whether a channel has an active standup
    '''
    return channel_id in get_standups()

# Assumption: standup/start and standup/active raise AccessErrors if the user is not a member of the channel.
def check_standup_inputs(channel_id, user_id):
    '''
    checks all inputs for standup functions
    '''
    if not is_valid_channel(channel_id):
        raise InputError(description='Channel does not exist')
    if not is_user_a_member(channel_id, user_id) and not is_user_a_owner(channel_id, user_id):
        raise AccessError(description='You are not a member of this channel')

def get_message_id():
    '''
    placeholder function - used untill messages file is complete with method to generate message id's
    '''
    return -1


# functions
def standup_start(token, channel_id, length):
    '''
    starts a standup in a given channel for length amount of time
    '''
    u_id = check_token(token)
    check_standup_inputs(channel_id, u_id)
    if is_standup_active(channel_id):
        raise InputError(description='A standup is already active in this channel')
    
    glob_standups = get_standups()
    global_standups[channel_id] = {
        ({
        'u_id': u_id
        'message_id': -1,
        'timestamp': str(time.strftime("%Y%m%d%H%M")),
        'message': message
        'reacts': [{
            'u_ids':[]
            'emoji':[]  
        }]
        'is_pined':False
    })


    }
    return {
        'time_finish': 1
    }


def standup_active(token, channel_id):
    
    return {
        'is_active': False, 
        'time_finish': 1
    }


def standup_send(token, channel_id, message):
    return {}

