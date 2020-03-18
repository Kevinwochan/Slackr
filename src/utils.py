from src.auth import JWTS, USERS
from src.channel import CHANNELS


def workspace_reset():
    ''' Deletes all Slackr information as if the website was just launched '''
    # TODO: verify user is an owner of the slackr
    JWTS.clear()
    USERS.clear()
    CHANNELS.clear()
