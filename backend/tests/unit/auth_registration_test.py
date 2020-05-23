import pytest
from src.error import InputError
from src.auth import auth_register


# Registration
def test_register_email_invalid():
    """Tests that registration throws an input error for invalid emails, invalid emails are defined by
    https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    """
    with pytest.raises(InputError):
        assert auth_register('1234', 'password', 'placeholder_first_name',
                             'placeholder_last_name')
    with pytest.raises(InputError):
        assert auth_register('@unsw.edu.au', 'password',
                             'placeholder_first_name', 'placeholder_last_name')
    with pytest.raises(InputError):
        assert auth_register('username', 'password', 'placeholder_first_name',
                             'placeholder_last_name')
    with pytest.raises(InputError):
        assert auth_register('', 'password', 'placeholder_first_name',
                             'placeholder_last_name')
    with pytest.raises(InputError):
        assert auth_register('z55555555.unsw.edu.au', 'password',
                             'placeholder_first_name', 'placeholder_last_name')


def test_register_email_in_use():
    """Tests that registration throws an input error when an email is used to create two accounts"""
    auth_register('z55555555@unsw.edu.au', 'password',
                  'placeholder_first_name', 'placeholder_last_name')
    with pytest.raises(InputError):
        auth_register('z55555555@unsw.edu.au', 'password1',
                      'placeholder_first_name1', 'placeholder_last_name1')


def test_register_password_too_short():
    """Tests that registration throws an input error when a password is shorter than 6 characters"""
    with pytest.raises(InputError):
        auth_register('z55555555@unsw.edu.au', '12345',
                      'placeholder_first_name', 'placeholder_last_name')
    with pytest.raises(InputError):
        auth_register('z55555555@unsw.edu.au', '', 'placeholder_first_name',
                      'placeholder_last_name')


def test_register_name_length():
    """Tests that registration throws an input error when the name entered is less than 1 character or more than 50 characters"""
    with pytest.raises(InputError):
        auth_register('z55555555@unsw.edu.au', 'password', '',
                      'placeholder_last_name')

    with pytest.raises(InputError):
        auth_register('z55555555@unsw.edu.au', 'password', '1' * 51,
                      'placeholder_last_name')

    with pytest.raises(InputError):
        auth_register('z55555555@unsw.edu.au', 'password',
                      'placeholder_first_name', '')

    with pytest.raises(InputError):
        auth_register('z55555555@unsw.edu.au', 'password',
                      'placeholder_first_name', '1' * 51)


def test_register_return_unique():
    """Tests that registration generates unique tokens """
    user1 = auth_register('z55555555@unsw.edu.au', 'password',
                          'placeholder_first_name', 'placeholder_last_name')
    user2 = auth_register('z44444444@unsw.edu.au', 'password',
                          'placeholder_first_name', 'placeholder_last_name')
    assert user1['token'] != user2['token']
    assert user1['u_id'] != user2['u_id']


def test_register_valid_credentials():
    """Tests that registration works using valid information and everything i"""
    new_user = auth_register('z5555555@unsw.edu.au', 'password', 'Michael',
                             'Liang')
    assert isinstance(new_user, dict)
    assert 'u_id' in new_user
    assert isinstance(new_user['u_id'], int)
    assert 'token' in new_user
    assert isinstance(new_user['token'], str)
