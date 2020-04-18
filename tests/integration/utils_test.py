'''
    Tests for utility functions
'''
import os
import pytest
from src.auth import auth_register
from src.channels import channels_create
from src.error import AccessError
from src.global_variables import (workspace_reset, get_channels,
                                  get_valid_tokens, get_users,
                                  get_slackr_owners)
from src.utils import check_token, generate_token, invalidate_token


def test_symmetric():
    '''
    A JWT that is encrypted should decrypt to the same integer
    '''
    for user_id in range(100):
        new_token = generate_token(user_id)
        decrypted_token = check_token(new_token)
        assert isinstance(decrypted_token, int)
        assert decrypted_token == user_id


def test_invalidation():
    '''
    A token that has been invalidated should raise an error
    '''
    for user_id in range(100):
        new_token = generate_token(user_id)
        invalidate_token(new_token)
        with pytest.raises(AccessError):
            assert check_token(new_token)
    assert len(get_users()) == 0


def test_application_clean():
    '''
    Tests that all global variables have been emptied by the reset
    '''
    for new_user in range(100):
        user = auth_register("z55555" + str(new_user) + "@unsw.edu.au",
                             "f for hayden rip", "hydaen", "smith")
        channels_create(user['token'], "test channel" + str(new_user), True)
    workspace_reset()
    assert len(get_channels().keys()) == 0
    assert len(get_users().keys()) == 0
    assert len(get_users()) == 0
    assert len(get_slackr_owners()) == 0
    assert len(get_valid_tokens()) == 0
    original_image_folder = os.path.join(os.getcwd(), 'images/original')
    assert len(os.listdir(original_image_folder)) == 1
    cropped_image_folder = os.path.join(os.getcwd(), 'images/cropped')
    assert len(os.listdir(cropped_image_folder)) == 1
