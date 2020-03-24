import pytest
from src.error import AccessError, InputError
from src.auth import auth_register, auth_logout
from src.channel import channel_invite, channel_details, channel_messages, channel_leave, channel_join
from src.channels import channels_create
from src.message import message_send

# Assumptions #
# Assuming that when you create a channel, you automatically join it as Owner
# Assuming that there isn't a Slackr Owner in these tests
# Assumes there are no existing channels or users when each test is run
# Assumes channel ids begin with id 0
# Assumes channels_details is implemented to verify members have been added/removed
# Assumes user ids begin with id 0
'''
    Tests for leaving a channel
'''


def test_channel_leave():
    test_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                              "Smith")
    test_channel = channels_create(test_user["token"], "test_channel", True)
    channel_leave(test_user["token"], test_channel["channel_id"])


# Trying to leave a channel with invalid channel ID
def test_channel_leave_invald_channel_id():
    test_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                              "Smith")
    with pytest.raises(InputError) as e:
        channel_leave(test_user["token"], 0)


# Trying to leave a channel that the user isn't in
def test_channel_leave_non_member():
    test_Owner_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                                    "Smith")
    test_normal_user = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                                     "Smith")
    test_channel = channels_create(test_Owner_user["token"], "test_channel",
                                   True)
    with pytest.raises(AccessError) as e:
        channel_leave(test_normal_user["token"], test_channel["channel_id"])


#Trying to leave a channel with invalid token (invalid after logging out)
def test_channel_leave_invalid_token():
    test_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                              "Smith")
    test_channel = channels_create(test_user["token"], "test_channel", True)
    auth_logout(test_user["token"])  # Invalidating token
    with pytest.raises(AccessError) as e:
        channel_leave(test_user["token"], test_channel["channel_id"])


'''
    Tests for joining a channel
'''


def test_channel_join():
    test_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                              "Smith")
    test_user2 = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                               "Smith")
    test_channel = channels_create(test_user["token"], "test_channel", True)
    channel_join(test_user2["token"], test_channel["channel_id"])


# Didn't create channel so channel token wouldn't exist
def test_channel_join_InputError():
    test_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                              "Smith")
    with pytest.raises(InputError) as e:
        channel_join(test_user["token"], 0)


# Trying to join a private channel
def test_channel_join_AccessError():
    test_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                              "Smith")
    test_user2 = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                               "Smith")
    test_channel = channels_create(test_user["token"], "test_channel", False)
    with pytest.raises(AccessError) as e:
        channel_join(test_user2["token"], test_channel["channel_id"])


#Trying to join with an invalid token (invalid after logging out)
def test_channel_join_InvalidToken():
    test_user = auth_register("z5555555@unsw.edu.au", "password", "John",
                              "Smith")
    test_user2 = auth_register("z8888888@unsw.edu.au", "password", "Bob",
                               "Smith")
    test_channel = channels_create(test_user2["token"], "test_channel", True)
    auth_logout(test_user["token"])  # Invalidating token of user1
    with pytest.raises(AccessError) as e:
        channel_join(test_user["token"], test_channel["channel_id"])


'''
    Test functions for inviting a user to a channel
'''


# Set up the users
@pytest.fixture
def user_dav():
    return auth_register("dav@gmail.com", "dav123", "dav", "zhu")


@pytest.fixture
def user_jas():
    return auth_register("jas@gmail.com", "jas123", "jas", "zhu")


@pytest.fixture
def user_chas():
    return auth_register("chas@gmail.com", "chas123", "chas", "zhu")


# Set up a channel created by dav
@pytest.fixture
def channel_dav(user_dav):
    return channels_create(user_dav['token'], "channel_dav", False)


# Test for invite a new member by an old member
def test_invite(user_dav, user_jas, channel_dav):
    channel_invite(user_dav['token'], channel_dav['channel_id'],
                   user_jas['u_id'])

    # create member jas
    member_jas = {}
    member_jas['u_id'] = user_jas['u_id']
    member_jas['name_first'] = "jas"
    member_jas['name_last'] = "zhu"

    # set up channel details
    channel_dav_detail = channel_details(user_dav['token'],
                                         channel_dav['channel_id'])

    assert member_jas in channel_dav_detail['all_members']


