'''
Allows users to edit and set their profile information
'''
import re
import requests
from PIL import Image
from src.utils import check_token, generate_random_string
from src.error import InputError
from src.global_variables import get_users
from src.auth_helper import is_user_disabled

def is_valid_handle(host_user_id, handle_str):
    '''
    checks that no existing user has this handle_str
    '''
    if len(handle_str) < 3 or len(handle_str) > 20:
        return False
    users = get_users()
    if users[host_user_id]['handle_str'] == handle_str:
        return True
    for user_id in users:
        if users[user_id]['handle_str'] == handle_str:
            return False
    return True


def is_valid_email(host_user_id, email):
    '''
    code from https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    checks that the valid is in a valid format according to geeks for geeks
    and checks that this email is not already in use
    '''
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not re.search(regex, email):
        return False
    users = get_users()
    if users[host_user_id]['email'] == email:
        return True
    for user_id in users:
        if users[user_id]['email'] == email:
            return False
    return True


def user_profile(token, user_id):
    '''
    fetches a user profile, any valid user is able to do this
    '''
    check_token(token)
    users = get_users()
    if not user_id in users or is_user_disabled(user_id):
        raise InputError
    user = users[user_id]
    return {
        'user': {
            'u_id': user_id,
            'email': user['email'],
            'name_first': user['name_first'],
            'name_last': user['name_last'],
            'handle_str': user['handle_str'],
            'profile_img_url': user['profile_img_url']
        }
   }


def user_profile_setname(token, name_first, name_last):
    '''
    Sets the name of the profile using given strings
    name_first and name_last have size limits
    and only the user owner can change this
    '''
    user_id = check_token(token)
    if len(name_first) < 1 or len(name_first) > 50:
        raise InputError
    if len(name_last) < 1 or len(name_last) > 50:
        raise InputError

    user = get_users()[user_id]
    user['name_first'] = name_first
    user['name_last'] = name_last

    return {}


def user_profile_setemail(token, email):
    '''
    Update the authorised user's email address
    '''
    user_id = check_token(token)
    if not is_valid_email(user_id, email):
        raise InputError

    user = get_users()[user_id]
    user['email'] = email
    return {}


def user_profile_sethandle(token, handle_str):
    '''
    Update the authorised user's handle (i.e. display name)
    handle has a size limit
    '''
    user_id = check_token(token)
    if len(handle_str) < 1 or len(handle_str) > 50:
        raise InputError
    if not is_valid_handle(user_id, handle_str):
        raise InputError

    user = get_users()[user_id]
    user['handle_str'] = handle_str
    return {}


def user_profile_setimage(token, img_url, x_start, y_start, x_end, y_end):
    '''
    Update the authorised user's display photo
    Downloads the given img_url into the server folder 'images'
    Crops images if they do not fit the size
    :param token:
    :type token: string
    '''
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    user_id = check_token(token)
    user = get_users()[user_id]

    file_extension = img_url.rsplit('.', 1)[1].lower()
    if not file_extension in ALLOWED_EXTENSIONS:
        raise InputError(description="file not allowed")

    if not x_start < x_end:
        raise InputError(description="x_start must be larger than x_end")
    if not y_start < y_end:
        raise InputError(description="y_start must be larger than y_end")

    try:
        image = requests.get(img_url, allow_redirects=True).content
    except:
        raise InputError(description="could not download image")

    new_file_name = f'{generate_random_string(20)}.{file_extension}'
    new_image = open(f'images/original/{new_file_name}', 'wb')
    new_image.write(image)

    original_image = Image.open(f'images/original/{new_file_name}')
    original_image = original_image.crop((x_start, y_start, x_end, y_end))
    cropped_image = open(f'images/cropped/{new_file_name}', 'wb')
    original_image.save(cropped_image)

    user['profile_img_url'] = f'/imgurl/{new_file_name}'
    return {}

