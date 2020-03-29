'''
Contains miscellaneous helper functions.
'''
# Assumption: Users are logged out after a server restart (presuming they are not also unregistered)
from datetime import datetime, timezone
from jwt import encode, decode
from src.error import AccessError
from src.global_variables import get_valid_tokens
SECRET = 'F FOR HAYDEN'


def generate_token(user_id):
    '''
    Returns a JWT token based on the users id and a secret message.
    if a user is already logged in, it does not add the token to curr_users
    '''
    curr_users = get_valid_tokens()

    token = encode({'id': user_id}, SECRET, algorithm='HS256').decode('utf-8')
    if token not in curr_users:
        curr_users.append(token)
    return token


def check_token(token):
    '''
    Checks if the token matches a logged in user (is containted in curr_users),
    and then returns that users id. raises AccessError if token does not match logged in user.
    '''
    curr_users = get_valid_tokens()
    print(token)
    if not token in curr_users:
        raise AccessError(description="You do not have a valid token")
    return decode(token.encode('utf-8'), SECRET, algorithms=['HS256'])['id']


def invalidate_token(token):
    '''
    Invalidates token by removing it from curr_users. raises AccessError if token is not in
    curr_users.
    Returns true if token is successfully invalidated.
    '''
    curr_users = get_valid_tokens()

    try:
        curr_users.remove(token)
    except ValueError:
        raise AccessError(description="Token is already invalid")
    return True


def get_current_timestamp():
    '''
    uses datetime to generate and return a unix timestamp for the current time in UTC
    TODO: check that this is the timezone we want
    '''
    curr_time = datetime.now()
    return  int(curr_time.replace(tzinfo=timezone.utc).timestamp())