# Test for channel_id does not refer to a valid channel
def test_invalid_channel_invite(user_dav, user_jas):
    with pytest.raises(InputError):
        assert channel_invite(user_dav['token'], "invalid channel id",
                              user_jas['u_id'])


# Test for the channel_id is a valid channel but the invitor isn't a member
def test_valid_channel_invite(user_chas, user_jas, channel_dav):
    with pytest.raises(InputError):
        assert channel_invite(user_chas['token'], channel_dav['channel_id'],
                              user_jas['u_id'])


# Test for u_id does not refer to a valid user
def test_valid_u_id(user_dav, channel_dav):
    with pytest.raises(InputError):
        assert channel_invite(user_dav['token'], channel_dav['channel_id'],
                              00000)


# Test for the authorised user is not part of channel.
def test_invite_right(user_jas, user_chas, channel_dav):
    with pytest.raises(AccessError):
        assert channel_invite(user_jas['token'], channel_dav['channel_id'],
                              user_chas)


# Test if the invited member has already been invited
# This test will not be run unless the test_invite working well
def test_channel_invite_already_member(user_dav, user_jas, channel_dav):

    # First invitation
    channel_invite(user_dav['token'], channel_dav['channel_id'],
                   user_jas['u_id'])

    # Second invitation
    channel_invite(user_dav['token'], channel_dav['channel_id'],
                   user_jas['u_id'])

    # create member jas
    member_jas = {}
    member_jas['u_id'] = user_jas['u_id']
    member_jas['name_first'] = "jas"
    member_jas['name_last'] = "zhu"

    # set up channel details
    channel_dav_detail = channel_details(user_dav['token'],
                                         channel_dav['channel_id'])

    assert member_jas in channel_dav_detail['all_members']


# If the user in the channel invite himself
def test_channel_invite_self_invite(user_dav, channel_dav, user_jas):

    # invite jas to the channel
    channel_invite(user_dav['token'], channel_dav['channel_id'],
                   user_jas['u_id'])

    # jas invite himself again
    channel_invite(user_jas['token'], channel_dav['channel_id'],
                   user_jas['u_id'])

    # create member jas
    member_jas = {}
    member_jas['u_id'] = user_jas['u_id']
    member_jas['name_first'] = "jas"
    member_jas['name_last'] = "zhu"

    # set up channel details
    channel_dav_detail = channel_details(user_dav['token'],
                                         channel_dav['channel_id'])

    assert member_jas in channel_dav_detail['all_members']


# If a user invite itself to a channel where he is not a member
def test_channel_invite_not_a_mamber(user_jas, channel_dav, user_dav):

    # jas invite himself again
    channel_invite(user_jas['token'], channel_dav['channel_id'],
                   user_jas['u_id'])

    # create member jas
    member_jas = {}
    member_jas['u_id'] = user_jas['u_id']
    member_jas['name_first'] = "jas"
    member_jas['name_last'] = "zhu"

    # set up channel details
    channel_dav_detail = channel_details(user_dav['token'],
                                         channel_dav['channel_id'])

    assert member_jas not in channel_dav_detail['all_members']


# Test for the input error when the channel id is not valid
def test_channel_messages_invalid_channel_id(user_dav, channel_dav):

    # There is only one message inside the channel
    msg_1 = message_send(user_dav['token'], channel_dav['channel_id'],
                         "message")

    with pytest.raises(InputError):
        assert channel_messages(user_dav['token'], 000000, 0)


# Test for the input error when the start is greater than the total number of
# messages
def test_channel_messages_invalid_start(channel_dav, user_dav):

    # There is only one message inside the channel
    msg_1 = message_send(user_dav['token'], channel_dav['channel_id'],
                         "message")

    with pytest.raises(InputError):
        assert channel_messages(user_dav['token'], channel_dav['channel_id'],
                                100)


# Test for the AccessError when the Authorised user is not a member of channel
def test_channel_messages_invalid_user(channel_dav, user_dav, user_chas):

    # There is only one message inside the channel
    msg_1 = message_send(user_dav['token'], channel_dav['channel_id'],
                         "message")

    with pytest.raises(AccessError):
        assert channel_messages(user_chas['token'], channel_dav['channel_id'],
                                0)


