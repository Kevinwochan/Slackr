import pytest
from src.auth import auth_register, auth_logout
from src.global_variables import workspace_reset
from src.channels import channels_create


# Generates an invalid token for testing AcessErrors. uses auth_register and auth_logout
# Assumes that 'invalidtokenemail@gmail.com' is a valid unused email
@pytest.fixture
def inv_token():
    '''
    Generates an always invalid token
    '''
    inv_token = auth_register('invalidtokenemail@gmail.com', 'password',
                              'invalid', 'token')['token']
    # Invalidate the token using logout (and check it worked)
    assert auth_logout(inv_token) == {'is_success': True}
    return inv_token


@pytest.fixture(autouse=True, scope='function')
def clean_application():
    '''
    Deletes all application data by resetting the workspace
    '''
    workspace_reset()


# Set up the users
@pytest.fixture
def user_dav():
    return auth_register("dav@gmail.com", "dav123", "dav", "zhu")


@pytest.fixture
def user_jas():
    return auth_register("jas@gmail.com", "jas123", "jas", "zhu")


@pytest.fixture
def user_chas():
    return auth_register("chas@gmail.com", "chas123", "chas", "zhu")


# Set up a channel created by dav
@pytest.fixture
def channel_dav(user_dav):
    return channels_create(user_dav['token'], "channel_dav", False)


@pytest.fixture
def new_user():
    """creates a new user"""
    return auth_register("z5555555@unsw.edu.au", "password", "first_name",
                         "last_name")


@pytest.fixture
def new_user_2():
    """create a new user"""
    return auth_register("z2222222@unsw.edu.au", "password2", "first_name2",
                         "last_name2")


@pytest.fixture
def new_user_3():
    """create a new user"""
    return auth_register("z3333333@unsw.edu.au", "password3", "first_name3",
                         "last_name3")


@pytest.fixture
def new_user_4():
    """create a new user"""
    return auth_register("z4444444@unsw.edu.au", "password4", "first_name4",
                         "last_name4")


@pytest.fixture
def new_channel_and_user(new_user):
    """creates a new user then a new channel and returns a merged dictionary"""
    new_channel = channels_create(new_user['token'], "channel_name", False)
    return {**new_channel, **new_user}


@pytest.fixture
def new_channel_and_user_2(new_user_2):
    """creates a new user then a new channel and returns a merged dictionary"""
    new_channel_2 = channels_create(new_user_2['token'], "channel_name", False)
    return {**new_channel_2, **new_user_2}


# Creates a user and returns their details
@pytest.fixture
def user1():
    email = "testemail@gmail.com"
    name_first = "John"
    name_last = "Smith"

    user = auth_register(email, "1234567", name_first, name_last)
    return {
        'token': user['token'],
        'u_id': user['u_id'],
        'email': email,
        'name_first': name_first,
        'name_last': name_last
    }


@pytest.fixture
def user2():
    email = "testdiff@gmail.com"
    name_first = "Jane"
    name_last = "Doe"

    user = auth_register(email, "1234567", name_first, name_last)
    return {
        'token': user['token'],
        'u_id': user['u_id'],
        'email': email,
        'name_first': name_first,
        'name_last': name_last,
    }
