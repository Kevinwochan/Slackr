from auth import auth_register
from channels import channels_list, channels_listall, channels_create
from error import InputError
import pytest



def test_list():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channels_list(test_user["token"])

def test_listall():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channels_listall(test_user["token"])

def test_channels_create():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channels_create(test_user['token'], 'name', True)

    with pytest.raises(InputError) as e:
        channels_create(test_user['token'], 'n'*21, True)
