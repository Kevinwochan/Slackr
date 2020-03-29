import pytest
from src.error import InputError, AccessError
from src.admin import permission_change
from src.auth import auth_register

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


def test_invalid_token(new_user_2):
    with pytest.raises(AccessError):
        assert permission_change(-1, new_user_2['u_id'], 1)

def test_():
    pass   

def test_():
    pass   

def test_():
    pass   

def test_():
    pass   
