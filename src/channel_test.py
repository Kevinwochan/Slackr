from auth import auth_register
import channel
import pytest
from channels import channels_create
from error import InputError
from error import AccessError


def test_channel_join():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_channel = channels_create(test_user["token"], "test_channel", true)
	channel.channel_join(test_user["token"],test_channel["channel_id"])
	pass

# Assumption that first person to join a channel is Owner of that channel
def test_channel_addowner():
	pass

def test_channel_removeowner():
	pass

def test_channel_join_InputError():
	pass

def test_channel_addowner_InputError():
	pass

def test_channel_remove_InputError():
	pass

def test_channel_join_AccessError():
	pass

def test_channel_addowner_AccessError():
	pass

def test_channel_removeowner_AccessError():
	pass
