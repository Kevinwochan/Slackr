from auth import auth_register
from channels import channels_list, channels_listall, channels_create
from error import InputError
import pytest

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
