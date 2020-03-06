import pytest
from error import AccessError, InputError
from auth import auth_register
from channel import channel_invite, channel_details
from channels import channels_create


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
def channel_dav():
    return channels_create(user_dav['token'], channel_dav, False)
    
# Test for invite a new member by an old member
def test_invite(user_dav, user_jas, channel_dav):
    channel_invite(user_dav['token'], channel_dav['channel_id'], user_jas['u_id'])
    
    # create member jas
    member_jas = {}
    member_jas['u_id'] = user_jas['u_id']
    member_jas['name_first'] = "jas"
    member_jas['name_last'] = "zhu"
    
    # set up channel details
    channel_dav_detail = channel_details(user_dav['token'], channel_dav['channel_id'])
    
    assert member_jas in channel_dav_detail['all_members']
    
    
# Test for channel_id does not refer to a valid channel
def test_invalid_channel_invite(user_dav, user_jas):
    with pytest.raises(InputError):
        assert channel_invite(user_dav['token'], "invalid channel id", user_jas['u_id'])
        
# Test for the channel_id is a valid channel but the invitor isn't a member
def test_valid_channel_invite(user_chas, user_jas, channel_dav):
    with pytest.raises(InputError):
        assert channel_invite(user_chas['token'], channel_dav['channel_id'], user_jas['u_id'])
        
# Test for u_id does not refer to a valid user
def test_valid_u_id(user_dav, channel_dav):
    with pytest.raises(InputError):
        assert channel_invite(user_dav['token'], channel_dav['channel_id'], "!invalid")
        
# Test for the authorised user is not part of channel.
def test_invite_right(user_jas, user_chas, channel_dav):
    with pytest.raises(AccessError):
        assert channel_invite(user_jas['token'], channel_dav['channel_id'], user_chas)
        
# Test if the invited member has already been invited
# This test will not be run unless the test_invite working well
def test_double_invite(user_dav, user_jas, channel_dav):
    
    # First invitation
    channel_invite(user_dav['token'], channel_dav['channel_id'], user_jas['u_id'])
    
    # Second invitation
    channel_invite(user_dav['token'], channel_dav['channel_id'], user_jas['u_id'])
    
    # create member jas
    member_jas = {}
    member_jas['u_id'] = user_jas['u_id']
    member_jas['name_first'] = "jas"
    member_jas['name_last'] = "zhu"
    
    # set up channel details
    channel_dav_detail = channel_details(user_dav['token'], channel_dav['channel_id'])
    
    assert member_jas in channel_dav_detail['all_members']
    
# If the user in the channel invite himself
def test_invite_itself(user_dav, channel_dav):
    
    # invite jas to the channel
    channel_invite(user_dav['token'], channel_dav['channel_id'], user_jas['u_id'])
    
    # jas invite himself again
    channel_invite(user_jas['token'], channel_dav['channel_id'], user_jas['u_id'])
    
    # create member jas
    member_jas = {}
    member_jas['u_id'] = user_jas['u_id']
    member_jas['name_first'] = "jas"
    member_jas['name_last'] = "zhu"
    
    # set up channel details
    channel_dav_detail = channel_details(user_dav['token'], channel_dav['channel_id'])
    
    assert member_jas in channel_dav_detail['all_members']
    
# If a user invite itself to a channel where he is not a member
def invite_itself(user_jas, channel_dav):

    # jas invite himself again
    channel_invite(user_jas['token'], channel_dav['channel_id'], user_jas['u_id'])
    
    # create member jas
    member_jas = {}
    member_jas['u_id'] = user_jas['u_id']
    member_jas['name_first'] = "jas"
    member_jas['name_last'] = "zhu"
    
    # set up channel details
    channel_dav_detail = channel_details(user_dav['token'], channel_dav['channel_id'])
    
    assert member_jas not in channel_dav_detail['all_members']    

    
    
