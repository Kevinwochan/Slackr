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
    
    return {
        'u_id': 1,
        'token': '12345',
    }
