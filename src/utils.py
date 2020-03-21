'''
Contains miscellaneous helper functions. These may be seperated into different files eventually
'''

#needs pip3 install pyjwt
# Assumption: Users are logged out after a server restart (presuming they are not also unregistered)
import re
from jwt import encode, decode
from error import AccessError, InputError
from global_variables import get_valid_tokens, get_users
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

####################################################################################################
##                                   ||Auth Helper Functions||                                    ##
####################################################################################################
# These functions check that inputs are valid according to the project specifications

# helper functions
def is_email_valid(email):
    '''
    Checks if email is valid, using the method described here:
    https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/

    Returns True if email is valid, otherwise returns False.
    '''
    condition = re.search(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)

    return bool(condition)

def is_password_valid(password):
    
    '''
    '[invalid if] Password entered is less than 6 characters long'

    Returns True if password is valid, otherwise returns False
    '''
    condition = len(password) >= 6

    return bool(condition)

def is_name_valid(name):
    '''
    '[Invalid if] name is not between 1 and 50 characters inclusive in length'

    Returns True if name is valid, otherwise returns False.
    '''
    condition_1 = len(name) >= 1
    condition_2 = len(name) <= 50

    return bool(condition_1 and condition_2)

def is_email_unique(email):
    '''
    Checks if an email is already associated with a user in glob_users
    '''
    glob_users = get_users()


    for user in glob_users.values():
        if email == user['email']:
            return False
    return True

def is_handle_unique(handle_str):
    '''
    Checks if a handle is already associated with a user in glob_users
    '''
    glob_users = get_users()

    for user in glob_users.values():
        if handle_str == user['handle_str']:
            return False
    return True

def check_registration_inputs(email, password, name_first, name_last):
    '''
    Checks all inputs for registration raises the appropriate errors
    '''
    if not is_email_valid(email):
        raise InputError(description="Invalid Email")
    if not is_email_unique(email):
        raise InputError(description="An account with this email has already been registered")
    if not is_password_valid(password):
        raise InputError(description="Password not strong enough")
    if not is_name_valid(name_first):
        raise InputError(description="First name must be between 1 and 50 characters long")
    if not is_name_valid(name_last):
        raise InputError(description="Last name must be between 1 and 50 characters long")

def check_login_inputs(email, password):
    '''
    Checks all inputs for login raises the appropriate errors
    '''
    if not is_email_valid(email):
        raise InputError(description="Invalid Email")

    if is_email_unique(email):
        raise InputError(description="This email has not been registered")
