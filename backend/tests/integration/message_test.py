'''
tests slackr message functionality
'''

#!/usr/bin/python3.7
from time import sleep
import pytest
from src.utils import get_current_timestamp
from src.error import AccessError, InputError
from src.channel import channel_invite, channel_messages
from src.auth import auth_register
from src.message import (message_edit, message_remove, message_send,
                         message_pin, message_unpin, message_react,
                         message_unreact, get_message_by_msg_id,
                         message_sendlater)


# Sending
def test_sending_long_message(new_channel_and_user):
    """ Test sending a message that is just below the size limit
        uses channel_messages to verify that the message has been recorded
        assuming message ids start with 0, the first message ever will
        have an id of 0
    """
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'a' * 1000)
    assert isinstance(message, dict)
    assert 'message_id' in message
    assert isinstance(message['message_id'], int)
    assert message['message_id'] == 0

def test_sending_to_invalid_channel(new_channel_and_user):
    '''
    Tests that an error is thrown when messsage_send is given an invalid channel id
    '''
    with pytest.raises(InputError):
        assert message_send(new_channel_and_user['token'],
                            -1, 'a')
def test_sending_too_long_message(new_channel_and_user):
    """Tests that an error is thrown when a message over the size limit is sent"""
    with pytest.raises(InputError):
        assert message_send(new_channel_and_user['token'],
                            new_channel_and_user['channel_id'], 'a' * 1001)


def test_sending_message_without_channel_access(new_channel_and_user):
    """Tests that a user sending a message to a channel
        they do not have access to, throws an error
    """
    unauthorized_user = auth_register("z6666666@unsw.edu.au", "password",
                                      "first_name1", "last_name1")

    with pytest.raises(AccessError):
        assert message_send(unauthorized_user['token'],
                            new_channel_and_user['channel_id'], 'a')


def test_sending_many_messages(new_channel_and_user):
    """Sends 49 messages into a channel and checks the id has been incremented"""
    for message_id in range(49):
        message = message_send(new_channel_and_user['token'],
                               new_channel_and_user['channel_id'],
                               str(message_id))

        assert isinstance(message, dict)
        assert 'message_id' in message
        assert isinstance(message['message_id'], int)
        assert message['message_id'] == message_id


def test_sending_empty_message(new_channel_and_user):
    """ Tests that an empty message will throw and error"""
    with pytest.raises(InputError):
        message_send(new_channel_and_user['token'],
                     new_channel_and_user['channel_id'], '')


def test_sending_with_invalid_token(new_channel_and_user):
    """ Tests that an access error is thrown when an an invalid token is used """
    with pytest.raises(AccessError):
        message_send('invalid token', new_channel_and_user['channel_id'], 'a')


# Removing
def test_removing_invalid_messages(new_channel_and_user):
    """ Tests that removing a message with an invalid message id throws an input error"""
    with pytest.raises(InputError):
        assert message_remove(new_channel_and_user['token'], 0)
    with pytest.raises(InputError):
        assert message_remove(new_channel_and_user['token'], -1)
    with pytest.raises(InputError):
        assert message_remove(new_channel_and_user['token'], 50)


def test_removing_a_message_unauthorized_user(new_channel_and_user):
    """Tests that an error is thrown when the user is not authorised to remove the message
        A user is not authorised if they are not authorised to see the channel
    """
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'a')
    unauthorized_user = auth_register("z6666666@unsw.edu.au", "password",
                                      "first_name1", "last_name1")

    with pytest.raises(AccessError):
        assert message_remove(unauthorized_user['token'],
                              message['message_id'])


def test_removing_a_message_neither_author_nor_owner(new_channel_and_user):
    """Tests that an error is thrown when the user is not authorised to remove the message
        A user is not authorised if they are
             i not the author of the message and
            ii: not an admin/owner of the chat
    """
    not_author = auth_register("z6666666@unsw.edu.au", "password",
                               "first_name1", "last_name1")
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'a')
    channel_invite(new_channel_and_user['token'],
                   new_channel_and_user['channel_id'], not_author['u_id'])

    with pytest.raises(AccessError):
        assert message_remove(not_author['token'], message['message_id'])


