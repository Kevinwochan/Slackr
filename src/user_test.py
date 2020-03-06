import pytest
from user import user_profile, user_profile_setname, user_profile_setemail, user_profile_sethandle
from auth import auth_register
from error import InputError, AccessError


def test_user_profile(inv_token):
    print (inv_token)
    assert inv_token == '12345'
