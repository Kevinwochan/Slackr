import pytest
from error import InputError
import auth

# note, what happens if you dont give it a string?
#make multiple users + check that their tokes are different
# Registration
def test_register_email_invalid():
    with pytest.raises(InputError) as e:
        #Assumption: functions will always be given the correct type
        #changed this test to pass a string as email rather than int
        assert auth_register('1234', 'password', 'fname', 'lname')
    with pytest.raises(InputError) as e:
        assert auth_register('@unsw.edu.au', 'password', 'fname', 'lname')
    with pytest.raises(InputError) as e:
        assert auth_register('username', 'password', 'fname', 'lname')
    #empty email

def test_register_email_in_use():
    new_user = auth_register('z55555555@unsw.edu.au', 'password', 'fname', 'lname')
    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', 'password', 'fname', 'lname')
    #with new names and such
def test_register_password_too_short():
    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', '12345', 'fname', 'lname')
    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', '', 'fname', 'lname')
    #password too long?

def test_register_name_length():
    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', 'password', '1', 'lname')

    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', 'password', '1'*51, 'lname')

    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', 'password', 'fname', '1')

    with pytest.raises(InputError) as e:
        auth_register('z55555555@unsw.edu.au', 'password', 'fname', '1'*51)
    #empty names

def test_registration_return_object():
    new_user = auth_register('z55555555@unsw.edu.au', 'password', 'fname', 'lname')
    assert type(new_user) is dict
    assert new_user['u_id'] in dict
    assert type(new_user['u_id']) is str
    assert new_user['token'] in dict
    assert type(new_user['token']) is str
    # check u_id <=20 characters
    #check u_id is lowercase
    # make second user with same name, check u_id is different

# Login
def test_login_email_invalid():
    with pytest.raises(InputError) as e:
        #changed this test to pass a string as email rather than int
        assert auth_login('1234', 'password')
    with pytest.raises(InputError) as e:
        assert auth_login('@unsw.edu.au', 'password')
    with pytest.raises(InputError) as e:
        assert auth_login('username', 'password')
    #same email errors as register

def test_login_no_user_found():
    with pytest.raises(InputError) as e:
        auth_login('z5555555@unsw.edu.au', 'password')

def test_login_password_incorrect(get_new_user):
    new_user = auth_register('z5555555@unsw.edu.au', 'password')
    with pytest.raises(InputError) as e:
        auth_login('z555555@unsw.edu.au', 'incorrect password')

def test_login_return_object():
    new_user = auth_register('z55555555@unsw.edu.au', 'password', 'fname', 'lname')
    login = auth_login('z55555555@unsw.edu.au', 'password')
    assert type(login) is dict
    assert login['u_id'] in dict
    assert type(login['u_id']) is str
    assert login['token'] in dict
    assert type(login['token']) is str
    assert login['u_id'] = new_user['u_id']
    #same as reg

# logout
def test_logout():
    new_user = auth_register('z5555555@unsw.edu.au', 'password')
    #i think this is a mistake -will throw exception
    login = auth_login('z555555@unsw.edu.au', 'incorrect password')
    #double check this
    assert 'token' in login
    assert auth_logout(login['token']) == {'is_success' : True}
    #invalid token - should return false assumption?
    #test if token has been invalidated

def test_valid_credentials();
    user = auth_register('z5555555@unsw.edu.au', 'password', 'first', 'last')
    assert 'u_id' in user
    assert type(user['u_id']) is string
    assert 'token' in user
    assert type(user['token']) is string
