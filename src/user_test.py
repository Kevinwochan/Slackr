import pytest
from user import user_profile, user_profile_setname, user_profile_setemail, user_profile_sethandle
# from auth import auth_register, auth_logout
from error import InputError, AccessError

'''
all blackbox testing - all input and acess errors
test functionality
'''

 # Generates an invalid token for testing AcessErrors. uses auth_register and auth_logout
 # Assumes that 'invalidtokenemail@gmail.com' is a valid unused email
'''
@pytest.fixture
def inv_token():
    inv_token = auth_register('invalidtokenemail@gmail.com', 'password', 'invalid', 'token')['token']
    # Invalidate the token using logout (and check it worked)
    assert auth_logout(inv_token) == {'is_success': True}
    return inv_token
'''
def test_user_profile(inv_token):
    print (inv_token)
    assert inv_token == '12345'
