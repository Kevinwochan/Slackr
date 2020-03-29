''' Users should be able to organise messages by a team or topic'''
import requests
from conftest import BASE_URL

USER = {'password': 'bigbrainpassword', 'email': 'z1234567@unsw.edu.au'}
CLIENT_DATA = {}


def test_setting_up():
    ''' Registers a new user '''
    response = requests.post(f'{BASE_URL}/auth/register',
                             json={
                                 'email': USER['email'],
                                 'password': USER['password'],
                                 'name_first': 'Kevin',
                                 'name_last': 'Chan',
                             })
    json = response.json()
    USER['token'] = json['token']
    USER['user_id'] = json['u_id']


def test_create_channel():
    '''
    A user can create channels
    '''
    requests.get(f'{BASE_URL}/channels/list', params={'token': USER['token']})

    response = requests.post(f'{BASE_URL}/channels/create',
                             json={
                                 'token': USER['token'],
                                 'name': 'Developers',
                                 'is_public': True
                             })
    assert response.status_code == 200
    json = response.json()
    CLIENT_DATA['channels'] = [json['channel_id']]

    response = requests.get(f'{BASE_URL}/channels/list',
                            params={'token': USER['token']})

    assert response.status_code == 200
    json = response.json()
    assert len(json['channels']) == 1
    assert json['channels'][0]['channel_id'] == CLIENT_DATA['channels'][0]
    assert json['channels'][0]['name'] == 'Developers'

    response = requests.get(f'{BASE_URL}/channels/listall',
                            params={'token': USER['token']})

    assert response.status_code == 200
    json = response.json()
    assert len(json['channels']) == 5


def test_inviting_users():
    '''
    Invites a load of users 
    '''
    for user_id in range(0, 4):
        response = requests.post(f'{BASE_URL}/channel/invite',
                                 json={
                                     'token': USER['token'],
                                     'channel_id': CLIENT_DATA['channels'][0],
                                     'u_id': user_id
                                 })
        assert response.status_code == 200

    response = requests.get(f'{BASE_URL}/channel/details',
                            params={
                                'token': USER['token'],
                                'channel_id': CLIENT_DATA['channels'][0]
                            })
    assert response.status_code == 200
