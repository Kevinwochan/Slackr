from hashlib import sha256
import smtplib, ssl
from src.auth_helper import is_password_valid, find_id, is_email_unique
from src.utils import generate_reset_code, check_reset_code
from src.error import InputError
from src.global_variables import get_users

PORT = 465
SLACKR_EMAIL = 'slackrmehk@gmail.com'
PASSWORD = 'nashe4-riqnav-Jaqfur'

#Time before reset_code expires (20min)
VALID_DURATION = 20*60

def send_passwordreset_email(recipient_email, reset_code):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
        server.login(SLACKR_EMAIL, PASSWORD)
        server.sendmail(SLACKR_EMAIL, recipient_email, reset_code)


def auth_passwordreset_request(email):
    if is_email_unique(email):
        return {}
    reset_code = generate_reset_code(email, VALID_DURATION)
    send_passwordreset_email(email, reset_code)
    return {}

def auth_passwordreset_reset(reset_code, new_password):
    '''Given a valid reset code and password, replaces a users password

    :param reset_code: valid jwt containing a users email
    :type reset_code: str
    :param new_password: Users new password
    :type new_password: str
    :raises InputError: Invalid reset code, expired reset code, invalid password
    :return: empty dictionary
    :rtype: dict
    '''
    email = check_reset_code(reset_code)
    u_id = find_id(email)
    if not is_password_valid(new_password):
        raise InputError(description="Password not strong enough")
    password_hash = sha256(new_password.encode()).hexdigest()
    glob_users = get_users()
    glob_users[u_id]['password_hash'] = password_hash

    return {}
