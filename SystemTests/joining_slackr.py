''' Users should be able to register an account with Slackr and view available channels '''
import requests
from conftest import BASE_URL


def test_slackr_user_lists_available_channels(populate_slackr):
    '''
    registers a new user
    '''
    response = requests.post(f'{BASE_URL}/auth/register',
                             json={
                                 'email': 'z1234567',
                                 'password': 'bigbrainpassword',
                                 'name_first': 'Kevin',
                                 'name_last': 'Chan',
                             })
    json = response.json()
    token = json['token']
    response = requests.get(f'{BASE_URL}/channels/list',
                            params={'token': token})
    json = response.json()
    assert len(json['channels']) == 0
    response = requests.get(f'{BASE_URL}/channels/listall',
                            params={'token': token})
    json = response.json()
    assert len(json['channels']) == 0

    response = requests.post(f'{BASE_URL}/channel/create',
                             json={
                                 'token': token,
                                 'name': 'best channel ever',
                                 'is_public': True
                             })
    json = response.json()
    response = requests.get(f'{BASE_URL}/channels/list',
                            params={'token': token})
    json = response.json()
    assert len(json['channels']) > 0
    response = requests.get(f'{BASE_URL}/channels/listall',
                            params={'token': token})
