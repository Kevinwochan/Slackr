from utils import check_token
from global_variables import get_channels
from error import InputError,AccessError
from channel import is_valid_channel, is_user_a_member, is_user_a_owner
#helper stuff
global_standups = {}

def get_standups():
    global global_standups
    return global_standups
# Assumption: standup/start and standup/active raise AccessErrors if the user is not a member of the channel.
def check_standup_inputs(channel_id, user_id):
    if not is_valid_channel(channel_id):
        raise InputError(description='Channel does not exist')
    if not is_user_a_member(channel_id, u_id) and not is_user_a_owner(channel_id, u_id):
        raise AccessError(description='You are not a member of this channel')


# functions
def standup_start(token, channel_id, length):
    u_id = check_token(token)
    check_standup_inputs(channel_id,u_id)
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

