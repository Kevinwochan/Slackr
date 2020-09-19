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
    messages = search(andrew['token'], '')['messages']
    assert len(messages) == 0


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
    assert 'message_id' in message
    assert isinstance(message['message_id'], int)
    assert message['message_id'] == new_message['message_id']
    assert 'u_id' in message
    assert isinstance(message['u_id'], int)
    assert 'message' in message
    assert isinstance(message['message'], str)
    assert 'time_created' in message
    assert isinstance(message['time_created'], int)


def test_search_for_multiple_messages():
    '''searching with valid paramters and checking the returned object is correct
        messages_sent is a dictionary of message_ids as keys the message_content as
        the value. This is used to verify that the messages found match the messages
        that were sent.
    '''
    andrew = auth_register("andrewt@gmail.com", "password", "andrew", "taylor")
    new_channel = channels_create(andrew['token'], "channel_1", True)

    messages_sent = {}
    for message_number in range(10):
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
        assert 'message_id' in message
        assert isinstance(message['message_id'], int)
        assert 'u_id' in message
        assert isinstance(message['u_id'], int)
        assert 'message' in message
        assert isinstance(message['message'], str)
        assert message['message'] == messages_sent[message['message_id']]
        assert 'time_created' in message
        assert isinstance(message['time_created'], int)


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
    message_send(john['token'], johns_channel['channel_id'],
                 'this is a test message in johns channel')

    andrews_search_results = search(andrew['token'], 'this is a test message')
    assert isinstance(andrews_search_results, dict)
    assert len(andrews_search_results['messages']) == 1

    johns_search_results = search(john['token'], 'this is a test message')
    assert isinstance(johns_search_results, dict)
    assert len(johns_search_results['messages']) == 1


def test_users_all_with_invalid_token():
    ''''Get the users info by an unathorised user (invalid token) throws an access error'''
    with pytest.raises(AccessError):
        users_all("invalid token")


# Normal
def test_users_all_normal_test():
    # set up the user
    user_andrew = auth_register("andrewt@gmail.com", "password", "andrew",
                                "taylor")
    user_chris = auth_register("chrisc@gmail.com", "pilotpassword", "chris",
                               "chen")

    # Access the users info by andrew's token
    users = users_all(user_andrew['token'])['users']

    assert len(users) == 2

    for user in users:
        if user['u_id'] == user_andrew['u_id']:
            assert user['email'] == "andrewt@gmail.com"
            assert user['name_first'] == "andrew"
            assert user['name_last'] == "taylor"
        else:
            assert user['email'] == "chrisc@gmail.com"
            assert user['name_first'] == "chris"
            assert user['name_last'] == "chen"
