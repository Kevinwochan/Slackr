from auth import auth_register
from channels import channels_list, channels_listall, channels_create
from error import InputError
import pytest

'''
tests:
create channel
    test - invalid token, invalid name
    test return type
    test invalid
    create private and public
    create 2 channels with the same name - error
    create channels with name too long
    create channel with empty name
channels_list
    invalid token
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
def test_channels_create():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channels_create(test_user['token'], 'name', True)
    channels_create(test_user['token'], 'name2', False)
    with pytest.raises(InputError) as e:
        channels_create(test_user['token'], 'n'*21, True)
    #assumption - creating 2 channels with the same name causes an inputerror
    with pytest.raises(InputError) as e:
        channels_create(test_user['token'], 'name', True)
    #regardless of visibility
    with pytest.raises(InputError) as e:
        channels_create(test_user['token'], 'name', False)

def test_list():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channels_list(test_user["token"]) #what should this do??

    channels_create(test_user['token'], 'name', True)
    channels_list(test_user["token"]) #what should this do??
    channels_create(test_user['token'], 'name2', True)

def test_listall():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channels_listall(test_user["token"])
