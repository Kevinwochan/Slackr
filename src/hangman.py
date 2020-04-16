import requests
import random

STATES = {
    'PROGRESS_1' : 1,
    'PROGRESS_2' : 2,
    'PROGRESS_3' : 3,
    'PROGRESS_4' : 4,
    'PROGRESS_5' : 5,
    'PROGRESS_6' : 6,
    'PROGRESS_7' : 7,
    'WIN'        : 8,
    'LOSE'       : 9
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

def generate_random_answer():
    ''' generates a random answer to guess each new game of hangman '''
    global ANSWER
    words_bank = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    words_list = response.content.splitlines()
    ANSWER = random.choice(words_list)
    return ANSWER

def format_guess():
    ''' converts data into text '''
    global GUESSES
    return f'GUESSES: {" ".join(GUESSES)}'

def format_answer():
    ''' converts data into text '''
    global ANSWER
    global GUESSES
    text = ''
    for i in range(0, len(ANSWER)):
        if ANSWER[i] in GUESSES:
            text += ANSWER[i]
        else:
            text += '_'
    return f'ANSWER: {text}'

def get_text_art(state):
    ''' converts state to text'''
    global ART
    return ART[STATE]

def get_text():
    ''' converts state into text '''
    global ART
    global STATE
    if STATE != STATES['WIN'] and STATE != STATES['LOSE']:
        return '\n'.join(['\n', get_text_art(STATE), format_answer(), format_guess()])
    return '\n'.join(['\n', get_text_art(STATE)])

def wrong_guess():
    ''' updates the state'''
    global STATE
    global ART
    STATE += 1

def correct_guess(letter):
    ''' updates the state'''
    global GUESSES
    global ANSWER
    global STATE
    GUESSES.append(letter)
    for letter in ANSWER:
        if not letter in GUESSES:
            return
    STATE = STATES['WIN']

def guess(letter):
    ''' core logic '''
    global GUESSES
    if letter in GUESSES:
        return 'you have already guessed this'
    elif letter in ANSWER:
        correct_guess(letter)
    else:
        wrong_guess()
    return get_text()

if __name__ == '__main__':
    print(get_text())
    while STATE != STATES['WIN'] and STATE != STATES['LOSE']:
        letter = input('guess a letter: ')
        print(guess(letter))
    