# Normal test for this function
def test_channel_messages(channel_dav, user_dav):

    # Create couple messages
    msg_1 = message_send(user_dav['token'], channel_dav['channel_id'],
                         "Message")
    msg_2 = message_send(user_dav['token'], channel_dav['channel_id'],
                         "I love cs1531")
    msg_3 = message_send(user_dav['token'], channel_dav['channel_id'],
                         "Make it")
    msg_4 = message_send(user_dav['token'], channel_dav['channel_id'],
                         "can't do it")

    # Create the dictionary of each message
    # Assume the time_created are all the same "12345"
    msg_1_card = {}
    msg_1_card['message_id'] = msg_1['message_id']
    msg_1_card['u_id'] = user_dav['u_id']
    msg_1_card['message'] = "Message"
    msg_1_card['time_created'] = 12345

    msg_2_card = {}
    msg_2_card['message_id'] = msg_2['message_id']
    msg_2_card['u_id'] = user_dav['u_id']
    msg_2_card['message'] = "I love cs1531"
    msg_2_card['time_created'] = 12345

    msg_3_card = {}
    msg_3_card['message_id'] = msg_3['message_id']
    msg_3_card['u_id'] = user_dav['u_id']
    msg_3_card['message'] = "Make it"
    msg_3_card['time_created'] = 12345

    msg_4_card = {}
    msg_4_card['message_id'] = msg_4['message_id']
    msg_4_card['u_id'] = user_dav['u_id']
    msg_4_card['message'] = "can't do it"
    msg_4_card['time_created'] = 12345

    # Test 0
    # When the start index is 0
    test_0 = channel_messages(user_dav['token'], channel_dav['channel_id'], 0)

    assert test_0['start'] == 0
    assert test_0['end'] == 50
    assert msg_1_card in test_0['messages']
    assert msg_2_card in test_0['messages']
    assert msg_3_card in test_0['messages']
    assert msg_4_card in test_0['messages']

    # Test 1
    # When the start index is 1
    test_1 = channel_messages(user_dav['token'], channel_dav['channel_id'], 1)

    assert test_1['start'] == 1
    assert test_1['end'] == 51
    assert msg_1_card in test_1['messages']
    assert msg_2_card in test_1['messages']
    assert msg_3_card in test_1['messages']
    assert msg_4_card in test_1['messages']


"""
    Assume the owner of a channel can only be one person
"""


# Normal test for the channel_details
def test_channel_details(user_chas, user_dav, user_jas, channel_dav):

    # Invite jas and chas to the channel
    channel_invite(user_dav['token'], channel_dav['channel_id'],
                   user_jas['u_id'])
    channel_invite(user_dav['token'], channel_dav['channel_id'],
                   user_chas['u_id'])

    # Achieve the detail of the channel by dev
    channel_dav_detail = channel_details(user_dav['token'],
                                         channel_dav['channel_id'])

    # Set up the member card for every member
    member_dav = {}
    member_dav['u_id'] = user_dav['u_id']
    member_dav['name_first'] = "dav"
    member_dav['name_last'] = "zhu"

    member_jas = {}
    member_jas['u_id'] = user_jas['u_id']
    member_jas['name_first'] = "jas"
    member_jas['name_last'] = "zhu"

    member_chas = {}
    member_chas['u_id'] = user_chas['u_id']
    member_chas['name_first'] = "chas"
    member_chas['name_last'] = "zhu"

    assert channel_dav_detail['name'] == "dav"
    assert channel_dav_detail['owner_members'][0] == member_dav
    assert member_chas in channel_dav_detail['all_members']
    assert member_dav in channel_dav_detail['all_members']
    assert member_jas in channel_dav_detail['all_members']


# Test for the InputError
def test_invalid_channel(user_dav):
    with pytest.raises(InputError):
        assert channel_details(user_dav['token'], 000000)


# Test for the AccessError
def test_invalid_member(user_chas, channel_dav):
    with pytest.raises(AccessError):
        assert channel_details(user_chas['token'], channel_dav['channel_id'])
