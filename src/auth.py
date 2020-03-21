"""
this should be mostly functioning but unpolished, i will fix it tomorrow i promise
"""


from hashlib import sha256
from utils import generate_token, invalidate_token, check_registration_inputs,\
is_handle_unique, check_login_inputs, check_token
from global_variables import get_users, get_valid_tokens
from error import InputError


# Helper functions 
#TODO: combine these helper functions with the ones in utils
# and decide where to store them

def create_handle(name_first, name_last):
    '''
    creates handle by joining a users (lowercase) first and last names, cutting it off at
    20 characters, and adding numbers to the end to make it unique if nessessary.
    '''
    concat = (name_first + name_last)[:20]
    i = '0'
    handle_str = concat
    while not is_handle_unique(handle_str):
        # Loop and add numbers to the end of handle_str until unique
        handle_str = concat[:20-len(i)] + i
        i = str(int(i) + 1)

    return handle_str

def find_id(email):
    '''
    Finds the user id associated with an email
    #TODO: this function is very similar to is_email_unique - may want to combine
    '''
    glob_users = get_users()

    for u_id in glob_users:
        if email == glob_users[u_id]['email']:
            return u_id

# Auth functions
def auth_login(email, password):
    '''
    Checks the user has valid email and password.
    Finds the users u_id and generates a token for them
    TODO: tidy this code up. it real messy, im vewy tiwed
    '''
    glob_users = get_users()

    check_login_inputs(email)
    u_id = find_id(email)
    assert isinstance(u_id, int)

    password_hash = sha256(password.encode()).hexdigest()
    # checking user password
    if glob_users[u_id]['password_hash'] != password_hash:
        raise InputError(description='Incorrect password')
    #TODO: making sure this works if the user is already logged in (dont want duplicate tokens)
    token = generate_token(u_id)
    return {
        'u_id': u_id,
        'token': token,
    }


def auth_logout(token):
    '''
    logs a user out by calling invalidate_token()
    '''
    return {
        'is_success': invalidate_token(token),
    }


def auth_register(email, password, name_first, name_last):
    '''
    Registers a user by saving their information to the global variable USERS.
    Checks if their email, password and names are valid (according to the specifications). 
    assigns them a user id and generates a token for them from that id using the function
    generate_token() from utils.py. u_id's start from 0.
    '''
    # Checking inputs
    check_registration_inputs(email, password, name_first, name_last)
    glob_users = get_users()
    u_id = len(glob_users)
    password_hash = sha256(password.encode()).hexdigest()
    handle_str = create_handle(name_first, name_last)

    glob_users[u_id] = {
        'email' : email,
        'name_first': name_first,
        'name_last' : name_last,
        'handle_str': handle_str,
        'password_hash': password_hash
    }
    token = generate_token(u_id)
    return {
        'u_id': u_id,
        'token': token,
    }
