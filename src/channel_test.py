from auth import auth_register
import channel
import pytest
from error import InputError
from error import AccessError


def test_channel_join():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	channel.channel_join(test_user["token"],)
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
