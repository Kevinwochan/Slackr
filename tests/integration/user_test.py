import pytest
from src.user import user_profile, user_profile_setname, user_profile_setemail, user_profile_sethandle, user_profile_setimage
from src.auth import auth_register
from src.error import InputError, AccessError

# Note: fixture inv_token is imported by pytest from conftest.py automatically.


################################################################################
##                          ||Tests: user_profile||                           ##
################################################################################
# invalid_token functions call the fixture inv_token. this fixture is located in
# the file conftest.py and is automatically imported by pytest. This fixture
# generates an invalid token using the register and logout functions
def test_profile_invalid_token(inv_token):
    test_user = auth_register("testemail@gmail.com", "1234567", "John",
                              "Smith")
    with pytest.raises(AccessError):
        user_profile(inv_token, test_user['u_id'])


def test_profile_invalid_id(user1):
    ''' looking up a profile for an invalid user_id '''
    with pytest.raises(InputError):
        user_profile(user1['token'], -1)


# Checking all returned data is of the right type
def test_profile_return_types(user1):
    user1_profile = user_profile(user1['token'], user1['u_id'])['user']
    assert isinstance(user1_profile, dict)

    assert 'u_id' in user1_profile
    assert isinstance(user1_profile['u_id'], int)

    assert 'email' in user1_profile
    assert isinstance(user1_profile['email'], str)

    assert 'name_first' in user1_profile
    assert isinstance(user1_profile['name_first'], str)

    assert 'name_last' in user1_profile
    assert isinstance(user1_profile['name_last'], str)

    assert 'handle_str' in user1_profile
    assert isinstance(user1_profile['handle_str'], str)


# Checking that test_profile returns data matching the user
def test_profile_return_data(user1):
    user1_profile = user_profile(user1['token'], user1['u_id'])['user']

    assert user1_profile['u_id'] == user1['u_id']
    assert user1_profile['email'] == user1['email']
    assert user1_profile['name_first'] == user1['name_first']
    assert user1_profile['name_last'] == user1['name_last']
    assert len(user1_profile['handle_str']) <= 20


# Checking that test_profile returns the data of the user corresponding to u_id
# NOT the token.
def test_profile_return_diff_user(user1, user2):
    # Calling user profile with user1's token and user2's u_id
    user2_prof = user_profile(user1['token'], user2['u_id'])['user']
    assert user2_prof['u_id'] == user2['u_id']
    assert user2_prof['email'] == user2['email']
    assert user2_prof['name_first'] == user2['name_first']
    assert user2_prof['name_last'] == user2['name_last']
    assert len(user2_prof['handle_str']) <= 20


################################################################################
##                      ||Tests: user_profile_setname||                       ##
################################################################################


def test_setname_invalid_token(inv_token):
    with pytest.raises(AccessError):
        user_profile_setname(inv_token, "John", "Smith")


def test_setname_invalid_name(user1):
    with pytest.raises(InputError):
        user_profile_setname(user1['token'], '', 'name')
    with pytest.raises(InputError):
        user_profile_setname(user1['token'], 'name', '')
    with pytest.raises(InputError):
        user_profile_setname(user1['token'], 'name', 'n' * 51)
    with pytest.raises(InputError):
        user_profile_setname(user1['token'], 'n' * 51, 'name')
    with pytest.raises(InputError):
        user_profile_setname(user1['token'], 'n' * 51, 'n' * 51)
    with pytest.raises(InputError):
        user_profile_setname(user1['token'], '', '')

    # Checking that user1's names have not been altered
    #Assumption: functions that result in errors perform no actions
    user1_profile = user_profile(user1['token'], user1['u_id'])['user']
    assert user1_profile['name_first'] == user1['name_first']
    assert user1_profile['name_last'] == user1['name_last']


# Runs edge case names to ensure no errors are raised
def test_setname_edge_cases(user1):
    user_profile_setname(user1['token'], 'n' * 50, 'name')
    user_profile_setname(user1['token'], 'name', 'n' * 50)
    user_profile_setname(user1['token'], 'n' * 50, 'l' * 50)
    user_profile_setname(user1['token'], 'name', 'n')
    user_profile_setname(user1['token'], 'n', 'name')
    user_profile_setname(user1['token'], 'n', 'n')


def test_setname_valid(user1):
    user1_profile = user_profile(user1['token'], user1['u_id'])['user']
    new_name_first = 'Different'
    new_name_last = 'Name'

    user_profile_setname(user1['token'], new_name_first, new_name_last)
    new_user1_profile = user_profile(user1['token'], user1['u_id'])['user']
    assert new_user1_profile['name_first'] == new_name_first
    assert new_user1_profile['name_last'] == new_name_last
    # Check that no other field has been changed
    assert user1_profile['u_id'] == new_user1_profile['u_id']
    assert user1_profile['email'] == new_user1_profile['email']
    assert user1_profile['handle_str'] == new_user1_profile['handle_str']


################################################################################
##                      ||Tests: user_profile_setemail||                      ##
################################################################################
def test_setemail_invalid_token(inv_token):
    with pytest.raises(AccessError):
        user_profile_setemail(inv_token, "newemail@gmail.com")


def test_setemail_invalid(user1):
    with pytest.raises(InputError):
        user_profile_setemail(user1['token'], '1234')
    with pytest.raises(InputError):
        user_profile_setemail(user1['token'], '@unsw.edu.au')
    with pytest.raises(InputError):
        user_profile_setemail(user1['token'], 'username')
    with pytest.raises(InputError):
        user_profile_setemail(user1['token'], '')

    # Checking that user1's email has not been altered
    user1_profile = user_profile(user1['token'], user1['u_id'])['user']
    assert user1_profile['email'] == user1['email']


