'''
Integration testing of standup functions
'''
from time import sleep
import pytest
from src.auth import auth_register
from src.channels import channels_create
from src.standup import standup_start, standup_active, standup_send
from src.error import AccessError, InputError

def test_standup_start_invalid_token(inv_token, channel_dav):
    '''
    Tests that standup_start raises an access error when given an invalid token
    '''
    with pytest.raises(AccessError):
        standup_start(inv_token, channel_dav['channel_id'], 5)

def test_standup_start_invalid_id(new_user):
    '''
    Tests fuction.
    Checks that standup start raises an Input error when given an invalid channel_id (-1).
    '''
    with pytest.raises(InputError):
        standup_start(new_user['token'], -1, 10)

def test_standup_start_active_standup(new_channel_and_user):
    '''
    Test function
    checks that for the duration of a standup, starting an new standup in the same channel
    raises an Input error.
    Checks that starting a new standup after a standup has finished does not raise an error
    '''
    token = new_channel_and_user['token']
    channel_id = new_channel_and_user['channel_id']
    standup_start(token, channel_id, 2)
    with pytest.raises(InputError):
        standup_start(token, channel_id, 2)
    sleep(1)
    with pytest.raises(InputError):
        standup_start(token, channel_id, 2)
    sleep(1)
    standup_start(token, channel_id, 1)
    sleep(1)

def test_standup_start_return_type(new_channel_and_user):
    token = new_channel_and_user['token']
    channel_id = new_channel_and_user['channel_id']
    standup = standup_start(token, channel_id, 2)
    assert isinstance(standup, dict)
    assert 'time_finish' in standup.keys()
    assert isinstance(standup['time_finish'], int)
*