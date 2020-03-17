import pytest

from src.error import AccessError, InputError
from src.auth import auth_register
from src.channel import channel_messages
from src.channels import channels_list, channels_create
from src.other import search, users_all
from src.message import message_send
from src.user import user_profile
"""
To test the search function, A user with name "Andrew" is created. Then Two
channels are created named "channel_1" and "channel_2" respectively. Afterwards,
Three messages are sent with one in chanenl_1 and two in channel_2. And a query_str
which is "love" is set and only two messages are qualified. Here the assumption 
of time is that the created time are all the same since the channel_messages function
isn't implemented so the created time can not be gotten.

"""


def test_search_with_invalid_token():
    ''''searching as an unathorised user (invalid token) throws an access error'''
    with pytest.raises(AccessError):
        search('invalid token', 'love')


def test_search_with_empty_query_string():
    '''searching with an empty query string throws an input error'''
    andrew = auth_register("andrewt@gmail.com", "password", "andrew", "taylor")
    with pytest.raises(InputError):
        search(andrew['token'], '')


def test_search_for_one_message():
    '''searching with valid paramters and checking the returned object is correct'''
    andrew = auth_register("andrewt@gmail.com", "password", "andrew", "taylor")
    new_channel = channels_create(andrew['token'], "channel_1", True)
    new_message = message_send(andrew['token'], new_channel['channel_id'],
                               f'this is a test message')

    search_results = search(andrew['token'], 'test message')
    assert isinstance(search_results, dict)
    assert len(search_results['messages']) == 1
    message = search_results['messages'][0]
    assert isinstance(message, dict)
    assert 'mesage_id' in message
    assert isinstance(message['message_id'], int)
    assert message['message_id'] == new_message['message_id']
    assert 'u_id' in message
    assert isinstance(message['u_id'], int)
    assert 'message' in message
    assert isinstance(message['message'], int)
    assert 'time_created' in message
    assert isinstance(message['time_created'], str)


def test_search_for_multiple_messages():
    '''searching with valid paramters and checking the returned object is correct
        messages_sent is a dictionary of message_ids as keys the message_content as
        the value. This is used to verify that the messages found match the messages
        that were sent.
    '''
    andrew = auth_register("andrewt@gmail.com", "password", "andrew", "taylor")
    new_channel = channels_create(andrew['token'], "channel_1", True)

    messages_sent = {}
    for message_number in range(1, 10):
        message_content = f'this is message number {message_number}'
        new_message_id = message_send(andrew['token'],
                                      new_channel['channel_id'],
                                      message_content)['message_id']
        messages_sent[new_message_id] = message_content

    search_results = search(andrew['token'], 'this is message number')
    assert isinstance(search_results, dict)
    assert len(search_results['messages']) == 10
    for message in search_results['messages']:
        assert isinstance(message, dict)
        assert 'mesage_id' in message
        assert isinstance(message['message_id'], int)
        assert 'u_id' in message
        assert isinstance(message['u_id'], int)
        assert 'message' in message
        assert isinstance(message['message'], int)
        assert messages_sent[message['message_id']] == message
        assert 'time_created' in message
        assert isinstance(message['time_created'], str)


def test_searching_multiple_channels():
    '''search should find all messages containing the query string regardless of channel'''
    andrew = auth_register("andrewt@gmail.com", "password", "andrew", "taylor")
    new_channel_a = channels_create(andrew['token'], "channel_a", True)
    new_channel_b = channels_create(andrew['token'], "channel_b", True)
    message_send(andrew['token'], new_channel_a['channel_id'],
                 f'this is a test message in channel a')
    message_send(andrew['token'], new_channel_b['channel_id'],
                 f'this is a test message in channel b')
    search_results = search(andrew['token'], 'this is a test message')
    assert isinstance(search_results, dict)
    assert len(search_results['messages']) == 2


def test_searching_multiple_channels_with_no_access():
    '''search should find all messages containing the query string THAT THE USER HAS ACCESS TO'''
    andrew = auth_register("andrewt@gmail.com", "password", "andrew", "taylor")
    andrews_channel = channels_create(andrew['token'], "andrews channel",
                                      False)
    message_send(andrew['token'], andrews_channel['channel_id'],
                 'this is a test message in andrews channel')

    john = auth_register("john@gmail.com", "password", "john", "smith")
    johns_channel = channels_create(john['token'], "channel_b", False)
    message_send(andrew['token'], johns_channel['channel_id'],
                 'this is a test message in johns channel')

    andrews_search_results = search(andrew['token'], 'this is a test message')
    assert isinstance(andrews_search_results, dict)
    assert len(andrews_search_results['messages']) == 1

    johns_search_results = search(john['token'], 'this is a test message')
    assert isinstance(johns_search_results, dict)
    assert len(johns_search_results['messages']) == 1


def test_search_normal_use_case():
    # Set up a user
    andrew = auth_register("andrewt@gmail.com", "password", "andrew", "taylor")

    # Create a new channel
    channel_1 = channels_create(andrew['token'], "channel_1", False)
    channel_2 = channels_create(andrew['token'], "channel_2", False)

    # Send the message
    msg_1 = message_send(andrew['token'], channel_1['channel_id'],
                         "I love cs1531")
    msg_2 = message_send(andrew['token'], channel_2['channel_id'],
                         "Happy bd I")
    msg_3 = message_send(andrew['token'], channel_2['channel_id'],
                         "I love SAMYANG")

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


def test_users_all_with_invalid_token():
    ''''Get the users info by an unathorised user (invalid token) throws an access error'''
    with pytest.raises(AccessError):
        users_all("invalid token")


# Normal
def normal_test():
    # set up the user
    user_andrew = auth_register("andrewt@gmail.com", "password", "andrew",
                                "taylor")
    user_chris = auth_register("chrisc@gmail.com", "pilot", "chris", "chen")

    # Access the users info by andrew's token
    users_card = users_all(user_andrew['token'])

    # To get the handle_str of each user
    andrew_profile = user_profile(user_andrew['token'], user_andrew['u_id'])
    chris_profile = user_profile(user_chris['token'], user_chris['u_id'])

    # andrew's expected info
    andrew_card = {}
    andrew_card['u_id'] = user_andrew['u_id']
    andrew_card['email'] = "andrewt@gmail.com"
    andrew_card['name_first'] = "andrew"
    andrew_card['name_last'] = "zhu"
    andrew_card['handle_str'] = andrew_profile['user']['handle_str']

    # chris's expected info
    chris_card = {}
    chris_card['u_id'] = user_chris['u_id']
    chris_card['email'] = "chrisc@gmail.com"
    chris_card['name_first'] = "chris"
    chris_card['name_last'] = "zhu"
    chris_card['handle_str'] = chris_profile['user']['handle_str']

    assert andrew_card in users_card['users']
    assert chris_card in users_card['users']
