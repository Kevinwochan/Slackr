import re
from utils import generate_token, invalidate_token
from error import InputError

'''
    user = USERS[u_id] # Example of accessing a user with a u_id
    user = {
        'u_id': 2,
        'email' : 'z5555555@unsw.edu.au',
        'name_first': 'Hayden', 
        'name_last' : 'Smith', 
         etc...
        handle_str,
        password,
        username
    }
'''
USERS = {}
def get_users():
    '''
    returns global USERS
    Use this function rather than directly accessing USERS
    '''
    global USERS # pylint: disable=global-statement
    return USERS

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
    Checks if an email is already associated with a user in USERS
    '''
    glob_users = get_users()


    for user in glob_users.values():
        if email == user['email']:
            return False
    return True

def check_registration_inputs(email, password, name_first, name_last):
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




# Auth functions
def auth_login(email, password):
    return {
        'u_id': 1,
        'token': '12345',
    }


def auth_logout(token):
    return {
        'is_success': True,
    }


def auth_register(email, password, name_first, name_last):
    '''
    Registers a user by saving their information to the global variable USERS.
    Checks if their email, password and names are valid (according to the specifications). 
    assigns them a user id and generates a token for them from that id using the function
    generate_token() from utils.py. u_id's start from 0.
    '''
    # Checking inputs
    if not is_email_valid(email):
        pass
    return {
        'u_id': 1,
        'token': '12345',
    }
