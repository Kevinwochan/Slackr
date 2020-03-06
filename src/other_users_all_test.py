import pytest
from other import users_all
from auth import auth_register
from user import user_profile

"""

Initially two users are set up with name of "andrew tylor" and "chris chen" respectively.
Then use andrew's token to get all the users' profile.
Afterwards, setting up the expected output and comparing the function tested

"""

def setup_other():
    # set up the user
    andrew = auth_register("andrewt@gmail.com", "password", "andrew", "taylor")
    chris = auth_register("chrisc@gmail.com", "pilot", "chris", "chen")

    # Access the users info by andrew's token
    users = users_all(andrew['token'])
    
    # set up the expected value
    andrew_profile = user_profile(andrew['token'], andrew['u_id'])
    chris_profile = user_profile(chris['token'], andrew['u_id'])
    
    # andrew's expected info
    expected_out = []
    expected_out.append({})
    expected_out[0]['u_id'] = andrew_profile['u_id']
    expected_out[0]['email'] = andrew_profile['email']
    expected_out[0]['name_first'] = andrew_profile['name_first']
    expected_out[0]['name_last'] = andrew_profile['name_last']
    expected_out[0]['handle_str'] = andrew_profile['handle_str']
    
    # chris's expected info
    expected_out.append({})
    expected_out[1]['u_id'] = chris_profile['u_id']
    expected_out[1]['email'] = chris_profile['email']
    expected_out[1]['name_first'] = chris_profile['name_first']
    expected_out[1]['name_last'] = chris_profile['name_last']
    expected_out[1]['handle_str'] = chris_profile['handle_str']
     
    assert users == expected_out
