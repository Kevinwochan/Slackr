import pytest
from error import InputError, AccessError
from auth import auth_login, auth_logout, auth_register


# Registration
def test_register_email_invalid():
    with pytest.raises(InputError) as e:
        #Assumption: functions will always be given the correct type
        assert auth_register('1234', 'password', 'fname', 'lname')
    with pytest.raises(InputError) as e:
        assert auth_register('@unsw.edu.au', 'password', 'fname', 'lname')
    with pytest.raises(InputError) as e:
        assert auth_register('username', 'password', 'fname', 'lname')
    with pytest.raises(InputError) as e:
        assert auth_register('', 'password', 'fname', 'lname')

def test_register_email_in_use():
    new_user = auth_register('z55555555@unsw.edu.au', 'password', 'fname', 'lname')
    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', 'password', 'fname', 'lname')
    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', 'password1', 'fname1', 'lname1')

def test_register_password_too_short():
    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', '12345', 'fname', 'lname')
    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', '', 'fname', 'lname')

def test_register_name_length():
    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', 'password', '', 'lname')

    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', 'password', '1'*51, 'lname')

    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', 'password', 'fname', '')

    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', 'password', 'fname', '1'*51)

def test_registration_return_object():
    new_user = auth_register('z55555555@unsw.edu.au', 'password', 'fname', 'lname')

    ''' - Can you double check this?
    assert type(new_user) is dict
    assert new_user['u_id'] in dict
    assert type(new_user['u_id']) is str
    assert new_user['token'] in dict
    assert type(new_user['token']) is str
    '''

def test_registration_return_unique():
    user1 = auth_register('z55555555@unsw.edu.au', 'password', 'fname', 'lname')
    user2 = auth_register('z44444444@unsw.edu.au', 'password', 'fname', 'lname')
    assert user1['token'] != user2['token']
    assert user1['u_id'] != user2['u_id']

# Login
def test_login_email_invalid():
    with pytest.raises(InputError) as e:
        assert auth_login('1234', 'password')
    with pytest.raises(InputError) as e:
        assert auth_login('@unsw.edu.au', 'password')
    with pytest.raises(InputError) as e:
        assert auth_login('username', 'password')
    with pytest.raises(InputError) as e:
        assert auth_login('', 'password')

def test_login_no_user_found():
    with pytest.raises(InputError) as e:
        auth_login('z5555555@unsw.edu.au', 'password')

def test_login_password_incorrect():
    new_user = auth_register('z5555555@unsw.edu.au', 'password', 'fname', 'lname')
    with pytest.raises(InputError) as e:
        auth_login('z5555555@unsw.edu.au', 'incorrect password')

def test_login_return_object():
    new_user = auth_register('z55555555@unsw.edu.au', 'password', 'fname', 'lname')
    login = auth_login('z55555555@unsw.edu.au', 'password')
    ''' -Can you double check this
    assert type(login) is dict
    assert login['u_id'] in dict
    assert type(login['u_id']) is str
    assert login['token'] in dict
    assert type(login['token']) is str
    assert login['u_id'] == new_user['u_id']
    '''

# logout
def test_logout():
    new_user = auth_register('z5555555@unsw.edu.au', 'password', 'fname', 'lname')
    login = auth_login('z5555555@unsw.edu.au', 'password')
    assert 'token' in login
    assert auth_logout(login['token']) == {'is_success' : True}
    # Checking that auth_logout invalidates the token
    with pytest.raises(AccessError) as e:
        assert auth_logout(login['token']) == {'is_success' : True}

def test_valid_credentials():
    user = auth_register('z5555555@unsw.edu.au', 'password', 'first', 'last')
    ''' -Can you double check this
    assert 'u_id' in user
    assert type(user['u_id']) is string
    assert 'token' in user
    assert type(user['token']) is string
    '''
