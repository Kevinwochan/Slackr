from global_variables import get_channels
from utils import check_token
from channels import channels_list

def search(token, query_str):
    user_channels = channels_list(token)

    for id_channel in user_channels[channel_id]:
        messages = user_channel[id_channel]['messages']
        for id_message in messages['message_id']:
            message = messages[id_message]['message']
            if query_str in message:
                return message
