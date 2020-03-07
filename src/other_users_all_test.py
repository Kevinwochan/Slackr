import pytest
from other import users_all
from auth import auth_register
from user import user_profile
from error import InputError, AccessError


def test_users_all_with_invalid_token():
    ''''Get the users info by an unathorised user (invalid token) throws an access error'''
    with pytest.raises(AccessError):
        users_all("invalid token")

# Normal 
def normal_test():
    # set up the user
    user_andrew = auth_register("andrewt@gmail.com", "password", "andrew", "taylor")
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


