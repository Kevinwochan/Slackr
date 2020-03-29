import pytest
from src.error import InputError, AccessError
from src.auth import auth_login, auth_logout, auth_register


# logout
def test_logout_no_account():
    """Tests logging out without a valid token"""
    with pytest.raises(AccessError):
        assert auth_logout('not a valid token') == {'is_success': False}


def test_logout():
    """Tests logging out after logging in"""
    new_user = auth_register('z5555555@unsw.edu.au', 'password',
                             'placeholder_first_name', 'placeholder_last_name')
    assert auth_logout(new_user['token']) == {'is_success': True}


def test_logout_twice():
    """Tests logging out twice using the same token"""
    new_user = auth_register('z5555555@unsw.edu.au', 'password',
                             'placeholder_first_name', 'placeholder_last_name')
    assert auth_logout(new_user['token']) == {'is_success': True}
    with pytest.raises(AccessError):
        assert auth_logout(new_user['token']) == {'is_success': False}
