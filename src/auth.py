from utils import generate_token, invalidate_token
import re
USERS = {}

# Helper functions
def is_email_valid(email):
    '''
    Checks if email is valid, using the method described here:
    https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/

    Returns True if email is valid, otherwise returns False.
    '''
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return bool(re.search(regex, email))

def is_password_valid(password):
    '''
    Checks if password is valid, according to project specifications:
    '[invalid if] Password entered is less than 6 characters long'

    Returns True if password is valid, otherwise returns False
    '''
    return bool(len(password)>=6)


def is_name_valid(name):
    '''
    Checks if a name (first or last) is valid, according to the project specifications:
    '[Invalid if] name is not between 1 and 50 characters inclusive in length'

    Returns True if name is valid, otherwise returns False.
    '''
    return bool(len(name)>=1 and len(name)<=50)


# Auth functions
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
