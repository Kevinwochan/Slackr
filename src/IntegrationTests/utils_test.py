'''
    Tests for utility functions
'''
import pytest
from src.auth import auth_register, USERS
from src.channels import channels_create, CHANNELS
from src.error import AccessError
from src.utils import workspace_reset, check_token, generate_token, invalidate_token, curr_users


def test_symmetric():
    '''
    A JWT that is encrypted should decrypt to the same integer
    '''
    for user_id in range(100):
        new_token = generate_token(user_id)
        assert check_token(new_token) == new_token


def test_invalidation():
    '''
    A token that has been invalidated should raise an error
    '''
    for user_id in range(100):
        new_token = generate_token(user_id)
        invalidate_token(new_token)
        with pytest.raises(AccessError):
            assert check_token(new_token) == new_token
    assert len(curr_users) == 0


def test_application_clean():
    '''
    Tests that all global variables have been emptied by the reset
    '''
    # TODO: once global variables are stable
    for new_user in range(100):
        user = auth_register("z55555" + str(new_user) + "@unsw.edu.au",
                             "f for hayden rip", "hydaen", "smith")
        channels_create(user['token'], "test channel" + str(new_user), True)
    workspace_reset()
    assert len(CHANNELS.keys() == 0)
    assert len(USERS.keys() == 0)
    assert len(curr_users == 0)
