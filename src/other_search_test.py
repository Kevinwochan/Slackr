import pytest
from channel import channel_messages
from channels import channels_list
from channel import channel_messages
from other import search
from auth import auth_register
from channels import channels_create
from message import message_send

"""
To test the search function, A user with name "Andrew" is created. Then Two
channels are created named "channel_1" and "channel_2" respectively. Afterwards,
Three messages are sent with one in chanenl_1 and two in channel_2. And a query_str
which is "love" is set and only two messages are qualified. Here the assumption 
of time is that the created time are all the same since the channel_messages function
isn't implemented so the created time can not be gotten.

"""

def test_search():
    # Set up a user
    andrew = auth_register("andrewt@gmail.com", "password", "andrew", "taylor")
    
    # Create a new channel
    channel_1 = channels_create(andrew['token'], "channel_1", False)
    channel_2 = channels_create(andrew['token'], "channel_2", False)

    # Send the message
    msg_1 = message_send(andrew['token'], channel_1['channel_id'], "I love cs1531")
    msg_2 = message_send(andrew['token'], channel_2['channel_id'], "Happy bd I")
    msg_3 = message_send(andrew['token'], channel_2['channel_id'], "I love SAMYANG")
    
    # Set up the expected dictionary
    # First message
    msg_1_card = {}
    msg_1_card['message_id'] = msg_1['message_id']
    msg_1_card['u_id'] = andrew['u_id']
    msg_1_card['message'] = "I love cs1531"
    msg_1_card['time_created'] = 12345

    # Second message
    msg_2_card = {}
    msg_2_card['message_id'] = msg_2['message_id']
    msg_2_card['u_id'] = andrew['u_id']
    msg_2_card['message'] = "Happy bd I"
    msg_2_card['time_created'] = 12345

    # Third message
    msg_3_card = {}
    msg_3_card['message_id'] = msg_3['message_id']
    msg_3_card['u_id'] = andrew['u_id']
    msg_3_card['message'] = "I love SAMYANG"
    msg_3_card['time_created'] = 12345

    # Test 1 when only two message matched
    query_str_1 = "love"
    test_1 = search(andrew['token'], query_str_1)
    assert msg_1_card in test_1['messages']
    assert msg_3_card in test_1['messages']

    # Test 2 when all of messages matched
    query_str_2 = "I"
    test_2 = search(andrew['token'], query_str_2)
    assert msg_1_card in test_2['messages']
    assert msg_2_card in test_2['messages']
    assert msg_3_card in test_2['messages']

    # Test 3 when none of message matched
    query_str_3 = "no_matched"
    test_3 = search(andrew['token'], query_str_3)
    assert msg_1_card not in test_3['messages']
    assert msg_2_card not in test_3['messages']
    assert msg_3_card not in test_3['messages']
