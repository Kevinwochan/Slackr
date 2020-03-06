import pytest
from user import user_profile, user_profile_setname, user_profile_setemail, user_profile_sethandle
from auth import auth_register
from error import InputError, AccessError

'''
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
@pytest.fixture
def user1():
    return auth_register("testemail@gmail.com", "1234567", "John", "Smith")

@pytest.fixture
def user2():
    return auth_register("testdiff@gmail.com", "1234567", "Jane", "Doe")

################################################################################
##                          ||Tests: user_profile||                           ##
################################################################################

def test_profile_invalid_token(inv_token):
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    with pytest.raises(AccessError) as e:
        user_profile(inv_token, test_user['u_id'])

# Need to double check this logic.
# Subracting 1 from the only valid id to ENSURE that i am using an invalid,
# unused id. The logic being that there is only 1 user registered, so there is
# only one valid id. id -1 is therefor != id, and so must be invalid
def test_profile_invalid_id(user1):
    inv_id = user1['u_id'] - 1
    with pytest.raises(InputError) as e:
        user_profile(user1['token'], inv_id)

# Checking all returned data is of the right type
def test_profile_return_types(user1):
    profile_return = user_profile(user1['token'], user1['u_id'])
    assert type(profile_return) == dict

    assert 'user' in profile_return.keys()
    user1_prof = profile_return['user']
    assert type(user1_prof) == dict

    assert 'u_id' in user1_prof
    assert type(user1_prof['u_id']) == int

    assert 'email' in user1_prof
    assert type(user1_prof['email']) == str

    assert 'name_first' in user1_prof
    assert type(user1_prof['name_first']) == str

    assert 'name_last' in user1_prof
    assert type(user1_prof['name_last']) == str

    assert 'handle_str' in user1_prof
    assert type(user1_prof['handle_str']) == str

# Checking that test_profile returns data matching the user
def test_profile_return_data(user1):
    user1_prof = user_profile(user1['token'], user1['u_id'])['user']

    assert user1_prof['u_id'] == user1['u_id']
    assert user1_prof['email'] == user1['email']
    assert user1_prof['name_first'] == user1['name_first']
    assert user1_prof['name_last'] == user1['name_last']
    assert len(user1_prof['handle_str']) <= 20

# Checking that test_profile returns the data of the user corresponding to u_id NOT the token
def test_profile_return_diff_user(user1, user2):
    # Calling user profile with user1's token and user2's u_id
    user2_prof = user_profile(user1['token'], user2['u_id'])['user']
    assert user2_prof['u_id'] == user2['u_id']
    assert user2_prof['email'] == user2['email']
    assert user2_prof['name_first'] == user2['name_first']
    assert user2_prof['name_last'] == user2['name_last']
    assert len(user1_prof['handle_str']) <= 20

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
