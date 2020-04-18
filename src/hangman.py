import string
import requests
import random
from src.global_variables import get_channels

STATES = {
    'PROGRESS_1' : 1,
    'PROGRESS_2' : 2,
    'PROGRESS_3' : 3,
    'PROGRESS_4' : 4,
    'PROGRESS_5' : 5,
    'PROGRESS_6' : 6,
    'LOSE'       : 7,
    'WIN'        : 8,
}

ART = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
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


ANSWER = ''
STATE = STATES['PROGRESS_1']
GUESSES = []

def start_hangman(channel_id, user_id, time_created, message_id):
    global STATE
    STATE = STATES['PROGRESS_1']
    channel = get_channels()[channel_id]
    new_message = {
        'u_id': user_id,
        'message_id': message_id,
        'time_created': time_created,
        'message': 'HANGMAN STARTED',
        'reacts': [],
        'is_pinned': False
    }
    generate_random_answer()
    channel['messages'].insert(0, new_message)
    return

def generate_random_answer():
    ''' generates a random answer to guess each new game of hangman '''
    global ANSWER
    words_bank = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(words_bank)
    words_list = response.content.decode('utf-8').splitlines()
    ANSWER = random.choice(words_list)
    return ANSWER

def format_guess():
    ''' nicely returns text about all of the users guesses so far
        e.g GUESSES: a b c
    '''
    global GUESSES
    return f'GUESSES: {" ".join(GUESSES)}'

def format_answer():
    ''' nicely returns text about how close the user is with the answer
        e.g ANSWER: R_CK
    '''
    global ANSWER
    global GUESSES
    text = ''
    for i in range(0, len(ANSWER)):
        if ANSWER[i] in GUESSES:
            text += ANSWER[i]
        else:
            text += '_'
    return f'ANSWER: {text}'


def get_text():
    ''' 
    This function returns some pretty text about the game
    '''
    global ART
    global STATE
    if STATE == STATES['WIN']:
        return f'\n{ART[STATE]}'
    elif STATE == STATES['LOSE']:
        global ANSWER
        return f'\n{ART[STATE]}\nANSWER WAS {ANSWER}'
    
    return '\n'.join(['\n', ART[STATE], format_answer(), format_guess()])

def wrong_guess():
    ''' 
    called everytime a user makes an incorrect guess
    This pushes the STATE of the game closer to GAME OVER
    '''
    global STATE
    global ART
    STATE += 1

def correct_guess():
    ''' 
    Called everytime a user makes a correct guess
    function changes the state to WIN if all letters in ANSWER are in our GUESSES list
    '''
    global ANSWER
    global STATE
    for letter in ANSWER:
        if not letter in GUESSES:
            return
    STATE = STATES['WIN']

def guess(letter):
    '''
    this function is called everytime a user makes a guess
    the guessed letter is not counted if the letter is already in GUESSES
    and then calls on other funcitons to change the state of the game

    :param letter: str, assume len(str) == 1
    :rtype str
    '''
    global GUESSES
    if len(letter) != 1 or letter in string.punctuation or letter == ' ' or letter.isdigit():
        return 'invalid guess, guess a single letter'
    if letter in GUESSES:
        return 'you have already guessed this'

    GUESSES.append(letter)
    if letter in ANSWER:
        correct_guess()
    else:
        wrong_guess()
    return get_text()

if __name__ == '__main__':
    generate_random_answer()
    # ANSWER = 'badger'
    while STATE != STATES['WIN'] and STATE != STATES['LOSE']:
        letter = input('guess a letter: ')
        print(guess(letter))
    
