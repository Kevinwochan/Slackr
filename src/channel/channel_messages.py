import pytest
from error import AccessError, InputError
from auth import auth_register
from channel import channel_invite, channel_details, channel_messages
from channels import channels_create
from message import message_send


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
    return channels_create(user_dav['token'], channel_dav, False)
    
# Test for the input error when the channel id is not valid
def test_invalid_channel_id(user_dav, channel_dav):

    # There is only one message inside the channel
    msg_1 = message_send(user_dav['token'], channel_dav['channel_id'], "message")
    
    with pytest.raises(InputError):
        assert channel_messages(user_dav['token'], 000000, 0)
    
# Test for the input error when the start is greater than the total number of 
# messages
def test_overflow(channel_dav, user_dav):
    
    # There is only one message inside the channel
    msg_1 = message_send(user_dav['token'], channel_dav['channel_id'], "message")
    
    with pytest.raises(InputError):
        assert channel_messages(user_dav['token'], channel_dav['channel_id'], 100)
        
# Test for the AccessError when the Authorised user is not a member of channel
def test_invalid_user(channel_dav, user_dav, user_chas):

    # There is only one message inside the channel
    msg_1 = message_send(user_dav['token'], channel_dav['channel_id'], "message")
    
    with pytest.raises(AccessError):
        assert channel_messages(user_chas['token'], channel_dav['channel_id'], 0)
        
# Normal test for this function
def test_channel_messages(channel_dav, user_dav):
    
    # Create couple messages
    msg_1 = message_send(user_dav['token'], channel_dav['channel_id'], "Message")
    msg_2 = message_send(user_dav['token'], channel_dav['channel_id'], "I love cs1531")
    msg_3 = message_send(user_dav['token'], channel_dav['channel_id'], "Make it")
    msg_4 = message_send(user_dav['token'], channel_dav['channel_id'], "can't do it")
    
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
