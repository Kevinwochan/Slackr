'''
Contains miscellaneous functions
'''
from src.global_variables import get_users, get_channels
from src.utils import check_token, set_reacted_messages, get_user_information
from src.channel import is_user_a_member


def users_all(token):
    '''Returns a list of all users

    :param token: jwt token
    :type token: str
    :return: contains u_id, email, name_first, name_last, handle_str for each user
    :rtype: dict
    '''
    check_token(token)
    users = get_users()
    return {
        'users': [get_user_information(user_id) for user_id in users],
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
