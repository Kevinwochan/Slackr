import pytest
from user import user_profile, user_profile_setname, user_profile_setemail, user_profile_sethandle
from auth import auth_register
from error import InputError, AccessError

#Assumption: anyone can view anyones profile
def test_profile_invalid_token(inv_token):
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    with pytest.raises(AccessError) as e:
        user_profile(inv_token, test_user['u_id'])

def test_setname_invalid_token(inv_token):
    with pytest.raises(AccessError) as e:
        user_profile_setname(inv_token, "John", "Smith")

def test_setemail_invalid_token(inv_token):
    with pytest.raises(AccessError) as e:
        user_profile_setemail(inv_token, "testemail@gmail.com")

def test_sethandle_invalid_token(inv_token):
    with pytest.raises(AccessError) as e:
        user_profile_sethandle(inv_token, 'hjacob')
