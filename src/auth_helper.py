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


def is_email_unique(email):
    '''
    Checks if an email is already associated with a user in glob_users
    '''
    glob_users = get_users()

    for user in glob_users.values():
        if email == user['email']:
            return False
    return True


def is_handle_unique(handle_str):
    '''
    Checks if a handle is already associated with a user in glob_users
    '''
    glob_users = get_users()

    for user in glob_users.values():
        if handle_str == user['handle_str']:
            return False
    return True


def is_user_disabled(u_id):
    '''Finds if a user has been deleted

    :param u_id: target user_id
    :type u_id: int
    :return: True if the user has been deleted, otherwise False
    :rtype: bool
    '''
    return get_users()[u_id]['disabled']


def find_id(email):
    '''
    Finds the user id associated with an email and returns it
    returns false if no user is found
    '''
    glob_users = get_users()

    for u_id in glob_users:
        if email == glob_users[u_id]['email']:
            return u_id
    # if no user is found with this email
    raise InputError(description='No user found')


def check_registration_inputs(email, password, name_first, name_last):
    '''
    Checks all inputs for registration raises the appropriate errors
    '''
    if not is_email_valid(email):
        raise InputError(description="Invalid Email")
    if not is_email_unique(email):
        raise InputError(
            description="An account with this email has already been registered"
        )
    if not is_password_valid(password):
        raise InputError(description="Password not strong enough")
    if not is_name_valid(name_first):
        raise InputError(
            description="First name must be between 1 and 50 characters long")
    if not is_name_valid(name_last):
        raise InputError(
            description="Last name must be between 1 and 50 characters long")

def check_login_inputs(email, password):
    '''
    Checks email is valid
    Checks email is associated with a user
    Checks password is correct
    Returns the u_id associated with the user
    '''
    if not is_email_valid(email):
        raise InputError(description="Invalid Email")
    if is_email_unique(email):
        raise InputError(description="This email has not been registered")

    u_id = find_id(email)
    glob_users = get_users()
    if is_user_disabled(u_id):
        raise InputError(description='This account has been removed from Slackr')
    password_hash = sha256(password.encode()).hexdigest()

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
