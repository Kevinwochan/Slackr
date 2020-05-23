'''Provides password reset functionality to slackr.
all generated reset tokens expire after approximately 20min
'''
import smtplib
import ssl
from src.auth_helper import is_password_valid, id_from_email, hash_string
from src.utils import generate_reset_code, check_reset_code
from src.error import InputError
from src.global_variables import get_users

PORT = 465
SLACKR_EMAIL = 'slackrmehk@gmail.com'
PASSWORD = 'nashe4-riqnav-Jaqfur'

#Time before reset_code expires (10min)
VALID_DURATION = 10*60

def send_email(recipient_email, message):
    '''sends an email to recipient_email containing message

    :param recipient_email: email address to recieve the email
    :type recipient_email: str
    :param message: message contained in the email
    :type message: str
    '''
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
        server.login(SLACKR_EMAIL, PASSWORD)
        server.sendmail(SLACKR_EMAIL, recipient_email, message)

def create_reset_email(recipient_email, reset_code):
    '''Returns message to send as an email

    :param recipient_email: email address to recieve the email
    :type recipient_email: str
    :param reset_code: jwt token
    :type reset_code: str
    :return: email message
    :rtype: str
    '''

    return f"""\
Subject: Reset Your Password

We've recieved a request to reset the password for your slackr account:
{recipient_email}

Your reset code is:
{reset_code}

Please copy and paste this to avoid mistakes.
This code will expire after 10 minutes.
"""


def auth_passwordreset_request(email):
    '''For a registered email, generate and email a reset code that expires after VALID_DURATION


    :param email: valid email address that corresponds to a slackr user
    :type email: str
    :return: empty dictionary
    :rtype: dict
    '''
    if id_from_email(email) is None:
        return {}
    reset_code = generate_reset_code(email, VALID_DURATION)
    message = create_reset_email(email, reset_code)
    send_email(email, message)
    return {}

def auth_passwordreset_reset(reset_code, new_password):
    '''Given a valid reset code and password, replaces a users password

    :param reset_code: valid jwt containing a users email
    :type reset_code: str
    :param new_password: Users new password
    :type new_password: str
    :raises InputError: Invalid reset code, expired reset code, invalid password,
    :raises InputError: No user exists with that email
    :return: empty dictionary
    :rtype: dict
    '''
    email = check_reset_code(reset_code)
    u_id = id_from_email(email)
    if u_id is None:
        return {}
    if not is_password_valid(new_password):
        raise InputError(description="Password not strong enough")
    password_hash = hash_string(new_password)
    glob_users = get_users()
    glob_users[u_id]['password_hash'] = password_hash

    return {}
