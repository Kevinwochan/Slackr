from auth import auth_register, auth_logout
from channels import channels_list, channels_listall, channels_create
from error import InputError, AccessError
import pytest
#Assumption: channels_test.py assumes that auth_register, auth_logout have been tested

################################################################################
##                         ||Tests: channels_create||                         ##
################################################################################
def test_chan_create_invalid_name():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")

    with pytest.raises(InputError) as e:
        channels_create(test_user['token'], 'n'*21, True)
    #Assumption: channels_create raises an InputError if given empty name
    with pytest.raises(InputError) as e:
        channels_create(test_user['token'], '', True)

# Checking that passing an invalid token raises AccessError
def test_chan_create_invalid_token():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    token = test_user['token']
    assert auth_logout(token) #invalidating token
    with pytest.raises(AccessError) as e:
        auth_logout(token) #confirming that token is an invalid token

    with pytest.raises(AccessError) as e:
        channels_create(token, 'name', True)

# Passing channels_create() Valid parametres and checking no errors are raised
def test_chan_create_valid():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channels_create(test_user['token'], 'name', True)
    channels_create(test_user['token'], 'name2', False)

def test_chan_create_return():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    chan1 = channels_create(test_user['token'], 'name', True)
    assert type(chan1) == dict
    assert 'channel_id' in chan1.keys()
    assert type(chan1['channel_id']) == int

# Creating 2+ channels with the same name and checking no errors are raised
#Assumption: 2 or more channels can be created with the same name - they will have to be differentiated by channel_id alone
def test_chan_create_double():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    chan1 = channels_create(test_user['token'], 'name', True)
    chan2 = channels_create(test_user['token'], 'name', False)
    chan3 = channels_create(test_user['token'], 'name', True)
    # Checking that channel_id's are unique
    assert chan1['channel_id'] != chan2['channel_id']
    assert chan1['channel_id'] != chan3['channel_id']

################################################################################
##                          ||Tests: channels_list||                          ##
################################################################################
def test_list_invalid_token():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    token = test_user['token']
    assert auth_logout(token) #invalidating token
    with pytest.raises(AccessError) as e:
        channels_list(token)

#Assumption: channels_list will return an empty list (in a dictionary) if there are no existing channels
def test_list_return_empty():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channels = channels_list(test_user['token'])
    assert type(channels) == dict
    assert 'channels' in channels.keys()
    assert type(channels['channels']) == list
    #No channels have been created, list should be empty
    assert len(channels['channels']) == 0

def test_list_return_one():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channel_name = 'My Channel'
    channel = channels_create(test_user['token'], channel_name, True)
    chan_lst = channels_list(test_user['token'])['channels']
    assert type(chan_lst) == list
        # One channel created. len should be 1
    assert len(chan_lst) == 1
    assert type(chan_lst[0]) == dict
    assert 'channel_id' in chan_lst[0].keys()
    assert 'name' in chan_lst[0].keys()
    # Checking that the returned details match the channel that was created
    #Assumption: channels_list lists channels in the order that the the user became a member of them
    assert channel['channel_id'] == chan_lst[0]['channel_id']
    assert channel_name == chan_lst[0]['name']

# Checking that the correct number of entries are made in the list
# and they contain the right details.
def test_list_return_two():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channel1_name = 'My Channel'
    channel2_name = 'My Second Channel'
    channel1 = channels_create(test_user['token'], channel1_name, True)
    channel2 = channels_create(test_user['token'], channel2_name, False)
    chan_lst = channels_list(test_user['token'])['channels']
    assert len(chan_lst) == 2
    channel1_details = chan_lst[0]
    channel2_details = chan_lst[1]
    assert channel1['channel_id'] == channel1_details['channel_id']
    assert channel1_name == channel1_details['name']
    # Checking that channel2's details match
    assert channel2['channel_id'] == channel2_details['channel_id']
    assert channel2_name == channel2_details['name']

def test_list_not_member():
    user1 = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channel1 = channels_create(user1['token'], "name", True)
    user2 = auth_register("secondemail@gmail.com", "1234567", "Jane", "Smith")
    chan_lst2 = channels_list(user2['token'])['channels']
    # Checking that channels_list returns an empty list for user2,
    # as they are not a member of the created channel.
    assert len(chan_lst2) == 0


################################################################################
##                          ||Tests: channels_listall||                       ##
################################################################################
# Most of the functionality of channels_listall is the same as channels_list,
# so the following tests are idendical to the tests for channels_list.
def test_listall_invalid_token():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    token = test_user['token']
    assert auth_logout(token) #invalidating token
    with pytest.raises(AccessError) as e:
        channels_listall(token)

#Assumption: channels_listall() will return an empty list (in a dictionary) if there are no existing channels
def test_listall_return_empty():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channels = channels_listall(test_user['token'])
    assert type(channels) == dict
    assert 'channels' in channels.keys()
    assert type(channels['channels']) == list
    #No channels have been created, list should be empty
    assert len(channels['channels']) == 0

def test_listall_return_one():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channel_name = 'My Channel'
    channel = channels_create(test_user['token'], channel_name, True)
    chan_lst = channels_listall(test_user['token'])['channels']
    assert type(chan_lst) == list
        # One channel created. len should be 1
    assert len(chan_lst) == 1
    assert type(chan_lst[0]) == dict
    assert 'channel_id' in chan_lst[0].keys()
    assert 'name' in chan_lst[0].keys()
    # Checking that the returned details match the channel that was created
    #Assumption: channels_listall lists channels in the order that they are created
    assert channel['channel_id'] == chan_lst[0]['channel_id']
    assert channel_name == chan_lst[0]['name']

# Checking that the correct number of entries are made in the list
# and they contain the right details.
def test_listall_return_two():
    test_user = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channel1_name = 'My Channel'
    channel2_name = 'My Second Channel'
    channel1 = channels_create(test_user['token'], channel1_name, True)
    channel2 = channels_create(test_user['token'], channel2_name, False)
    chan_lst = channels_listall(test_user['token'])['channels']
    assert len(chan_lst) == 2
    channel1_details = chan_lst[0]
    channel2_details = chan_lst[1]
    assert channel1['channel_id'] == channel1_details['channel_id']
    assert channel1_name == channel1_details['name']
    # Checking that channel2's details match
    assert channel2['channel_id'] == channel2_details['channel_id']
    assert channel2_name == channel2_details['name']

# Unique tests for channels_listall
def test_listall_not_member():
    user1 = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channel1 = channels_create(user1['token'], "name", True)
    user2 = auth_register("secondemail@gmail.com", "1234567", "Jane", "Smith")
    chan_lst1 = channels_list(user1['token'])['channels']
    chan_lst2 = channels_list(user2['token'])['channels']
    # Checking that channels_listall returns the same list for user2,
    assert len(chan_lst1) == len(chan_lst2) == 1
    assert chan_lst1 == chan_lst2

#Assumption: All channels are listed by channels_listall, regardless of if they are private or not
def test_listall_private():
    user1 = auth_register("testemail@gmail.com", "1234567", "John", "Smith")
    channel1 = channels_create(user1['token'], "name", False)
    user2 = auth_register("secondemail@gmail.com", "1234567", "Jane", "Smith")
    chan_lst1 = channels_list(user1['token'])['channels']
    chan_lst2 = channels_list(user2['token'])['channels']
    # Checking that channels_listall returns the same list for user2,
    assert len(chan_lst1) == len(chan_lst2) == 1
    assert chan_lst1 == chan_lst2
