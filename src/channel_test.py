from auth import auth_register, auth_logout
import channel
import pytest
from channels import channels_create
from error import InputError
from error import AccessError

# Assumptions #
# Assuming that when you create a channel, you automatically join it as Owner
# Assuming that there isn't a Slackr Owner in these tests

##############################
#channel_leave test functions#
##############################


def test_channel_leave():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_channel = channels_create(test_user["token"], "test_channel", True)
	channel.channel_leave(test_user["token"],test_channel["channel_id"])


# Trying to leave a channel with invalid channel ID
def test_channel_leave_InputError():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_channel = channels_create(test_user["token"], "test_channel", True)
	with pytest.raises(InputError) as e:
		channel.channel_leave(test_user["token"],nonexistant_channel["channel_id"])


# Trying to leave a channel that the user isn't in
def test_channel_leave_AccessError():
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	with pytest.raises(AccessError) as e:
		channel.channel_leave(test_normal_user["token"],test_channel["channel_id"])


#Trying to leave a channel with invalid token (invalid after logging out)
def test_channel_leave_InvalidToken():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_channel = channels_create(test_user["token"], "test_channel", True)
	auth_logout(test_user["token"]) # Invalidating token
	with pytest.raises(AccessError) as e:
		channel.channel_leave(test_user["token"],test_channel["channel_id"])

#############################
#channel_join test functions#
#############################


def test_channel_join():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_user2 = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_channel = channels_create(test_user["token"], "test_channel", True)
	channel.channel_join(test_user2["token"],test_channel["channel_id"])


# Didn't create channel so channel token wouldn't exist
def test_channel_join_InputError():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	with pytest.raises(InputError) as e:
		channel.channel_join(test_user["token"],non_existent_channel["channel_id"])


# Trying to join a private channel
def test_channel_join_AccessError():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_user2 = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_channel = channels_create(test_user2["token"], "test_channel", False)
	with pytest.raises(AccessError) as e:
		channel.channel_join(test_user["token"],test_channel["channel_id"])


#Trying to join with an invalid token (invalid after logging out)
def test_channel_join_InvalidToken():
	test_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_user2 = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_channel = channels_create(test_user2["token"], "test_channel", True)
	auth_logout(test_user["token"]) # Invalidating token of user1
	with pytest.raises(AccessError) as e:
		channel.channel_join(test_user["token"],test_channel["channel_id"])


#################################
#channel_addowner test functions#
#################################


# Assumption that first person to join/create a channel is Owner of that channel
def test_channel_addowner():
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	channel.channel_join(test_normal_user["token"],test_channel["channel_id"])
	channel.channel_addowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])


# Two input errors. Not valid channel id  & already owner
def test_channel_addowner_InputError(): 
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	with pytest.raises(InputError) as e:
		channel.channel_addowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])

	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	channel.channel_join(test_normal_user["token"],test_channel["channel_id"])
	channel.channel_addowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])
	with pytest.raises(InputError) as e:
		channel.channel_addowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])


# Assuming there isn't a Slackr owner
def test_channel_addowner_AccessError():
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_normal_user2 = auth_register("z9999999@unsw.edu.au","password", "Sam", "Smith") 
	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	channel.channel_join(test_normal_user["token"],test_channel["channel_id"])
	channel.channel_join(test_normal_user2["token"],test_channel["channel_id"])
	with pytest.raises(AccessError) as e:
		channel.channel_addowner(test_normal_user["token"], test_channel["channel_id"], test_normal_user2["u_id"])


# Trying to add owner to normal user with an invalid token (invalid after logging out)
def test_channel_addowner_InvalidToken():
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	channel.channel_join(test_normal_user["token"],test_channel["channel_id"])
	auth_logout(test_normal_user["token"]) # Invalidating token of normal user
	with pytest.raises(AccessError) as e:
		channel.channel_addowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])


####################################
#channel_removeowner test functions#
####################################


# Assumption that first person to join/create a channel is Owner of that channel
def test_channel_removeowner():
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	channel.channel_join(test_normal_user["token"],test_channel["channel_id"])
	channel.channel_addowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])
	channel.channel_removeowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])
	

# Two input errors. Not valid channel id & not owner
def test_channel_removeowner_InputError(): 
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	with pytest.raises(InputError) as e:
		channel.channel_removeowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])

	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	channel.channel_join(test_normal_user["token"],test_channel["channel_id"])
	with pytest.raises(InputError) as e:
		channel.channel_addowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])


# Assuming there isn't a Slackr owner
def test_channel_removeowner_AccessError():
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_normal_user2 = auth_register("z9999999@unsw.edu.au","password", "Sam", "Smith") 
	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	channel.channel_join(test_normal_user["token"],test_channel["channel_id"])
	channel.channel_join(test_normal_user2["token"],test_channel["channel_id"])
	with pytest.raises(AccessError) as e:
		channel.channel_removeowner(test_normal_user["token"], test_channel["channel_id"], test_normal_user2["u_id"])


# Trying to remove an owner with an invalid token (invalid after logging out)
def test_channel_removeowner_InvalidToken():
	test_Owner_user = auth_register("z5555555@unsw.edu.au","password", "John", "Smith") 
	test_normal_user = auth_register("z8888888@unsw.edu.au","password", "Bob", "Smith") 
	test_channel = channels_create(test_Owner_user["token"], "test_channel", True)
	channel.channel_join(test_normal_user["token"],test_channel["channel_id"])
	auth_logout(test_normal_user["token"]) # Invalidating token of normal user
	with pytest.raises(AccessError) as e:
		channel.channel_removeowner(test_Owner_user["token"], test_channel["channel_id"], test_normal_user["u_id"])