from src.auth import JWTS, USERS
from src.channel import CHANNELS


def workspace_reset():
    ''' Deletes all Slackr information as if the website was just launched '''
    JWTS.clear()
    USERS.clear()
    CHANNELS.clear()
