import pytest
from src.error import InputError
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
