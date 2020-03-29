import pytest
from src.error import InputError, AccessError
from src.admin import permission_change
from src.auth import auth_register, auth_logout

@pytest.fixture
def new_user():
    '''creates a new user/owner'''
    return auth_register("z5555555@unsw.edu.au", "password",
                         "first_name", "last_name")

@pytest.fixture
def new_user_2():
    '''create a new user'''
    return auth_register("z2222222@unsw.edu.au", "password2",
                         "first_name2", "last_name2")


def test_invalid_token(new_user, new_user_2):
    '''tests that permission_change throws an AccessError when it's given an invalid token'''
    auth_logout(new_user['token']) #invalidating token by logging out
    with pytest.raises(AccessError):
        permission_change(new_user['u_id'], new_user_2['u_id'], 1)

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