def test_removing_authored_message(new_channel_and_user):
    """ Tests the successful removal of a message from a user that sent it"""
    author = auth_register("z6666666@unsw.edu.au", "password", "first_name1",
                           "last_name1")
    channel_invite(new_channel_and_user['token'],
                   new_channel_and_user['channel_id'], author['u_id'])
    message = message_send(author['token'], new_channel_and_user['channel_id'],
                           'a')
    message_remove(author['token'], message['message_id'])


def test_removing_message_as_owner(new_channel_and_user):
    ''' tests the sucessful removal of a message by the channel owner'''
    author = auth_register("z6666666@unsw.edu.au", "password", "first_name1",
                           "last_name1")
    channel_invite(new_channel_and_user['token'],
                   new_channel_and_user['channel_id'], author['u_id'])
    message = message_send(author['token'], new_channel_and_user['channel_id'],
                           'a')
    message_remove(new_channel_and_user['token'], message['message_id'])


def test_removing_with_invalid_token(new_channel_and_user):
    """ Tests that an access error is thrown when an an invalid token is used """
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'a')
    with pytest.raises(AccessError):
        message_remove('invalid token', message['message_id'])


# Editing
def test_editing_invalid_messages(new_channel_and_user):
    """ Tests that editing a message with an invalid message id throws an input error"""
    with pytest.raises(InputError):
        assert message_edit(new_channel_and_user['token'], 0,
                            'new message to replace existing message')
    with pytest.raises(InputError):
        assert message_edit(new_channel_and_user['token'], -1,
                            'new message to replace existing message')
    with pytest.raises(InputError):
        assert message_edit(new_channel_and_user['token'], 50,
                            'new message to replace existing message')


def test_editing_a_message_unauthorized_user(new_channel_and_user):
    """Tests that an error is thrown when the user is not authorised to edit the message
        A user is not authorised if they are not authorised to see the channel
    """
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'a')
    unauthorized_user = auth_register("z6666666@unsw.edu.au", "password",
                                      "first_name1", "last_name1")

    with pytest.raises(AccessError):
        assert message_edit(unauthorized_user['token'], message['message_id'],
                            'new message to replace existing message')


def test_editing_a_message_neither_author_nor_owner(new_channel_and_user):
    """Tests that an error is thrown when the user is not authorised to edit the message
        A user is not authorised if they are
             i not the author of the message and
            ii: not an admin/owner of the chat
    """
    not_author = auth_register("z6666666@unsw.edu.au", "password",
                               "first_name1", "last_name1")
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'a')
    channel_invite(new_channel_and_user['token'],
                   new_channel_and_user['channel_id'], not_author['u_id'])

    with pytest.raises(AccessError):
        assert message_edit(not_author['token'], message['message_id'],
                            'new message to replace existing message')


def test_editing_authored_message(new_channel_and_user):
    """ Tests the successful edit of a message from a user that sent it"""
    author = auth_register("z6666666@unsw.edu.au", "password", "first_name1",
                           "last_name1")
    channel_invite(new_channel_and_user['token'],
                   new_channel_and_user['channel_id'], author['u_id'])
    message = message_send(author['token'], new_channel_and_user['channel_id'],
                           'a')
    message_edit(author['token'], message['message_id'],
                 'new message to replace existing message')


def test_editing_authored_message_with_empty_message(new_channel_and_user):
    """ Tests replacing a message with an empty message removes the messages"""
    author = auth_register("z6666666@unsw.edu.au", "password", "first_name1",
                           "last_name1")
    channel_invite(new_channel_and_user['token'],
                   new_channel_and_user['channel_id'], author['u_id'])
    message = message_send(author['token'], new_channel_and_user['channel_id'],
                           'a')
    message_edit(author['token'], message['message_id'], '')
    with pytest.raises(InputError):
        message_edit(author['token'], message['message_id'], '')


