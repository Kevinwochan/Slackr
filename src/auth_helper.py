'''
Helper functions for auth_login and auth_register.
Checks inputs and raises appropriate errors.
'''
import re
from hashlib import sha256
from src.error import InputError
from src.global_variables import get_users


# These functions check that inputs are valid according to the project specifications for the
# functions auth login and auth register.
def is_email_valid(email):
    '''
    Checks if email is valid, using the method described here:
    https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/

    Returns True if email is valid, otherwise returns False.
    '''
    condition = re.search(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',
                          email)

    return bool(condition)


def is_password_valid(password):
    '''
    '[invalid if] Password entered is less than 6 characters long'

    Returns True if password is valid, otherwise returns False
    '''
    condition = len(password) >= 6

    return bool(condition)


def is_name_valid(name):
    '''
    '[Invalid if] name is not between 1 and 50 characters inclusive in length'

    Returns True if name is valid, otherwise returns False.
    '''
    condition_1 = len(name) >= 1
    condition_2 = len(name) <= 50

    return bool(condition_1 and condition_2)


def id_from_email(email):
    '''Returns the user id corresponding to an email

    :param email: email to be verified
    :type email: str
    :return: if user is found, returns u_id, otherise None
    :rtype: int/NoneType
    '''
    glob_users = get_users()

    for u_id in glob_users:
        if email == glob_users[u_id]['email']:
            return u_id
    return None


def is_handle_unique(handle_str):
    '''
    Checks if a handle is already associated with a user in glob_users
    '''
    glob_users = get_users()

    for user in glob_users.values():
        if handle_str == user['handle_str']:
            return False
    return True

def check_registration_inputs(email, password, name_first, name_last):
    '''
    Checks all inputs for registration raises the appropriate errors
    '''
    if not is_email_valid(email):
        raise InputError(description="Invalid Email")
    if id_from_email(email) is not None:
        raise InputError(description="An account with this email has already been registered")
    if not is_password_valid(password):
        raise InputError(description="Password not strong enough")
    if not is_name_valid(name_first):
        raise InputError(
            description="First name must be between 1 and 50 characters long")
    if not is_name_valid(name_last):
        raise InputError(
            description="Last name must be between 1 and 50 characters long")

def hash_string(string):
    '''returns the sha256 hash of a string

    :param string: String to be hashed
    :type string: str
    :return: string hash
    :rtype: str
    '''
    return sha256(string.encode()).hexdigest()

def check_login_inputs(email, password):
    '''
    Checks email is valid
    Checks email is associated with a user
    Checks password is correct
    Returns the u_id associated with the user
    '''
    if not is_email_valid(email):
        raise InputError(description="Invalid Email")
    u_id = id_from_email(email)
    if u_id is None:
        raise InputError(description="This email has not been registered")

    glob_users = get_users()
    password_hash = hash_string(password)

    # checking user password
    if glob_users[u_id]['password_hash'] != password_hash:
        raise InputError(description='Incorrect password')

    return u_id


def create_handle(name_first, name_last):
    '''
    creates handle by joining a users (lowercase) first and last names, cutting it off at
    20 characters, and adding numbers to the end to make it unique if nessessary.
    '''
    concat = (name_first + name_last)[:20].lower()
    i = '0'
    handle_str = concat
    while not is_handle_unique(handle_str):
        # Loop and add numbers to the end of handle_str until unique
        handle_str = concat[:20 - len(i)] + i
        i = str(int(i) + 1)

    return handle_str
