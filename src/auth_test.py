import pytest
from error import InputError, AccessError
from auth import auth_login, auth_logout, auth_register


# Registration
def test_register_email_invalid():
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


def test_register_email_in_use():
    auth_register('z55555555@unsw.edu.au', 'password',
                  'placeholder_first_name', 'placeholder_last_name')
    with pytest.raises(InputError):
        auth_register('z55555555@unsw.edu.au', 'password',
                      'placeholder_first_name', 'placeholder_last_name')
    with pytest.raises(InputError):
        auth_register('z55555555@unsw.edu.au', 'password1',
                      'placeholder_first_name1', 'placeholder_last_name1')


def test_register_password_too_short():
    with pytest.raises(InputError):
        auth_register('z55555555@unsw.edu.au', '12345',
                      'placeholder_first_name', 'placeholder_last_name')
    with pytest.raises(InputError):
        auth_register('z55555555@unsw.edu.au', '', 'placeholder_first_name',
                      'placeholder_last_name')


def test_register_name_length():
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
    user1 = auth_register('z55555555@unsw.edu.au', 'password',
                          'placeholder_first_name', 'placeholder_last_name')
    user2 = auth_register('z44444444@unsw.edu.au', 'password',
                          'placeholder_first_name', 'placeholder_last_name')
    assert user1['token'] != user2['token']
    assert user1['u_id'] != user2['u_id']


def test_register_valid_credentials():
    new_user = auth_register('z5555555@unsw.edu.au', 'password', 'first',
                             'last')
    assert isinstance(new_user, dict)
    assert 'u_id' in new_user
    assert isinstance(new_user['u_id'], str)
    assert 'token' in new_user
    assert isinstance(new_user['token'], str)


# Login
def test_login_email_invalid():
    with pytest.raises(InputError):
        assert auth_login('1234', 'password')
    with pytest.raises(InputError):
        assert auth_login('@unsw.edu.au', 'password')
    with pytest.raises(InputError):
        assert auth_login('username', 'password')
    with pytest.raises(InputError):
        assert auth_login('', 'password')


def test_login_no_user_found():
    with pytest.raises(InputError):
        auth_login('z5555555@unsw.edu.au', 'password')


def test_login_password_incorrect():
    auth_register('z5555555@unsw.edu.au', 'password', 'placeholder_first_name',
                  'placeholder_last_name')
    with pytest.raises(InputError):
        auth_login('z5555555@unsw.edu.au', 'incorrect password')


def test_login_return_object():
    new_user = auth_register('z55555555@unsw.edu.au', 'password',
                             'placeholder_first_name', 'placeholder_last_name')
    login = auth_login('z55555555@unsw.edu.au', 'password')
    assert isinstance(login, dict)
    assert 'u_id' in login
    assert isinstance(login['u_id'], str)
    assert 'token' in login
    assert isinstance(login['token'], str)
    assert login['u_id'] == new_user['u_id']


# logout
def test_logout_no_account():
    assert auth_logout('not a valid token') == {'is_success': False}


def test_logout():
    new_user = auth_register('z5555555@unsw.edu.au', 'password',
                             'placeholder_first_name', 'placeholder_last_name')
    assert auth_logout(new_user['token']) == {'is_success': True}


def test_logout_twice():
    new_user = auth_register('z5555555@unsw.edu.au', 'password',
                             'placeholder_first_name', 'placeholder_last_name')
    assert auth_logout(new_user['token']) == {'is_success': True}
    with pytest.raises(AccessError):
        assert auth_logout(new_user['token']) == {'is_success': False}
