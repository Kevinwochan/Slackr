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
    msg_2 = message_send(andrew['token'], channel_2['channel_id'], "Happy bd")
    msg_3 = message_send(andrew['token'], channel_2['channel_id'], "I love SAMYANG")
    
    # A simple query_str for test
    query_str = "love"
    
    # Set up the expected dictionary
    list_expected = {}
    
    # First message
    list_expected['messages'] = []
    list_expected['messages'].append({})
    list_expected['messages'][0]['message_id'] = msg_1['message_id']
    list_expected['messages'][0]['u_id'] = andrew['u_id']
    list_expected['messages'][0]['message'] = "I love cs1531"
    list_expected['messages'][0]['time_created'] = 12345
    
    # Second message matched the query_str
    list_expected['messages'].append({})
    list_expected['messages'][1]['message_id'] = msg_3['message_id']
    list_expected['messages'][1]['u_id'] = andrew['u_id']
    list_expected['messages'][1]['message'] = "I love SAMYANG"
    list_expected['messages'][1]['time_created'] = 12345
    
    assert search(andrew['token'], query_str) == list_expected
         
        
    
    
    
         
        
    
    
    
