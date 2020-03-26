from utils import check_token
from global_variables import get_channels
from error import InputError

#helper stuff
global_standups = {}

def get_standups():
    global global_standups
    return global_standups

check_channel_id


# functions
def standup_start(token, channel_id, length):
    check_token(token)

    return {
        'time_finish': timestamp
    }


def standup_active(token, channel_id):
    
    return {
        'is_active': False, 
        'time_finish': timestamp
    }


def standup_send(token, channel_id, message):

    return {}

