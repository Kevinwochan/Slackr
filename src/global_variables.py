'''
File containing all global variables.
These can be access by importing and using the get_ functions below.
Their structure is described in the README.md file in src.
'''
import os, shutil
import threading
import os
# pylint: disable=invalid-name, global-statement, broad-except

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
    '''Deletes all Slackr information and backups'''
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
    delete_files(os.path.join(os.getcwd(), 'images/cropped'))
    delete_files(os.path.join(os.getcwd(), 'images/original'))
    if os.path.exists("slackr_data.p"):
        os.remove("slackr_data.p")


def replace_data(users, channels, num_messages):
    '''Replaces global data with new data.

    :param users: contains details of registered users
    :type users: dictionary
    :param channels: contains details of existing channels and messages
    :type channels: dictionary,
    :param num_messages: next valid message id
    :type num_messages: int
    '''
    global global_users
    global global_channels
    global global_num_messages
    global_users = users
    global_channels = channels
    global_num_messages = num_messages

def delete_files(folder):
    '''
    Deletes all downloaded images
    '''
    for filename in os.listdir(folder):
        if 'default' in filename:
            continue
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

# pylint: enable=invalid-name, global-statement, broad-except
