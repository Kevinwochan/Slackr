'''
File containing all global variables.
These can be access by importing and using the get_ functions below.
Their structure is described in the README.md file in src.
'''
# pylint: disable=invalid-name, global-statement
global_users = {}
global_channels = {}
global_valid_tokens = []
global_slackr_owner = 0


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

def get_slackr_owners():
    '''
    Returns a list of user_ids that are slackr owners
    '''
    global global_users
    owners = []
    for user_id in global_users:
        if global_users[user_id]['is_owner']:
            owners.append(user_id)
    return owners

def workspace_reset():
    '''
    Deletes all Slackr information as if the website was just launched
    '''
    global global_users
    global global_channels
    global global_valid_tokens
    global global_slackr_owner

    global_users.clear()
    global_channels.clear()
    global_valid_tokens.clear()
    global_slackr_owner = 0

# pylint: enable=invalid-name, global-statement
