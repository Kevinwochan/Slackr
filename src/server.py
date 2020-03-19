''' Assignment Imports '''
import sys
from json import dumps
from flask import Flask, request
from flask_cors import CORS
from error import InputError

''' Custom Imports '''
from auth import auth_register


def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response


APP = Flask(__name__)
CORS(APP)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)


# Example
@APP.route("/echo", methods=['GET'])
def echo():
    data = request.args.get('data')
    if data == 'echo':
        raise InputError(description='Cannot echo "echo"')
    return dumps({'data': data})


@APP.route('/auth/register', methods=['POST'])
def register():
    json = request.get_json()
    return dumps(
        auth_register(json['email'], json['password'], json['name_first'],
                      json['name_last']))


if __name__ == "__main__":
    APP.debug = True  #TODO: remove this for production
    APP.run(port=(int(sys.argv[1]) if len(sys.argv) == 2 else 8080))
