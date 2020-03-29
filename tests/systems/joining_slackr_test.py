''' Users should be able to register an account with Slackr and view available channels '''
import requests
from conftest import BASE_URL

CLIENT_DATA = {}

def test_registration(populate_slackr):
    '''
    registers a new user
    '''
    response = requests.post(f'{BASE_URL}/auth/register',
                             json={
                                 'email': 'z1234567@unsw.edu.au',
                                 'password': 'bigbrainpassword',
                                 'name_first': 'Kevin',
                                 'name_last': 'Chan',
                             })
    assert response.status_code == 200
    json = response.json()
    CLIENT_DATA['token'] = json['token']

def test_listing_channels():
    response = requests.get(f'{BASE_URL}/channels/list',
                            params={'token': CLIENT_DATA['token']})
    assert response.status_code == 200
    json = response.json()
    assert len(json['channels']) == 0

    response = requests.get(f'{BASE_URL}/channels/listall',
                            params={'token': CLIENT_DATA['token']})
    assert response.status_code == 200
    json = response.json()
    assert len(json['channels']) == 4

def test_creating_channels():
    response = requests.post(f'{BASE_URL}/channels/create',
                             json={
                                 'token': CLIENT_DATA['token'],
                                 'name': 'best channel ever',
                                 'is_public': True
                             })
    json = response.json()
    response = requests.get(f'{BASE_URL}/channels/list',
                            params={'token': CLIENT_DATA['token']})
    assert response.status_code == 200
    json = response.json()
    assert len(json['channels']) > 0
    response = requests.get(f'{BASE_URL}/channels/listall',
                            params={'token': CLIENT_DATA['token']})
    assert response.status_code == 200

def test_whos_on_slackr():
    response = requests.get(f'{BASE_URL}/users/all',
                            params={'token': CLIENT_DATA['token']})
    assert response.status_code == 200
    json = response.json()
    assert len(json['users']) == 21