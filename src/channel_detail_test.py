import pytest
from error import AccessError, InputError
from auth import auth_register
from channel import channel_details, channel_invite
from channels import channels_create

"""
    Assume the owner of a channel can only be one person
"""

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
    
# Normal test for the channel_details
def test_channel_details(user_chas, user_dav, user_jas, channel_dav):
    
    # Invite jas and chas to the channel
    channel_invite(user_dav['token'], channel_dav['channel_id'], user_jas['u_id'])
    channel_invite(user_dav['token'], channel_dav['channel_id'], user_chas['u_id'])
    
    # Achieve the detail of the channel by dev
    channel_dav_detail = channel_details(user_dav['token'], channel_dav['channel_id'])
    
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
        assert channel_details(user_dav['token'], "!Invalid")
        
# Test for the AccessError
def test_invalid_member(user_chas, channel_dav):
    with pytest.raises(AccessError):
        assert channel_details(user_chas['token'], channel_dav['channel_id'])
