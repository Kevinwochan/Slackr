''' Users should be able to upload a display picture that is accessible publicly and stored by the server in association with the user'''
import requests
from tests.systems.conftest import BASE_URL

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

def test_submitting_image():
    '''
    submits an image link
    '''
    response = requests.post(f'{BASE_URL}/user/profile/uploadphoto',
                             json={
                                 'token': CLIENT_DATA['token'],
                                 'img_url': 'https://imgs.xkcd.com/comics/ohm.png',
                                 'x_start': '0',
                                 'y_start': '0',
                                 'x_end': '200',
                                 'y_end': '200',
                             })
    assert response.status_code == 200
    json = response.json()


def test_creating_channels():
    response = requests.post(f'{BASE_URL}/channels/create',
                             json={
                                 'token': CLIENT_DATA['token'],
                                 'name': 'best channel ever',
                                 'is_public': True
                             })
    assert response.status_code == 200
    json = response.json()

def test_profile_image_is_default():
    response = requests.get(f'{BASE_URL}/channels/details',
                            params={'token': CLIENT_DATA['token']})
    json = response.json()

