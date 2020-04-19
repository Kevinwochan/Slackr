import pytest
from src.error import InputError, AccessError
from src.admin import permission_change, user_remove
from src.auth import auth_register, auth_logout
from src.channel import channel_invite
from src.channels import channels_create
from src.global_variables import get_channels, get_slackr_owners


@pytest.fixture
def new_user():
    '''creates a new user/owner'''
    return auth_register("z5555555@unsw.edu.au", "password", "first_name",
                         "last_name")


@pytest.fixture
def new_user_2():
    '''create a new user'''
    return auth_register("z2222222@unsw.edu.au", "password2", "first_name2",
                         "last_name2")


@pytest.fixture
def new_user_3():
    '''create a new user'''
    return auth_register("z3333333@unsw.edu.au", "password3", "first_name3",
                         "last_name3")


def test_invalid_token(new_user, new_user_2):
    '''tests that permission_change throws an AccessError when it's given an invalid token'''
    auth_logout(new_user['token'])  #invalidating token by logging out
    with pytest.raises(AccessError):
        permission_change(new_user['token'], new_user_2['u_id'], 1)


def test_not_owner(new_user, new_user_2, new_user_3):
    '''tests that a normal user cannot change permission - gives access error'''
    with pytest.raises(AccessError):
        permission_change(new_user_2['token'], new_user_3['u_id'], 1)


def test_invalid_permission_id(new_user, new_user_2):
    '''tests that permission_change throws an InputError when it's given an invalid permission_id'''
    with pytest.raises(InputError):
        permission_change(new_user['token'], new_user_2['u_id'], 3)


def test_invalid_user(new_user):
    '''tests that permission_change throws an InputError when it's given an invalid u_id'''
    with pytest.raises(InputError):
        permission_change(new_user['token'], -1, 1)


def test_member_becoming_owner():
    pass

def test_owner_becoming_member():
    pass


def test_no_permission_change():
    pass

def test_remove_user(new_user, new_user_2):
    channel = channels_create(new_user['token'], "new_channel", False)
    channel_invite(new_user['token'], channel['channel_id'], new_user_2['u_id'])
    print(get_slackr_owners())
    user_remove(new_user['token'], new_user_2['u_id'])
    assert not new_user_2 in get_channels()[channel['channel_id']]['members']
