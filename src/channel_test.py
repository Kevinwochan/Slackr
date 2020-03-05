from auth import auth_register
import channel
import pytest
from channels import channels_create
from error import InputError
from error import AccessError


def test_channel_join():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_channel = channels_create(test_user["token"], "test_channel", True)
	channel.channel_join(test_user["token"],test_channel["channel_id"])


# Assumption that first person to join/create a channel is Owner of that channel
def test_channel_addowner():
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	channel.channel_addowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])

# Assumption that first person to join/create a channel is Owner of that channel
def test_channel_removeowner():
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	channel.channel_addowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])
	channel.channel_removeowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])
	

# Didn't create channel so channel token wouldn't exist
def test_channel_join_InputError():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	with pytest.raises(InputError) as e:
		channel.channel_join(test_user["token"],non_existent_channel["channel_id"])


# Two input errors. Not valid channel id  & already owner
def test_channel_addowner_InputError(): 
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	with pytest.raises(InputError) as e:
		channel.channel_addowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])

	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	channel.channel_addowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])
	with pytest.raises(InputError) as e:
		channel.channel_addowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])


# Two input errors. Not valid channel id & not owner
def test_channel_removeowner_InputError(): 
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	with pytest.raises(InputError) as e:
		channel.channel_removeowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])

	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	with pytest.raises(InputError) as e:
		channel.channel_addowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])
	
# Trying to join a private channel
def test_channel_join_AccessError():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_user2 = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_channel = channels_create(test_user2["token"], "test_channel", False)
	with pytest.raises(AccessError) as e:
		channel.channel_join(test_user["token"],test_channel["channel_id"])

# Assuming there isn't a Slackr owner
def test_channel_addowner_AccessError():
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_normal_user2 = auth_register("z9999999@unsw.edu.au","password", "Sam", "Smith") 
	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	with pytest.raises(AccessError) as e:
		channel.channel_addowner(test_normal_user["token"], test_channel["channel_id"], test_normal_user2["u_id"])

# Assuming there isn't a Slaer owner
def test_channel_removeowner_AccessError():
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_normal_user2 = auth_register("z9999999@unsw.edu.au","password", "Sam", "Smith") 
	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	with pytest.raises(AccessError) as e:
		channel.channel_removeowner(test_normal_user["token"], test_channel["channel_id"], test_normal_user2["u_id"])

