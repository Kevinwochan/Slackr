'''
This file provides shared pytests and fixtures for all System Tests
'''
import os
import pytest
import requests

IP = '127.0.0.1'
PORT = os.getenv('FLASK_RUN_PORT')
BASE_URL = f'http://{IP}:{PORT}'


@pytest.fixture(autouse=True, scope='module')
def clean_application():
    '''
    Deletes all application data by resetting the workspace
    '''
    requests.post(f'{BASE_URL}/workspace/reset', json={})


@pytest.fixture(autouse=True, scope='module')
def populate_slackr():
    '''
    Populates slackr as if it has been in use for the passed couple of minutes
    '''
    tokens = []
    for user in range(20):
        response = requests.post(f'{BASE_URL}/auth/register',
                                 json={
                                     'email': f'z{user}@unsw.edu.au',
                                     'password': f'reallystrongpassword{user}',
                                     'name_first': f'{user}first',
                                     'name_last': f'{user}last',
                                 })
        tokens.append(response.json()['token'])

    channels = []
    for channel in range(2):
        requests.post(f'{BASE_URL}/channel/create',
                      json={
                          'token': tokens[channel],
                          'name': f'new channel {channel}',
                          'is_public': True
                      })
        channels.append(response.json()['channel_id'])

    for channel in range(2):
        requests.post(f'{BASE_URL}/channel/create',
                      json={
                          'token': tokens[channel],
                          'name': f'new channel {channel}',
                          'is_public': False
                      })
        channels.append(response.json()['channel_id'])

    return {'channels': channels, 'tokens': tokens}
