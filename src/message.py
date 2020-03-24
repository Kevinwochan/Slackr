from src.channels import CHANNELS
from utils import check_token
from error import AccessError, InputError
import time

message_id = 0


def message_send(token, channel_id, message):

    # Check if the token is valid and get the u_id
    uid = check_token(token)

    # Check if the message is valid
    if len(message) > 1000:
        raise InputError("Your message should be less than 1000")
    
    global message_id
    message_id += 1
    CHANNELS[channel_id]['messges'].append({
        'message_id': message_id,
        'timestamp': str(time.strftime("%Y%m%d%H%M")),
        'message': message

        # For the reacts, I assume it is a list of dictionary beacuse it is possible
        # that more than one user could react to the message
        'reacts': [{
            'u_id':[]
            'emoji':[]  
        }]
    })

    return {
        'message_id': message_id,
    }


def message_remove(token, message_id):
    return {}


def message_edit(token, message_id, message):
    return {}