def test_editing_with_invalid_token(new_channel_and_user):
    """ Tests that an access error is thrown when an an invalid token is used """
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'a')
    with pytest.raises(AccessError):
        message_edit('invalid token', message['message_id'],
                     'new message to replace existing message')


def test_message_react_normal(new_channel_and_user):
    """ Test that an legal user react a message"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    message_react(new_channel_and_user['token'], message['message_id'], 1)
    message_specific = get_message_by_msg_id(message['message_id'])

    assert message_specific['reacts'] == [{
        'react_id':
        1,
        'u_ids': [new_channel_and_user['u_id']],
        'is_this_user_reacted':
        True
    }]


def test_message_already_reacted(new_channel_and_user):
    """ Test that if a user react to a message that has already been reacted"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    message_react(new_channel_and_user['token'], message['message_id'], 1)
    with pytest.raises(InputError):
        message_react(new_channel_and_user['token'], message['message_id'], 1)


def test_message_invalid_react_id(new_channel_and_user):
    """ Test that if a user try to react a message with an invalid react_id"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    with pytest.raises(InputError):
        message_react(new_channel_and_user['token'], message['message_id'], 0)


def test_message_react_user_not_in_channel(new_channel_and_user,
                                           new_channel_and_user_2):
    """ Test that if a user try to react a message when he/she is not in that channel"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    with pytest.raises(InputError):
        message_react(new_channel_and_user_2['token'], message['message_id'],
                      1)


def test_message_unreact_norm(new_channel_and_user):
    """ Test that a legal user unreat a peice of mesage when there is only one piece of message"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    message_react(new_channel_and_user['token'], message['message_id'], 1)
    message_unreact(new_channel_and_user['token'], message['message_id'], 1)
    message_specific = get_message_by_msg_id(message['message_id'])

    assert message_specific['reacts'] == [{'is_this_user_reacted': True, 'react_id': 1, 'u_ids': []}]


def test_message_unreact_invalid_react_id(new_channel_and_user):
    """ Test that a legal user unreact a message but with invalid react_id"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    message_react(new_channel_and_user['token'], message['message_id'], 1)
    with pytest.raises(InputError):
        message_unreact(new_channel_and_user['token'], message['message_id'],
                        0)


def test_message_unreact_user_not_in_channel(new_channel_and_user,
                                             new_channel_and_user_2):
    """ Test that if a user try to unreact a message when he/she is not in that channel"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    message_react(new_channel_and_user['token'], message['message_id'], 1)
    with pytest.raises(InputError):
        message_unreact(new_channel_and_user_2['token'], message['message_id'],
                        1)


def test_message_unreact_no_reacts(new_channel_and_user):
    """ Test that if a user try to unreact a message when there is no reacts in message"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adc')
    with pytest.raises(InputError):
        message_unreact(new_channel_and_user['token'], message['message_id'],
                        1)


def test_message_unreact_ueser_not_react(new_channel_and_user,
                                         new_channel_and_user_2):
    """ Test that if a uer try to unreact a message which is not his/her reaction"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    message_react(new_channel_and_user['token'], message['message_id'], 1)

    channel_invite(new_channel_and_user['token'],
                   new_channel_and_user['channel_id'],
                   new_channel_and_user_2['u_id'])

    with pytest.raises(InputError):
        message_unreact(new_channel_and_user_2['token'], message['message_id'],
                        1)


def test_message_pin_norm(new_channel_and_user):
    """ Test that if a legal use pin a message"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    message_pin(new_channel_and_user['token'], message['message_id'])
    message_specific = get_message_by_msg_id(message['message_id'])

    assert message_specific['is_pinned']


def test_message_pin_invalid_msg_id(new_channel_and_user):
    """ Test that if the message is invalid"""
    with pytest.raises(InputError):
        message_pin(new_channel_and_user['token'], -1)


