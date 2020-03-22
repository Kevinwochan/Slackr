'''
File containing all global variables.
These can be access by importing and using the get_ functions below.
Their structure is described in the README.md file in src.
'''
# pylint: disable=invalid-name, global-statement
global_users = {}
global_channels = {}
global_valid_tokens = []

# Functions used to access global variables
def get_users():
    '''
    Returns global_users
    '''
    global global_users
    return global_users

def get_channels():
    '''
    Returns global_channels
    '''
    global global_channels
    return global_channels

def get_valid_tokens():
    '''
    Returns global_valid_tokens
    '''
    global global_valid_tokens
    return global_valid_tokens
# pylint: enable=invalid-name, global-statement
