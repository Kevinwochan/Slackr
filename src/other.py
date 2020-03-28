'''
Contains miscellaneous functions
'''
from src.global_variables import get_users
from src.utils import check_token

def users_all(token):
    '''
    Returns a list of all users
        each user is a dictionary contains types u_id, email, name_first, name_last, handle_str
    '''
    check_token(token)
    users = get_users()
    return {
        'users': [
            {
                'u_id': user_id,
                'email': users[user_id]['email'],
                'name_first': users[user_id]['name_first'],
                'name_last': users[user_id]['name_last'],
                'handle_str': users[user_id]['handle_str']
            }
            for user_id in users
        ],
    }


def search(token, query_str):
    return {
        'messages': [{
            'message_id': 1,
            'u_id': 1,
            'message': 'Hello world',
            'time_created': 1582426789,
        }],
    }
