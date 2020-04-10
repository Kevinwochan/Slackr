'''
File containing all global variables.
These can be access by importing and using the get_ functions below.
Their structure is described in the README.md file in src.
'''
import threading
# pylint: disable=invalid-name, global-statement

global_users = {}
global_channels = {}
global_valid_tokens = []
global_num_messages = 0
global_standups = {}


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


def get_num_messages():
    global global_num_messages
    return global_num_messages


def set_num_messages(new_num_messages):
    global global_num_messages
    global_num_messages = new_num_messages


def get_standups():
    '''
    returns global_standups
    '''
    global global_standups
    return global_standups

def cancel_all_timers():
    '''
    Cancels threads that of type threading.timer
    '''
    for thread in threading.enumerate():
        if isinstance(thread, threading.Timer):
            thread.cancel()

def workspace_reset():
    '''
    Deletes all Slackr information as if the website was just launched
    '''
    global global_users
    global global_channels
    global global_valid_tokens
    global global_num_messages

    global_users.clear()
    global_channels.clear()
    global_valid_tokens.clear()
    cancel_all_timers()
    global_standups.clear()
    global_num_messages = 0

def replace_data(users, channels, num_messages):
    '''Replaces global data with new data

    :param
        users: contains details of registered users
        channels: contains details of existing channels and messages,
        num_messages: next valid message id.
    :type
        users: dictionary,
        channels: dictionary,
        num_messages: int.
    :rtype N/A
    :return N/A
    '''
    global global_users
    global global_channels
    global global_num_messages
    global_users = users
    global_channels = channels
    global_num_messages = num_messages

# pylint: enable=invalid-name, global-statement
