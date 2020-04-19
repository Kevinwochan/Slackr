'''
Contains miscellaneous helper functions.
'''
# Assumption: Users are logged out after a server restart
import random
import string
from datetime import datetime
from jwt import encode, decode, InvalidTokenError
from src.auth_helper import is_user_disabled
from src.error import AccessError, InputError
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

def check_token(token):
    '''Checks if a jwt token corresponds to a currently logged in user.
    If the user's account has been deleted, invalidates that users token.

    :param token: jwt token
    :type token: str
    :raises AccessError: If the token does not correspond to a logged in user
    :raises AccessError: If the token corresponds to a deleted user
    :return: User id corresponding to the the valid token
    :rtype: int
    '''

    curr_users = get_valid_tokens()
    if not token in curr_users:
        raise AccessError(description="You do not have a valid token")
    u_id = decode(token.encode('utf-8'), SECRET, algorithms=['HS256'])['id']

    if is_user_disabled(u_id):
        invalidate_token(token)
        raise AccessError(description="Your account has been deleted")
    return u_id



def get_current_timestamp(delay=0):
    '''Returns current time + delay as a unix timestamp

    :param delay: Seconds to add to current time, defaults to 0
    :type delay: int, optional
    :return: Unix timestamp
    :rtype: int
    '''
    curr_time = datetime.now()
    return int(curr_time.timestamp() + delay)

def generate_reset_code(email, exp):
    '''Generates an email reset code that can be used to identify a user

    :param email: Valid email address
    :type email: str
    :param exp: Seconds to code expiration
    :type exp: int
    :return: jwt token
    :rtype: str
    '''
    return encode({'exp': get_current_timestamp(exp), 'email': email},
                  SECRET, algorithm='HS256').decode('utf-8')

def check_reset_code(reset_code):
    '''Validates reset_code and returns users email

    :param reset_code: jwt token to be validated
    :type reset_code: str
    :raises InputError: If reset_code is invalid or expired
    :return: email
    :rtype: str
    '''
    try:
        return decode(reset_code.encode('utf-8'), SECRET, algorithms=['HS256'])['email']
    except InvalidTokenError:
        raise InputError(description='Reset code invalid or expired') from None

def set_reacted_messages(u_id, messages):
    '''set field is_this_user_reacted to true if the u_id is in list of u_ids in the react

    :param u_id: user id
    :type u_id: int
    :param messages: dictionary data structure - contains reacts field, which contains list
    :type messages: dict
    '''
    for message in messages:
        for react in message['reacts']:
            if u_id in react['u_ids']:
                react['is_this_user_reacted'] = True
            else:
                react['is_this_user_reacted'] = False

def generate_random_string(size):
    '''
    :param size: int
    :return a random string of length size
    :rtype str
    https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
    '''
    return ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=size))
