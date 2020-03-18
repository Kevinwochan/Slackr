from flask import Flask
from src.auth import auth_login, JWTS
import json

app = Flask(__name__)

'''
a list of users.
each user is a dictionary like:
    user = {
        'u_id': 2,
        etc...
        'email',
        name_first, 
        name_last, 
        handle_str,
        password,
        username
    }
'''
USERS = []
CHANNELS = []
'''
a list of jwts generated from a user successffully logging in
'''


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/auth/login', methods=['POST'])
def login():
    JWTS.append(auth_login('', ''))
    return

if __name__ == '__main__':
    app.debug = True #TODO: remove this for production
    app.run()
