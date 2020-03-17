from flask import Flask
from src.auth import auth_login
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
# TODO: remmove this get method, get is only for testing
@app.route('/auth/login', methods=['GET','POST'])
def login():
        return json.dumps(auth_login('', ''))

