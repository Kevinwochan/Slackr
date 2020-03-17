import pytest
from src.error import AccessError, InputError
from src.auth import auth_register, auth_logout
from src.channels import channel_invite, channel_details, channel_messages, channel_leave, channel_addowner, channel_join
from src.channels import channels_create
from message import message_send

'''
    Tests for adding an owner to a channel
'''
# Assumption that first person to join/create a channel is Owner of that channel
def test_channel_addowner():
    test_Owner_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                                    "Smith")
    test_normal_user = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                                     "Smith")
    test_channel = channels_create(test_Owner_user["token"], "test_channel",
                                   True)
    channel_join(test_normal_user["token"], test_channel["channel_id"])
    channel_addowner(test_Owner_user["token"],
                             test_channel["channel_id"],
                             test_normal_user["u_id"])


# Two input errors. Not valid channel id  & already owner
def test_channel_addowner_InputError_invalid_channel():
    test_Owner_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                                    "Smith")
    test_normal_user = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                                     "Smith")
    with pytest.raises(InputError) as e:
        channel_addowner(test_Owner_user["token"], 0,
                                 test_normal_user["u_id"])


def test_channel_addowner_InputError_user_already_owner():
    test_Owner_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                                    "Smith")
    test_normal_user = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                                     "Smith")
    test_channel = channels_create(test_Owner_user["token"], "test_channel",
                                   True)
    channel_join(test_normal_user["token"], test_channel["channel_id"])
    channel_addowner(test_Owner_user["token"],
                             test_channel["channel_id"],
                             test_normal_user["u_id"])
    with pytest.raises(InputError) as e:
        channel_addowner(test_Owner_user["token"],
                                 test_channel["channel_id"],
                                 test_normal_user["u_id"])


def test_channel_addowner_InputError_invalid_user():
    test_Owner_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                                    "Smith")
    test_channel = channels_create(test_Owner_user["token"], "test_channel",
                                   True)
    with pytest.raises(InputError) as e:
        channel_addowner(test_Owner_user["token"],
                                 test_channel["channel_id"], 1)


# Assuming there isn't a Slackr owner
def test_channel_addowner_AccessError():
    test_Owner_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                                    "Smith")
    test_normal_user = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                                     "Smith")
    test_normal_user2 = auth_register("z9999999@unsw.edu.au", "password",
                                      "Sam", "Smith")
    test_channel = channels_create(test_Owner_user["token"], "test_channel",
                                   True)
    channel_join(test_normal_user["token"], test_channel["channel_id"])
    channel_join(test_normal_user2["token"],
                         test_channel["channel_id"])
    with pytest.raises(AccessError) as e:
        channel_addowner(test_normal_user["token"],
                                 test_channel["channel_id"],
                                 test_normal_user2["u_id"])


# Trying to add owner to normal user with an invalid token (invalid after logging out)
def test_channel_addowner_InvalidToken():
    test_Owner_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                                    "Smith")
    test_normal_user = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                                     "Smith")
    test_channel = channels_create(test_Owner_user["token"], "test_channel",
                                   True)
    channel_join(test_normal_user["token"], test_channel["channel_id"])
    auth_logout(test_normal_user["token"])  # Invalidating token of normal user
    with pytest.raises(AccessError) as e:
        channel_addowner(test_Owner_user["token"],
                                 test_channel["channel_id"],
                                 test_normal_user["u_id"])


'''
    Tests for removing an owner from a channel
'''
# Assumption that first person to join/create a channel is Owner of that channel
def test_channel_removeowner():
    test_Owner_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                                    "Smith")
    test_normal_user = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                                     "Smith")
    test_channel = channels_create(test_Owner_user["token"], "test_channel",
                                   True)
    channel_join(test_normal_user["token"], test_channel["channel_id"])
    channel_addowner(test_Owner_user["token"],
                             test_channel["channel_id"],
                             test_normal_user["u_id"])
    channel_removeowner(test_Owner_user["token"],
                                test_channel["channel_id"],
                                test_normal_user["u_id"])


# Two input errors. Not valid channel id & not owner
def test_channel_removeowner_InputError_invalid_user():
    test_Owner_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                                    "Smith")
    test_normal_user = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                                     "Smith")
    with pytest.raises(InputError) as e:
        channel_removeowner(test_Owner_user["token"], 0,
                                    test_normal_user["u_id"])


def test_channel_removeowner_InputError_invalid_channel():
    test_Owner_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                                    "Smith")
    test_normal_user = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                                     "Smith")
    test_channel = channels_create(test_Owner_user["token"], "test_channel",
                                   True)
    channel_join(test_normal_user["token"], test_channel["channel_id"])
    with pytest.raises(InputError) as e:
        channel_addowner(test_Owner_user["token"],
                                 test_channel["channel_id"],
                                 test_normal_user["u_id"])


# Assuming there isn't a Slackr owner
def test_channel_removeowner_AccessError():
    test_Owner_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                                    "Smith")
    test_normal_user = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                                     "Smith")
    test_normal_user2 = auth_register("z9999999@unsw.edu.au", "password",
                                      "Sam", "Smith")
    test_channel = channels_create(test_Owner_user["token"], "test_channel",
                                   True)
    channel_join(test_normal_user["token"], test_channel["channel_id"])
    channel_join(test_normal_user2["token"],
                         test_channel["channel_id"])
    with pytest.raises(AccessError) as e:
        channel_removeowner(test_normal_user["token"],
                                    test_channel["channel_id"],
                                    test_normal_user2["u_id"])


# Trying to remove an owner with an invalid token (invalid after logging out)
def test_channel_removeowner_InvalidToken():
    test_Owner_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                                    "Smith")
    test_normal_user = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                                     "Smith")
    test_channel = channels_create(test_Owner_user["token"], "test_channel",
                                   True)
    channel_join(test_normal_user["token"], test_channel["channel_id"])
    auth_logout(test_normal_user["token"])  # Invalidating token of normal user
    with pytest.raises(AccessError) as e:
        channel_removeowner(test_Owner_user["token"],
                                    test_channel["channel_id"],
                                    test_normal_user["u_id"])
