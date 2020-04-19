'''
Contains miscellaneous functions
'''
from src.global_variables import get_users, get_channels
from src.utils import check_token, set_reacted_messages
from src.channel import is_user_a_member
from src.auth_helper import is_user_disabled

def users_all(token):
    '''
    Returns a list of all users
        each user is a dictionary contains types u_id, email, name_first, name_last, handle_str
    '''
    check_token(token)
    users = get_users()
    return {
        'users': [{
            'u_id': user_id,
            'email': users[user_id]['email'],
            'name_first': users[user_id]['name_first'],
            'name_last': users[user_id]['name_last'],
            'handle_str': users[user_id]['handle_str']
        } for user_id in users if not is_user_disabled(user_id)],
    }


def search(token, query_str):
    ''' finds all messages containing the query str '''
    user_id = check_token(token)

    search_results = []
    channels = get_channels()
    for channel_id in channels:
        if not is_user_a_member(channel_id, user_id):
            continue
        for message in channels[channel_id]['messages']:
            if query_str in message['message']:
                search_results.append(message)
    sorted(search_results,
           key=lambda message: message['time_created'],
           reverse=True)
    set_reacted_messages(user_id, search_results)
    return {'messages': search_results}