def test_message_pin_not_member(new_channel_and_user, new_channel_and_user_2):
    """ Test that try to pin a message by a user who is not one of members"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    with pytest.raises(AccessError):
        message_pin(new_channel_and_user_2['token'], message['message_id'])


def test_message_already_pinned(new_channel_and_user):
    """ Test that try to pin a message that has already been pinned"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    message_pin(new_channel_and_user['token'], message['message_id'])

    with pytest.raises(InputError):
        message_pin(new_channel_and_user['token'], message['message_id'])


def test_message_pin_not_owner(new_channel_and_user, new_channel_and_user_2):
    """ Test that try to pin a message but not the owner"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    channel_invite(new_channel_and_user['token'],
                   new_channel_and_user['channel_id'],
                   new_channel_and_user_2['u_id'])

    with pytest.raises(InputError):
        message_pin(new_channel_and_user_2['token'], message['message_id'])


def test_message_unpin_norm(new_channel_and_user):
    """ Test that if a legal use unpin a message"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    message_specific = get_message_by_msg_id(message['message_id'])

    assert not message_specific['is_pinned']


def test_message_unpin_invalid_msg_id(new_channel_and_user):
    """ Test that if the message is invalid"""
    with pytest.raises(InputError):
        message_unpin(new_channel_and_user['token'], -1)


def test_message_unpin_not_member(new_channel_and_user,
                                  new_channel_and_user_2):
    """ Test that try to unpin a message by a user who is not one of members"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    with pytest.raises(AccessError):
        message_unpin(new_channel_and_user_2['token'], message['message_id'])


def test_message_already_unpinned(new_channel_and_user):
    """ Test that try to unpin a message that has already been pinned"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')

    with pytest.raises(InputError):
        message_unpin(new_channel_and_user['token'], message['message_id'])


def test_message_unpin_not_owner(new_channel_and_user, new_channel_and_user_2):
    """ Test that try to unpin a message but not the owner"""
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'adcd')
    channel_invite(new_channel_and_user['token'],
                   new_channel_and_user['channel_id'],
                   new_channel_and_user_2['u_id'])
    message_pin(new_channel_and_user['token'], message['message_id'])

    with pytest.raises(InputError):
        message_unpin(new_channel_and_user_2['token'], message['message_id'])

def test_sendlater_invalid_token(inv_token, new_channel_and_user):
    '''
    test function. checks that an access error is raised when sendlater is
    given an invalid token
    '''
    channel_id = new_channel_and_user['channel_id']
    time_sent = get_current_timestamp() + 2
    with pytest.raises(AccessError):
        message_sendlater(inv_token, channel_id, 'message', time_sent)

def test_sendlater_invalid_inputs(new_channel_and_user, user_chas):
    '''
    test function.
    checks that errors are raised when sendlater is given invalid inputs
    '''
    token = new_channel_and_user['token']
    channel_id = new_channel_and_user['channel_id']
    time_sent = get_current_timestamp() + 2
    time_sent_invalid = get_current_timestamp() - 2
    with pytest.raises(InputError):
        message_sendlater(token, -1, 'message', time_sent)
    with pytest.raises(InputError):
        message_sendlater(token, channel_id, '1'*1001, time_sent)
    with pytest.raises(InputError):
        message_sendlater(token, channel_id, '', time_sent)
    with pytest.raises(AccessError):
        message_sendlater(user_chas['token'], channel_id, 'sdd', time_sent)
    with pytest.raises(AccessError):
        message_sendlater(user_chas['token'], channel_id, 'sdd', time_sent_invalid)


def test_sendlater_valid_inputs(new_channel_and_user):
    '''
    checks that message is added to channels message after a delay
    '''
    token = new_channel_and_user['token']
    channel_id = new_channel_and_user['channel_id']
    time_sent = get_current_timestamp() + 2
    test_message = message_sendlater(token, channel_id, 'hi', time_sent)
    assert isinstance(test_message, dict)
    assert len(channel_messages(token, channel_id, 0)['messages']) == 0
    sleep(2.5)
    assert len(channel_messages(token, channel_id, 0)['messages']) == 1
