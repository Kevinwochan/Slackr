'''
Provides standup functionality for slackr, so that a user can start a standup
and then all messages sent using standup_send will be buffered for a given period
of timebefore being compiled and sent as a message.
If no messages are sent during a standup, the standup is discarded and no message is
posted to the channel
'''

from threading import Timer
from src.utils import check_token, get_current_timestamp
from src.global_variables import (get_channels, get_num_messages,
                                  set_num_messages, get_users, get_standups)
from src.error import InputError, AccessError
from src.channel import is_valid_channel, is_user_a_member
from src.message import create_message


# Helper Functions
def is_standup_active(channel_id):
    '''
    finds whether a channel has an active standup
    '''
    return channel_id in get_standups()


# Assumption: standup/start and standup/active
# raise AccessErrors if the user is not a member of the channel.
def check_standup_inputs(channel_id, user_id):
    '''
    checks all inputs for standup functions
    '''
    if not is_valid_channel(channel_id):
        raise InputError(description='Channel does not exist')
    if not is_user_a_member(channel_id, user_id):
        raise AccessError(description='You are not a member of this channel')


def get_message_id():
    '''
    uses get_num_messages, set_num_messages to get a new message id,
    then increments the global message id count.
    '''
    message_id = get_num_messages()
    set_num_messages(message_id + 1)
    return message_id


def find_handle(user_id):
    '''
    returns the handle_str corresponding to a user_id
    '''
    users = get_users()
    return users[user_id]['handle_str']


def standup_end(channel_id):
    '''
    replaces placeholder message_id with the next available message id,
    uses str.join() to turn the message list into a string separated by newlines
    appends this new message to the list of messages in the given channel, and removes that
    channel id from the list of active standups
    if there no messages were sent during the standup, the standup is not added to the list of
    messages, but is still removed from the list of active standups
    '''
    glob_channels = get_channels()
    glob_standups = get_standups()
    message_lst = glob_standups[channel_id]['message']
    if len(message_lst) > 0:
        glob_standups[channel_id]['message_id'] = get_message_id()
        glob_standups[channel_id]['message'] = '\n'.join(message_lst)
        glob_channels[channel_id]['messages'].insert(
            0, glob_standups.pop(channel_id))
    else:
        glob_standups.pop(channel_id)


# Functions
def standup_start(token, channel_id, length):
    '''
    starts a standup in a given channel for length amount of time
    creates blank message with time_finish timestamp, placeholder message_id,
    and stores it in glob_standups
    '''
    u_id = check_token(token)
    check_standup_inputs(channel_id, u_id)
    if is_standup_active(channel_id):
        raise InputError(
            description='A standup is already active in this channel')

    glob_standups = get_standups()
    time_finish = get_current_timestamp(length)

    message_template = create_message(u_id, -1, time_finish, [])
    glob_standups[channel_id] = message_template

    standup = Timer(length, standup_end, args=[channel_id])
    standup.start()

    return {'time_finish': time_finish}


def standup_active(token, channel_id):
    '''
    if there is an active standup in the channel, returns unix timestamp of when standup will finish
    otherwise, returns None
    '''
    u_id = check_token(token)
    check_standup_inputs(channel_id, u_id)
    is_active = is_standup_active(channel_id)

    try:
        time_finish = get_standups()[channel_id]['time_created']
    except KeyError:
        time_finish = None
    return {'is_active': is_active, 'time_finish': time_finish}


def standup_send(token, channel_id, message):
    '''
    adds a given message to the buffer of messages to be sent when the standup ends.
    message is saved as 'handle_str: message', to be ready to be printed
    '''
    u_id = check_token(token)
    check_standup_inputs(channel_id, u_id)
    if len(message) > 1000:
        raise InputError(
            description='Message must be less than 1000 characters')
    if not is_standup_active(channel_id):
        raise InputError(
            description='There is no standup active in this channel')

    get_standups()[channel_id]['message'].append(
        f'{find_handle(u_id)}: {message}')

    return {}
