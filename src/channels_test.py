from auth import auth_register, auth_logout
from channels import channels_list, channels_listall, channels_create
from error import InputError, AccessError
import pytest
#Assumption: channels_test.py assumes that auth_register, auth_logout have been tested

'''
channels_list
    create channels
    list channels
    check return type
    create another user, - list and check that dic channel isnt test_channels_create
    2nd user should not be able to list first channel by default - not a member yet
    create 2 channels and check
    default? - willl there already be channels?
channels_listall
    invalid token
    create channel as one user
    create 2nd channel as other user
        check list is not the same
    check listall is the same (is this an assumption)
    create private channel- check listall doesnt change
'''

################################################################################
##                         ||Tests: channels_create||                         ##
################################################################################
def test_chan_create_invalid_name():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")

    with pytest.raises(InputError) as e:
        channels_create(test_user['token'], 'n'*21, True)
    #Assumption: channels_create raises an InputError if given empty name
    with pytest.raises(InputError) as e:
        channels_create(test_user['token'], '', True)

# Checking that passing an invalid token raises AccessError
def test_chan_create_invalid_token():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    token = test_user['token']
    assert auth_logout(token) #invalidating token
    with pytest.raises(AccessError) as e:
        auth_logout(token) #confirming that token is an invalid token

    with pytest.raises(AccessError) as e:
        channels_create(token, 'name', True)

# Passing channels_create() Valid parametres and checking no errors are raised
def test_chan_create_valid():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channels_create(test_user['token'], 'name', True)
    channels_create(test_user['token'], 'name2', False)

def test_chan_create_return():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    chan1 = channels_create(test_user['token'], 'name', True)
    assert type(chan1) == dict
    assert 'channel_id' in chan1

# Creating 2+ channels with the same name and checking no errors are raised
#Assumption: 2 or more channels can be created with the same name - they will have to be differentiated by channel_id alone
def test_chan_create_double():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    chan1 = channels_create(test_user['token'], 'name', True)
    chan2 = channels_create(test_user['token'], 'name', False)
    chan3 = hannels_create(test_user['token'], 'name', True)
    # Checking that channel_id's are unique
    assert chan1['channel_id'] != chan2['channel_id']
    assert chan1['channel_id'] != chan3['channel_id']

################################################################################
##                          ||Tests: channels_list||                          ##
################################################################################
def test_list_invalid_token():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    token = test_user['token']
    assert auth_logout(token) #invalidating token
    with pytest.raises(AccessError) as e:
        channels_list(token)

def

def test_list():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channels_list(test_user["token"]) #what should this do??

    channels_create(test_user['token'], 'name', True)
    channels_list(test_user["token"]) #what should this do??
    channels_create(test_user['token'], 'name2', True)

################################################################################
##                          ||Tests: channels_listall||                       ##
################################################################################

def test_listall():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channels_listall(test_user["token"])
