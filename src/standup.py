from threading import Timer
from utils import check_token, get_current_timestamp
from global_variables import get_channels
from error import InputError,AccessError
from channel import is_valid_channel, is_user_a_member, is_user_a_owner
#TODO: change get_message_id, check reacts, update with latest changes to message.py
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
    #TODO: replace this with same method used in message.py (ideally by importing a function)
    '''
    from message import message_id
    global message_id
    message_id += 1
    return message_id


def standup_end(channel_id):
    glob_channels = get_channels()
    glob_standups = get_standups()
    glob_standups[channel_id]['message_id'] = get_message_id()
    glob_channels[channel_id]['messages'].append(glob_standups.pop(channel_id))




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
    time_finish = get_current_timestamp() + length
    #creating blank message with time_finish timestamp, and storing it in glob_standups
    #has placeholder message_id
    global_standups[channel_id] = {
        'u_id': u_id,
        'message_id': -1,
        'timestamp': time_finish,
        'message': '',
        'reacts': [], # TODO: update this when reacts are finished
        'is_pined':False
    }

    standup = Timer(length, standup_end, args=[channel_id])
    standup.start()

    return {
        'time_finish': time_finish
    }


def standup_active(token, channel_id):
    u_id = check_token(token)
    check_standup_inputs(channel_id, u_id)
    is_active = is_standup_active(channel_id)

    try:
        time_finish = get_standups()[channel_id]['timestamp']
    except KeyError:
        time_finish = None

    return {
        'is_active': is_active, 
        'time_finish': time_finish
    }


def standup_send(token, channel_id, message):
    return {}

