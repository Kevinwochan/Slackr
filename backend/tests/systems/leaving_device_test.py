''' Users should be able to log out of slackr so that other people that use the device cannot impersonate the user '''
import requests
from tests.systems.conftest import BASE_URL

USER = {'password': 'bigbrainpassword', 'email': 'z1234567@unsw.edu.au'}


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


def test_authorised_user_logs_out():
    ''' Log the user our with no issues '''
    response = requests.post(f'{BASE_URL}/auth/logout',
                             json={'token': USER['token']})


def test_unauthorised_user_access():
    '''
    Lists available channels after logging out
    '''
    response = requests.get(f'{BASE_URL}/channels/list',
                            params={'token': USER['token']})
    assert response.status_code == 403
    response = requests.get(f'{BASE_URL}/channels/listall',
                            params={'token': USER['token']})
    assert response.status_code == 403


def test_unauthorised_user_incorrect_credentials():
    '''
    Attempts to log in using an invalid password multiple times
    '''
    response = requests.post(f'{BASE_URL}/auth/login',
                             json={
                                 'email': f'{USER["email"]}a',
                                 'password': f'{USER["password"]}',
                             })
    assert response.status_code == 400

    response = requests.post(f'{BASE_URL}/auth/login',
                             json={
                                 'email': f'{USER["email"]}',
                                 'password': f'{USER["password"]}a',
                             })
    assert response.status_code == 400


def test_logging_back_in():
    '''
    Logging in with valid credentials should restore full access
    '''
    response = requests.post(f'{BASE_URL}/auth/login',
                             json={
                                 'email': USER["email"],
                                 'password': USER["password"],
                             })
    json = response.json()
    USER['token'] = json['token']
    USER['user_id'] = json['u_id']


def test_authorised_user_access():
    '''
    Channels access is restored
    '''
    requests.get(f'{BASE_URL}/channels/list', params={'token': USER['token']})
    requests.get(f'{BASE_URL}/channels/listall',
                 params={'token': USER['token']})
