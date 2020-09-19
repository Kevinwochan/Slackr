import pytest
from src.error import AccessError
from src.auth import auth_logout, auth_register


# logout
def test_logout_no_account():
    """Tests logging out without a valid token"""
    with pytest.raises(AccessError):
        assert auth_logout('not a valid token') == {'is_success': False}
