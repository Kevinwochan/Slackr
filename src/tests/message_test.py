#!/usr/bin/python3.7

import pytest
from src.error import AccessError, InputError
from src.channels import channels_create
from src.channel import channel_join
from src.auth import auth_register
from src.message import message_edit, message_remove, message_send


@pytest.fixture
def new_user():
    """creates a new user"""
    return auth_register("z5555555@unsw.edu.au", "password",
                         "placeholder_first_name", "placeholder_last_name")


@pytest.fixture
def new_channel_and_user(new_user):
    """creates a new user then a new channel and returns a merged dictionary"""
    new_channel = channels_create(new_user['token'],
                                  "placeholder_channel_name", False)
    return {**new_channel, **new_user}


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
                                      "placeholder_first_name1",
                                      "placeholder_last_name1")

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
                                      "placeholder_first_name1",
                                      "placeholder_last_name1")

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
                               "placeholder_first_name1",
                               "placeholder_last_name1")
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'a')
    channel_join(not_author['token'], new_channel_and_user['channel_id'])

    with pytest.raises(AccessError):
        assert message_remove(not_author['token'], message['message_id'])


def test_removing_authored_message(new_channel_and_user):
    """ Tests the successful removal of a message from a user that sent it"""
    author = auth_register("z6666666@unsw.edu.au", "password",
                           "placeholder_first_name1", "placeholder_last_name1")
    channel_join(author['token'], new_channel_and_user['channel_id'])
    message = message_send(author['token'], new_channel_and_user['channel_id'],
                           'a')
    message_remove(author['token'], message['message_id'])


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
                                      "placeholder_first_name1",
                                      "placeholder_last_name1")

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
                               "placeholder_first_name1",
                               "placeholder_last_name1")
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'a')
    channel_join(not_author['token'], new_channel_and_user['channel_id'])

    with pytest.raises(AccessError):
        assert message_edit(not_author['token'], message['message_id'],
                            'new message to replace existing message')


def test_editing_authored_message(new_channel_and_user):
    """ Tests the successful edit of a message from a user that sent it"""
    author = auth_register("z6666666@unsw.edu.au", "password",
                           "placeholder_first_name1", "placeholder_last_name1")
    channel_join(author['token'], new_channel_and_user['channel_id'])
    message = message_send(author['token'], new_channel_and_user['channel_id'],
                           'a')
    message_edit(author['token'], message['message_id'],
                 'new message to replace existing message')


def test_editing_authored_message_with_empty_message(new_channel_and_user):
    """ Tests replacing a message with an empty message"""
    author = auth_register("z6666666@unsw.edu.au", "password",
                           "placeholder_first_name1", "placeholder_last_name1")
    channel_join(author['token'], new_channel_and_user['channel_id'])
    message = message_send(author['token'], new_channel_and_user['channel_id'],
                           'a')
    with pytest.raises(InputError):
        message_edit(author['token'], message['message_id'], '')


def test_editing_with_invalid_token(new_channel_and_user):
    """ Tests that an access error is thrown when an an invalid token is used """
    message = message_send(new_channel_and_user['token'],
                           new_channel_and_user['channel_id'], 'a')
    with pytest.raises(AccessError):
        message_edit('invalid token', message['message_id'],
                     'new message to replace existing message')
