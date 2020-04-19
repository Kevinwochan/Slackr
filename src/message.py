'''
Message module for sending. editing and removing messages
'''
from threading import Timer
from src.error import AccessError, InputError
from src.utils import check_token, get_current_timestamp
from src.global_variables import (get_slackr_owners, get_channels,
                                  get_num_messages, set_num_messages)
from src.channel import is_user_a_member, is_valid_channel
from src.hangman import start_hangman, guess

VALID_REACTS = [1]


def get_message_by_msg_id(message_id):
    """
    Get the corresponding message by message_id
    """
    channels_data = get_channels()
    for channel_id in channels_data:
        for message in channels_data[channel_id]['messages']:
            if message_id == message['message_id']:
                return message
    raise InputError("Message_id is not valid")


def get_channel_by_msg_id(message_id):
    """
    Get the channel dictionary by message_id
    """
    channels_data = get_channels()
    for channel_id in channels_data:
        for message in channels_data[channel_id]['messages']:
            if message_id == message['message_id']:
                return channels_data[channel_id]
    raise InputError("channel is not found")


def user_in_channel_by_msg_id(message_id, token):
    """
    Determine whether or not the user is in that channel which contains message_id
    """

    u_id = check_token(token)
    channels = get_channel_by_msg_id(message_id)
    return u_id in channels['members'] or u_id in channels['owners']


def is_channel_owner(token, channel):
    """
    Determine whether the user is the owner of the channel
    """
    u_id = check_token(token)
    if u_id in channel['owners']:
        return True
    else:
        return False


def is_message_owner(token, message_id):
    """
    Determine whether the user is the owner of the message
    """
    message = get_message_by_msg_id(message_id)
    u_id = check_token(token)
    return u_id == message['u_id']


def is_slackr_owner(token):
    """
    Determine whether the user owns the slackr
    """
    owners = get_slackr_owners()
    u_id = check_token(token)
    return u_id in owners


def create_message(user_id, message_id, time_created, message):
    '''
    returns a default message with is_pinned = False
    '''
    return {
        'u_id': user_id,
        'message_id': message_id,
        'time_created': time_created,
        'message': message,
        'reacts': [{
            'react_id': 1,
            'u_ids': [],
            'is_this_user_reacted': True
        }],
        'is_pinned': False
    }


def message_send(token, channel_id, message):
    '''
    adds message to a channels list of messages
    expects parameter types:
        token: str
        channel_id: int
        message: str
    returns dictionary
    '''
    user_id = check_token(token)

    if len(message) > 1000 or len(message) < 1:
        raise InputError(
            description=
            'Your message should be less than 1000 characters and at least 1 character'
        )
    if not is_valid_channel(channel_id):
        raise InputError
    if not is_user_a_member(channel_id, user_id):
        raise AccessError
    message_id = get_num_messages()
    glob_channels = get_channels()
    channel = glob_channels[channel_id]
    time_created = get_current_timestamp()

    if message.startswith('/hangman'):
        start_hangman(channel_id, user_id, time_created, message_id)
    elif message.startswith('/guess'):
        guess(message, channel_id, user_id, time_created, message_id)
    else:
        channel['messages'].insert(
            0, create_message(user_id, message_id, time_created, message))
    set_num_messages(message_id + 1)
    return {'message_id': message_id}


def message_react(token, message_id, react_id):
    '''
    adds a reaction to a messages list of reactions
    expects parameter types:
        token: str
        message_id: int
        react_id: int
    returns empty dictionary
    '''
    u_id = check_token(token)
    message = get_message_by_msg_id(message_id)

    if react_id not in VALID_REACTS:
        raise InputError(description='Invalid react id')
    if not user_in_channel_by_msg_id(message_id, token):
        raise InputError(description='User is not in channel')
    for react in message['reacts']:
        if react['react_id'] == react_id:
            if u_id in react['u_ids']:
                raise InputError(description='Already reacted')
            react['u_ids'].append(u_id)
    return {}


