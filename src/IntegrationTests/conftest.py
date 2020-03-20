import pytest
from src.auth import auth_register, auth_logout

 # Generates an invalid token for testing AcessErrors. uses auth_register and auth_logout
 # Assumes that 'invalidtokenemail@gmail.com' is a valid unused email
@pytest.fixture
def inv_token():
    inv_token = auth_register('invalidtokenemail@gmail.com', 'password', 'invalid', 'token')['token']
    # Invalidate the token using logout (and check it worked)
    assert auth_logout(inv_token) == {'is_success': True}
    return inv_token
