'''
Hangman Modules
'''
import random
import string
import requests
from src.global_variables import get_channels
import src.message

STATES = {
    'PROGRESS_1': 1,
    'PROGRESS_2': 2,
    'PROGRESS_3': 3,
    'PROGRESS_4': 4,
    'PROGRESS_5': 5,
    'PROGRESS_6': 6,
    'LOSE': 7,
    'WIN': 8,
}

ART = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
    'GAME OVER',
    'YOU SAVED HIM!',
]

'''
data =  {
    channel_id : {
        'answer': 'badger'
        'gusses': [a e i o u],
        'state' ; 1
    },
}
'''


def download_word_list():
    ''' downloads a wordlist'''
    response = requests.get(
        "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain")
    return response.content.decode('utf-8').splitlines()


word_list = download_word_list()
data = {}


def generate_random_answer():
    ''' generates a random answer to guess each new game of hangman '''
    return random.choice(word_list)


def start_hangman(channel_id, user_id, time_created, message_id):
    ''' initalisise a hangman game on a channel and inserts the response in the channel'''
    channel = get_channels()[channel_id]
    if has_hangman_started(channel_id):
        channel['messages'].insert(
            0,
            src.message.create_message(user_id, message_id, time_created,
                                       'A game of hangman is already in progress'))
        return

    new_word = generate_random_answer()
    data[channel_id] = {
        'answer': new_word,
        'guesses': [],
        'state': STATES['PROGRESS_1']
    }
    print(data)
    channel['messages'].insert(
        0,
        src.message.create_message(user_id, message_id, time_created,
                                   'HANGMAN STARTED\nguess a letter with /guess'))


def format_guess(channel_id):
    ''' nicely returns text about all of the users guesses so far
        e.g GUESSES: a b c
    '''
    return f'GUESSES: {" ".join(data[channel_id]["guesses"])}'


def format_answer(channel_id):
    ''' nicely returns text about how close the user is with the answer
        e.g ANSWER: R_CK
    '''
    text = ''
    answer = data[channel_id]['answer']
    geusses = data[channel_id]['guesses']
    for i in range(0, len(answer)):
        if answer[i] in geusses:
            text += answer[i]
        else:
            text += '_'
    return f'ANSWER: {text}'


def get_text(channel_id):
    ''' 
    This function returns some pretty text about the game
    '''
    state = data[channel_id]['state']
    if state == STATES['WIN']:
        return f'\n{ART[state]}'
    if state == STATES['LOSE']:
        return f'\n{ART[state]}\nANSWER WAS {data[channel_id]["answer"]}'
    return '\n'.join([
        '\n', ART[state],
        format_answer(channel_id),
        format_guess(channel_id)
    ])


def wrong_guess(channel_id):
    ''' 
    called everytime a user makes an incorrect guess
    This pushes the STATE of the game closer to GAME OVER
    '''
    data[channel_id]['state'] += 1


def correct_guess(channel_id):
    ''' 
    Called everytime a user makes a correct guess
    function changes the state to WIN if all letters in ANSWER are in our GUESSES list
    '''
    for letter in data[channel_id]['answer']:
        if not letter in data[channel_id]['guesses']:
            return
    data[channel_id]['state'] = STATES['WIN']


def guess(message, channel_id, user_id, time_created, message_id):
    '''
    this function is called everytime a user makes a guess
    the guessed letter is not counted if the letter is already in GUESSES
    and then calls on other funcitons to change the state of the game

    :param letter: str, assume len(str) == 1
    :rtype str
    '''
    message_split = message.split(' ')
    if len(message_split) != 2:
        message = "guess must be a single letter of the english alphabet e.g '/guess a'"

    if not has_hangman_started(channel_id):
        message = 'start a new hangman game with /hangman'

    elif data[channel_id]['state'] == STATES['WIN'] or data[channel_id][
            'state'] == STATES['LOSE']:
        message = 'start a new hangman game with /hangman'
    else:
        letter = message_split[1]
        if len(letter) != 1 or letter in string.punctuation or letter == ' ' or letter.isdigit():
            message = "guess must be a single letter of the english alphabet e.g '/guess a'"

        elif letter in data[channel_id]['guesses']:
            message = 'you have already guessed this'
        else:
            data[channel_id]['guesses'].append(letter)
            if letter in data[channel_id]['answer']:
                correct_guess(channel_id)
            else:
                wrong_guess(channel_id)
            message = get_text(channel_id)
    channel = get_channels()[channel_id]
    print(data)
    channel['messages'].insert(0, src.message.create_message(
        user_id, message_id, time_created, message))


def has_hangman_started(channel_id):
    '''checks if a game of hangman is in progress '''
    if channel_id in data:
        state = data[channel_id]['state']
        if not state in [STATES['WIN'], STATES['LOSE']]:
            return True
    return False