def test_setemail_taken(user1, user2):
    '''
    when a user tries to set their user profile email to an email that is already
    in use by another user, an input error is thrown
    '''
    with pytest.raises(InputError):
        user_profile_setemail(user1['token'], user2['email'])
    with pytest.raises(InputError):
        user_profile_setemail(user2['token'], user1['email'])
    # Checking that user's emails have not been altered
    user1_profile = user_profile(user1['token'], user1['u_id'])['user']
    user2_prof = user_profile(user2['token'], user2['u_id'])['user']
    assert user1_profile['email'] == user1['email']
    assert user2_prof['email'] == user2['email']


def test_setemail_valid(user1):
    user1_profile = user_profile(user1['token'], user1['u_id'])['user']
    new_email = 'newemail@gmail.com'
    user_profile_setemail(user1['token'], new_email)

    new_user1_profile = user_profile(user1['token'], user1['u_id'])['user']
    assert new_user1_profile['email'] == new_email

    # Check that no other field has been changed
    assert user1_profile['u_id'] == new_user1_profile['u_id']
    assert user1_profile['name_first'] == new_user1_profile['name_first']
    assert user1_profile['name_last'] == new_user1_profile['name_last']
    assert user1_profile['handle_str'] == new_user1_profile['handle_str']


################################################################################
##                     ||Tests: user_profile_sethandle||                      ##
################################################################################
def test_sethandle_invalid_token(inv_token):
    with pytest.raises(AccessError):
        user_profile_sethandle(inv_token, 'newhandle')


def test_sethandle_invalid(user1):
    user1_profile_before = user_profile(user1['token'], user1['u_id'])['user']
    with pytest.raises(InputError):
        user_profile_sethandle(user1['token'], 'a')
    with pytest.raises(InputError):
        user_profile_sethandle(user1['token'], 'a' * 21)

    # Checking that user1's handle has not been altered
    user1_profile_after = user_profile(user1['token'], user1['u_id'])['user']
    assert user1_profile_after == user1_profile_before


def test_sethandle_taken(user1, user2):
    user1_profile = user_profile(user1['token'], user1['u_id'])['user']
    user2_prof = user_profile(user2['token'], user2['u_id'])['user']

    with pytest.raises(InputError):
        user_profile_sethandle(user1['token'], user2_prof['handle_str'])
    with pytest.raises(InputError):
        user_profile_sethandle(user2['token'], user1_profile['handle_str'])

    # Checking that user's handles have not been altered
    new_user1_profile = user_profile(user1['token'], user1['u_id'])['user']
    new_user2_prof = user_profile(user2['token'], user2['u_id'])['user']
    assert user1_profile['handle_str'] == new_user1_profile['handle_str']
    assert user2_prof['handle_str'] == new_user2_prof['handle_str']


def test_sethandle_valid(user1):
    user1_profile = user_profile(user1['token'], user1['u_id'])['user']
    new_handle = 'newhandle'
    user_profile_sethandle(user1['token'], new_handle)

    new_user1_profile = user_profile(user1['token'], user1['u_id'])['user']
    assert new_user1_profile['handle_str'] == new_handle

    # Check that no other field has been changed
    assert user1_profile['u_id'] == new_user1_profile['u_id']
    assert user1_profile['email'] == new_user1_profile['email']
    assert user1_profile['name_first'] == new_user1_profile['name_first']
    assert user1_profile['name_last'] == new_user1_profile['name_last']


################################################################################
##                    ||General Tests: user_profile_set*||                    ##
################################################################################
# Checks that the set functions return the right type (empty dictionary)
# This is probably unimportant
def test_set_return_type(user1):
    setname_return = user_profile_setname(user1['token'], 'new', 'name')
    setemail_return = user_profile_setemail(user1['token'],
                                            'newemail@gmail.com')
    sethandle_return = user_profile_sethandle(user1['token'], 'newhandle')
    assert isinstance(setname_return, dict)
    assert isinstance(setemail_return, dict)
    assert isinstance(sethandle_return, dict)

    assert len(setname_return) == 0
    assert len(setemail_return) == 0
    assert len(sethandle_return) == 0


# Checking that entering existing details raises no errors and changes no user
# details.
def test_set_same(user1):
    user1_profile = user_profile(user1['token'], user1['u_id'])['user']

    user_profile_setname(user1['token'], user1['name_first'],
                         user1['name_last'])
    user_profile_setemail(user1['token'], user1['email'])
    user_profile_sethandle(user1['token'], user1_profile['handle_str'])

    new_user1_profile = user_profile(user1['token'], user1['u_id'])['user']

    assert new_user1_profile['email'] == user1_profile['email']
    assert new_user1_profile['name_first'] == user1_profile['name_first']
    assert new_user1_profile['name_last'] == user1_profile['name_last']
    assert new_user1_profile['handle_str'] == user1_profile['handle_str']

def test_user_setimage_valid(user1):
    user_profile_setimage(user1['token'], 'https://i.imgur.com/MJcwL1W.jpg', 0, 0, 200, 200)

def test_user_setimage_invalid_img_url(user1):
    with pytest.raises(InputError):
        user_profile_setimage(user1['token'], 'https://i.imgur.com/MJcwL1W', 0, 0, 200, 200)

def test_user_setimage_invalid_dimensions(user1):
    with pytest.raises(InputError):
        user_profile_setimage(user1['token'], 'https://i.imgur.com/MJcwL1W', -4, 34, 34200, -200)