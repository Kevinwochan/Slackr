import pytest
from src.error import InputError, AccessError
from src.auth import auth_login, auth_logout, auth_register


# Login
def test_login_email_invalid():
    """Tests that logging in throws an input error when a invalid email is used"""
    with pytest.raises(InputError):
        assert auth_login('1234', 'password')
    with pytest.raises(InputError):
        assert auth_login('@unsw.edu.au', 'password')
    with pytest.raises(InputError):
        assert auth_login('username', 'password')
    with pytest.raises(InputError):
        assert auth_login('', 'password')


def test_login_no_user_found():
    """Tests that logging in throws an error when no account exists with that email"""
    with pytest.raises(InputError):
        auth_login('z5555555@unsw.edu.au', 'password')


def test_login_password_incorrect():
    """Tests that logging in throws an error when the password is incorrect"""
    auth_register('z5555555@unsw.edu.au', 'password', 'placeholder_first_name',
                  'placeholder_last_name')
    with pytest.raises(InputError):
        auth_login('z5555555@unsw.edu.au', 'incorrect password')


def test_login_valid_credentials():
    """Tests logging in with valid information returns a dictionary described in the spec"""
    new_user = auth_register('z55555555@unsw.edu.au', 'password',
                             'placeholder_first_name', 'placeholder_last_name')
    login = auth_login('z55555555@unsw.edu.au', 'password')
    assert isinstance(login, dict)
    assert 'u_id' in login
    assert isinstance(login['u_id'], int)
    assert 'token' in login
    assert isinstance(login['token'], str)
    assert login['u_id'] == new_user['u_id']
