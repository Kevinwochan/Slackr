''' python imports '''
from flask import Flask
import json

''' assignment code imports '''
from src.auth import auth_login
from src.utils import workspace_reset

app = Flask(__name__)


@app.route('/')
def hello_world():
    return json.dumps(JWTS)

@app.route('/auth/login', methods=['POST'])
def login():
    return

@app.route('workspace/reset', methods=['POST']
def reset():
    workspace_reset()
    return 

if __name__ == '__main__':
    app.debug = True #TODO: remove this for production
    app.run()
