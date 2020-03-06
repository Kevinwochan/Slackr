import pytest
from user import user_profile, user_profile_setname, user_profile_setemail, user_profile_sethandle
from auth import auth_register
from error import InputError, AccessError

'''
user_profile:
    create user, check their own details - check name, email, id match the created anyones
    -- CANT CHECK HANDLE - without making assumptions on how the handle is generated
    create a second user - check that the first can view the seconds details and vice versa
    create one user(to get a valid token): take their user id and subtract 1 - so we know its an invalid user ID
    \ then check that it returns input error when given invalid id
    check all return types

user_profile_setname:
    create user, change name to be invalid, test that error is raised
    create user, change their name, see if the changed name is returned in user_profile_setname
    check that handle + email are unnaffected
    test return type (why???)
User_profile_setemail:
    create user, change email to be invalid, check if error is raised
    change email, check
    check other fields are unnaffected
    check return type


user_profile_sethandle:
    create user, change handle to be invalid, check error
    create 2 users, change user 2 to have user 1's handle, check error is raised
    check other fields are unnaffected
    check return type

user_profile general tests
    test that the right users details are adjusted - THIS SEEMS IMPORTANT

'''

################################################################################
##                          ||Tests: user_profile||                           ##
################################################################################

#Assumption: anyone can view anyones profile
def test_profile_invalid_token(inv_token):
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    with pytest.raises(AccessError) as e:
        user_profile(inv_token, test_user['u_id'])




################################################################################
##                      ||Tests: user_profile_setname||                       ##
################################################################################

def test_setname_invalid_token(inv_token):
    with pytest.raises(AccessError) as e:
        user_profile_setname(inv_token, "John", "Smith")

def test_setemail_invalid_token(inv_token):
    with pytest.raises(AccessError) as e:
        user_profile_setemail(inv_token, "testemail@gmail.com")

def test_sethandle_invalid_token(inv_token):
    with pytest.raises(AccessError) as e:
        user_profile_sethandle(inv_token, 'hjacob')
