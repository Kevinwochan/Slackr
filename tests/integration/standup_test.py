'''
Integration testing of standup functions
'''
from time import sleep
import pytest
from src.standup import standup_start, standup_active, standup_send
from src.error import AccessError, InputError
from src.channel import channel_messages
def test_standup_invalid_token(inv_token, new_channel_and_user):
    '''
    Tests that all standup functions raises raise AccessErrors when given an invalid token.
    '''
    valid_token = new_channel_and_user['token']
    channel_id = new_channel_and_user['channel_id']
    with pytest.raises(AccessError):
        standup_start(inv_token, channel_id, 1)

    standup_start(valid_token, channel_id, 2)
    with pytest.raises(AccessError):
        standup_active(inv_token, channel_id)

    with pytest.raises(AccessError):
        standup_send(inv_token, channel_id, 'this is a message')

def test_standup_invalid_id(new_user):
    '''
    Test fuction.
    Checks that all standup functions raises an InputError when given an invalid channel_id (-1).
    '''
    with pytest.raises(InputError):
        standup_start(new_user['token'], -1, 10)

    with pytest.raises(InputError):
        standup_active(new_user['token'], -1)

    with pytest.raises(InputError):
        standup_send(new_user['token'], -1, 'this is a message')


def test_standup_start_not_member(channel_dav, user_chas):
    '''
    Test function.
    Checks that standup_start raises an AccessError if a user tries to start a
    standup in a channel that they are not a member of.
    '''
    with pytest.raises(AccessError):
        standup_start(user_chas['token'], channel_dav['channel_id'], 1)

    with pytest.raises(AccessError):
        standup_active(user_chas['token'], channel_dav['channel_id'])

    with pytest.raises(AccessError):
        standup_send(user_chas['token'], channel_dav['channel_id'], 'message')


def test_standup_invalid_active(new_channel_and_user):
    '''
    Test function
    checks that for the duration of a standup, starting an new standup in the same channel
    raises an Input error.
    Checks that starting a new standup after a standup has finished does not raise an error
    Checks that standup_active correctly returns when a standup is inactive.
    checks that standup_send raises an error if a standup is inactive
    '''
    token = new_channel_and_user['token']
    channel_id = new_channel_and_user['channel_id']
    assert not standup_active(token, channel_id)['is_active']
    with pytest.raises(InputError):
        standup_send(token, channel_id, 'message')
    standup_start(token, channel_id, 2)
    assert standup_active(token, channel_id)['is_active']
    standup_send(token, channel_id, 'message')

    with pytest.raises(InputError):
        standup_start(token, channel_id, 2)
    sleep(1)
    with pytest.raises(InputError):
        standup_start(token, channel_id, 2)
    sleep(2)
    assert not standup_active(token, channel_id)['is_active']
    standup_start(token, channel_id, 1)
    assert standup_active(token, channel_id)['is_active']

def test_standup_return_type(new_channel_and_user):
    '''
    test function. checks that the return values from standup functions are of the expected types
    '''
    token = new_channel_and_user['token']
    channel_id = new_channel_and_user['channel_id']
    standup = standup_start(token, channel_id, 1)
    assert isinstance(standup, dict)
    assert 'time_finish' in standup.keys()
    assert isinstance(standup['time_finish'], int)

    active_return = standup_active(token, channel_id)
    assert isinstance(active_return['is_active'], bool)
    assert isinstance(active_return['time_finish'], int)

    send_return = standup_send(token, channel_id, 'message')
    assert isinstance(send_return, dict)
    assert len(send_return) == 0

def test_standup_empty(new_channel_and_user):
    '''
    test function.
    tests that if no message was sent during a standup,
    the standup is discarded and not added to a channels messages.
    '''
    token = new_channel_and_user['token']
    channel_id = new_channel_and_user['channel_id']
    standup_start(token, channel_id, 1)
    sleep(1.5)
    messages = channel_messages(token, channel_id, 0)
    assert len(messages['messages']) == 0

def test_standup_send(new_channel_and_user):
    '''
    tests standup send correctly adds a message to a channel
    '''
    token = new_channel_and_user['token']
    channel_id = new_channel_and_user['channel_id']
    standup_start(token, channel_id, 1)
    standup_send(token, channel_id, 'Message 1')
    sleep(1.5)
    messages = channel_messages(token, channel_id, 0)
    assert len(messages['messages']) == 1

def test_standup_send_invalid_message(new_channel_and_user):
    '''
    test function
    checks that standup_send raises an input error when given a message >1000 characters
    '''
    token = new_channel_and_user['token']
    channel_id = new_channel_and_user['channel_id']
    standup_start(token, channel_id, 1)
    with pytest.raises(InputError):
        standup_send(token, channel_id, '1'*1001)
    sleep(1.5)
    messages = channel_messages(token, channel_id, 0)
    assert len(messages['messages']) == 0
