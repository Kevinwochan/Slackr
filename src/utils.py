'''
Contains miscellaneous helper functions. These may be seperated into different files eventually
'''

#needs pip3 install pyjwt
# Assumption: Users are logged out after a server restart (presuming they are not also unregistered)
from jwt import encode, decode
from error import AccessError
from global_variables import get_valid_tokens
SECRET = 'F FOR HAYDEN'





def generate_token(user_id):
    '''
    Returns a JWT token based on the users id and a secret message.
    '''
    curr_users = get_valid_tokens()

    token = encode({'id': user_id}, SECRET, algorithm='HS256').decode('utf-8')
    curr_users.append(token)
    return token


def check_token(token):
    '''
    Checks if the token matches a logged in user (is containted in curr_users),
    and then returns that users id. raises AccessError if token does not match logged in user.
    '''
    curr_users = get_valid_tokens()

    if not token in curr_users:
        raise AccessError(description="You do not have a valid token")
    return decode(token.encode('utf-8'), SECRET, algorithm='HS256')['id']


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
