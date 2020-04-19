'''
Adds data persistence functionality to slackr - automatically run before first flask request
NOTE: global_valid_tokens , global_standups are not backed up. In other words
All users are logged out upon server restart, all active standups are discarded.
Likewise, any unsent messages sent with message/sendlater are discarded
'''
from threading import Thread
from time import sleep
from datetime import datetime
from pickle import dump, load
from src.global_variables import get_users, get_channels, get_num_messages, replace_data
from src.utils import get_current_timestamp


def backup_data():
    '''Pickles slackr data with a timestamp.'''
    slackr_data = {
        'timestamp': get_current_timestamp(),
        'global_users': get_users(),
        'global_channels': get_channels(),
        'global_num_messages': get_num_messages()
    }
    with open('slackr_data.p', 'wb') as FILE:  #pylint: disable=invalid-name
        dump(slackr_data, FILE)


def load_data():
    '''If slackr backup exists, unpickles slackr backup and stores it in global variables.'''
    try:
        data = load(open("slackr_data.p", "rb"))
        date = datetime.fromtimestamp(
            data['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        print(f'Slackr backup found: Loading data from {date} UTC.')
        replace_data(data['global_users'], data['global_channels'],
                     data['global_num_messages'])

    except FileNotFoundError:
        print('No Slackr backup found: Launching clean.')


def start_auto_backup(interval):
    '''Creates and starts a daemon thread which runs backup_data() repeatedly.

    :param interval: seconds between backups
    :type interval: int
    '''
    print(f'Starting automatic data backup at {interval}s intervals.')

    def auto_backup(interval):
        while True:
            sleep(interval)
            backup_data()

    thread = Thread(target=auto_backup, args=[interval], daemon=True)
    thread.start()
