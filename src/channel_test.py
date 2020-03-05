from auth import auth_register
import channel
import pytest
from channels import channels_create
from error import InputError
from error import AccessError

# Keeping passes until all tests are done and working

def test_channel_join():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_channel = channels_create(test_user["token"], "test_channel", True)
	channel.channel_join(test_user["token"],test_channel["channel_id"])

	pass

# Assumption that first person to join a channel is Owner of that channel
def test_channel_addowner():
	pass

def test_channel_removeowner():
	pass

# Didn't create channel so channel token wouldn't exist
def test_channel_join_InputError():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	with pytest.raises(InputError) as e:
		channel.channel_join(test_user["token"],non_existent_channel["channel_id"])

	pass

def test_channel_addowner_InputError():
	pass

def test_channel_remove_InputError():
	pass

def test_channel_join_AccessError():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_user2 = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_channel = channels_create(test_user2["token"], "test_channel", False)
	with pytest.raises(AccessError) as e:
		channel.channel_join(test_user["token"],test_channel["channel_id"])
		
	pass

def test_channel_addowner_AccessError():
	pass

def test_channel_removeowner_AccessError():
	pass