def message_unreact(token, message_id, react_id):
    '''
    removes a reaction from a messages list of reactions
    expects parameter types:
        token: str
        message_id: int
        react_id: int
    returns empty dictionary
    '''
    u_id = check_token(token)
    message = get_message_by_msg_id(message_id)

    if react_id not in VALID_REACTS:
        raise InputError(description='Invalid react id')
    if not user_in_channel_by_msg_id(message_id, token):
        raise InputError(description='User is not in channel')
    for react in message['reacts']:
        if react['react_id'] == react_id:
            if u_id in react['u_ids']:
                react['u_ids'].remove(u_id)
            else:
                raise InputError(description='You have not made this reaction')
    return {}


def message_remove(token, message_id):
    '''
    Deletes a valid message based on message id
    '''
    check_token(token)
    channel_specific = get_channel_by_msg_id(message_id)
    message_specific = get_message_by_msg_id(message_id)
    if not is_channel_owner(token, channel_specific) and not is_message_owner(
            token, message_id) and not is_slackr_owner(token):
        raise AccessError(description='Not qualified to edit')
    channel_specific['messages'].remove(message_specific)
    return {}


def message_edit(token, message_id, message):
    '''
    Changes a valid message. deletes message if the message is changed to be empty
    '''
    check_token(token)
    channel_specific = get_channel_by_msg_id(message_id)
    message_specific = get_message_by_msg_id(message_id)
    if not is_channel_owner(token, channel_specific):
        if not is_message_owner(token, message_id):
            if not is_slackr_owner(token):
                raise AccessError(description='Not qualified to edit')
    if len(message) == 0:
        channel_specific['messages'].remove(message_specific)
    else:
        message_specific['message'] = message
    return {}


def message_pin(token, message_id):
    '''
    Pins a message in a channel
    '''
    u_id = check_token(token)
    channel_specific = get_channel_by_msg_id(message_id)
    message_specific = get_message_by_msg_id(message_id)

    if u_id not in channel_specific['members'] and not is_channel_owner(
            token, channel_specific):
        raise AccessError(
            description=
            'The authorised user is not a member of the channel that the message is within'
        )

    if not is_channel_owner(token, channel_specific):
        raise InputError(description='The authorised user is not an owner')

    if message_specific['is_pinned']:
        raise InputError(
            description='Message with ID message_id is already pinned')

    if is_channel_owner(token, channel_specific
                        ) is True and message_specific['is_pinned'] is False:
        message_specific['is_pinned'] = True

    return {}


def message_unpin(token, message_id):
    '''
    Unpins a message in a channel
    '''
    u_id = check_token(token)
    message_specific = get_message_by_msg_id(message_id)
    channel_specific = get_channel_by_msg_id(message_id)
    if u_id not in channel_specific['members'] and not is_channel_owner(
            token, channel_specific):
        raise AccessError(
            description=
            'The authorised user is not a member of the channel that the message is within'
        )

    if not is_channel_owner(token, channel_specific):
        raise InputError(description='The authorised user is not an owner')
    if message_specific['is_pinned'] is False:
        raise InputError(
            description='Message with ID message_id is already unpinned')
    if is_channel_owner(token, channel_specific
                        ) is True and message_specific['is_pinned'] is True:
        message_specific['is_pinned'] = False

    return {}


def sendlater_end(channel_id, message):
    '''
    Helper function for message_sendlater, used with threading.Timer to
    add a messsage to a channels list of message after a delay.
    '''
    glob_channels = get_channels()
    glob_channels[channel_id]['messages'].insert(0, message)


def message_sendlater(token, channel_id, message, time_sent):
    '''
    sends a message at a given time_sent, where time_sent is a unix timestamp
    greater than the current time.
    '''
    u_id = check_token(token)
    if not is_valid_channel(channel_id):
        raise InputError(description="No channel exists with that ID")
    if not is_user_a_member(channel_id, u_id):
        raise AccessError(description='You are not a member of this channel')
    if len(message) > 1000 or len(message) < 1:
        raise InputError(
            description=
            'Your message should be less than 1000 characters and at least 1 character'
        )
    curr_time = get_current_timestamp()
    if curr_time >= time_sent:
        raise InputError(description="You can not send a message back in time")
    delay = time_sent - curr_time
    message_id = get_num_messages()
    set_num_messages(message_id + 1)
    message_template = create_message(u_id, message_id, time_sent, message)
    timer = Timer(delay, sendlater_end, args=[channel_id, message_template])
    timer.start()
    return {'message_id': message_id}
