''' Flask API for Slackr '''
import sys
import os
from flask import Flask, request, jsonify, send_from_directory, send_file
from json import dumps
from flask_cors import CORS
from src.auth import auth_register, auth_login, auth_logout
from src.admin import permission_change
from src.channel import channel_addowner, channel_details, channel_invite, channel_join, channel_leave, channel_messages, channel_removeowner
from src.channels import channels_create, channels_list, channels_listall
from src.user import user_profile, user_profile_setemail, user_profile_sethandle, user_profile_setname, user_profile_setimage
from src.message import message_edit, message_remove, message_send, message_sendlater, message_pin, message_react, message_unpin, message_unreact
from src.global_variables import workspace_reset
from src.other import search, users_all
from src.standup import standup_active, standup_send, standup_start
from src.backup import load_data, start_auto_backup


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

# pylint: disable=missing-function-docstring

@APP.before_first_request
def init_data():
    '''Runs functions at slackr launch before first request.'''
    load_data()
    start_auto_backup(5)

@APP.before_first_request
def init_data():
    '''Runs functions at slackr launch before first request.'''
    load_data()
    start_auto_backup(5)

@APP.route('/auth/register', methods=['POST'])
def auth_register_wsgi():
    json = request.get_json()
    return jsonify(
        auth_register(json['email'], json['password'], json['name_first'],
                      json['name_last']))


@APP.route('/auth/login', methods=['POST'])
def auth_login_wsgi():
    json = request.get_json()
    return jsonify(auth_login(json['email'], json['password']))


@APP.route('/auth/logout', methods=['POST'])
def auth_logout_wsgi():
    json = request.get_json()
    #token = request.cookies.get('token') TODO
    return jsonify(auth_logout(json['token']))


@APP.route('/channel/invite', methods=['POST'])
def channel_invite_wsgi():
    json = request.get_json()
    return jsonify(
        channel_invite(json['token'], int(json['channel_id']),
                       int(json['u_id'])))


@APP.route('/channel/details', methods=['GET'])
def channel_details_wsgi():
    json = request.args
    return jsonify(channel_details(json['token'], int(json['channel_id'])))


@APP.route('/channel/messages', methods=['GET'])
def channel_messages_wsgi():
    json = request.args
    return jsonify(
        channel_messages(json['token'], int(json['channel_id']),
                         int(json['start'])))


@APP.route('/channel/leave', methods=['POST'])
def channel_leave_wsgi():
    json = request.get_json()
    return jsonify(channel_leave(json['token'], int(json['channel_id'])))


@APP.route('/channel/join', methods=['POST'])
def channel_join_wsgi():
    json = request.get_json()
    return jsonify(channel_join(json['token'], int(json['channel_id'])))


@APP.route('/channel/addowner', methods=['POST'])
def channel_addowner_wsgi():
    json = request.get_json()
    return jsonify(
        channel_addowner(json['token'], int(json['channel_id']),
                         int(json['u_id'])))


@APP.route('/channel/removeowner', methods=['POST'])
def channel_removeowner_wsgi():
    json = request.get_json()
    return jsonify(
        channel_removeowner(json['token'], int(json['channel_id']),
                            int(json['u_id'])))


@APP.route('/channels/list', methods=['GET'])
def channels_list_wsgi():
    json = request.args
    return jsonify(channels_list(json['token']))


@APP.route('/channels/listall', methods=['GET'])
def channels_listall_wsgi():
    json = request.args
    return jsonify(channels_listall(json['token']))


@APP.route('/channels/create', methods=['POST'])
def channels_create_wsgi():
    json = request.get_json()
    return jsonify(
        channels_create(json['token'], json['name'], json['is_public']))


@APP.route('/message/send', methods=['POST'])
def message_send_wsgi():
    json = request.get_json()
    return jsonify(
        message_send(json['token'], int(int(json['channel_id'])),
                     json['message']))


@APP.route('/message/sendlater', methods=['POST'])
def message_sendlater_wsgi():
    json = request.get_json()
    return jsonify(
        message_sendlater(json['token'], int(json['channel_id']),
                          json['message'], json['time_sent']))


@APP.route('/message/react', methods=['POST'])
def message_react_wsgi():
    json = request.get_json()
    return jsonify(
        message_react(json['token'], int(json['message_id']),
                      json['react_id']))


@APP.route('/message/unreact', methods=['POST'])
def message_unreact_wsgi():
    json = request.get_json()
    return jsonify(
        message_unreact(json['token'], int(json['message_id']),
                        json['react_id']))


@APP.route('/message/pin', methods=['POST'])
def message_pin_wsgi():
    json = request.get_json()
    return jsonify(message_pin(json['token'], int(json['message_id'])))


@APP.route('/message/unpin', methods=['POST'])
def message_unpin_wsgi():
    json = request.get_json()
    return jsonify(message_unpin(json['token'], json['message_id']))


@APP.route('/message/remove', methods=['DELETE'])
def message_remove_wsgi():
    json = request.get_json()
    return jsonify(message_remove(json['token'], int(json['message_id'])))


@APP.route('/message/edit', methods=['PUT'])
def message_edit_wsgi():
    json = request.get_json()
    return jsonify(
        message_edit(json['token'], int(json['message_id']), json['message']))


@APP.route('/user/profile', methods=['GET'])
def user_profile_wsgi():
    json = request.args
    return jsonify(user_profile(json['token'], int(json['u_id'])))


@APP.route('/user/profile/setname', methods=['PUT'])
def user_profile_setname_wsgi():
    json = request.get_json()
    return jsonify(
        user_profile_setname(json['token'], json['name_first'],
                             json['name_last']))


@APP.route('/user/profile/setemail', methods=['PUT'])
def user_profile_setemail_wsgi():
    json = request.get_json()
    return jsonify(user_profile_setemail(json['token'], json['email']))


@APP.route('/user/profile/sethandle', methods=['PUT'])
def user_profile_sethandle_wsgi():
    json = request.get_json()
    return jsonify(user_profile_sethandle(json['token'], json['handle_str']))


@APP.route('/user/profile/uploadphoto', methods=['POST'])
def user_profile_setimage_wsgi():
    json = request.get_json()
    return jsonify(
        user_profile_setimage(json['token'], json['img_url'], int(json['x_start']),
                              int(json['y_start']), int(json['x_end']), int(json['y_end'])))


@APP.route('/imgurl/<string:filename>', methods=['GET'])
def image_wsgi(filename):
    image_folder = os.path.join(os.getcwd(), './images/cropped')
    if os.path.isfile(os.path.join(image_folder, filename)):
        return send_from_directory(image_folder, filename)
    return send_file(os.path.join(image_folder, 'default.png'))

@APP.route('/users/all', methods=['GET'])
def users_all_wsgi():
    json = request.args
    return jsonify(users_all(json['token']))


@APP.route('/search', methods=['GET'])
def search_wsgi():
    json = request.args
    return jsonify(search(json['token'], json['query_str']))


@APP.route('/standup/start', methods=['POST'])
def standup_start_wsgi():
    json = request.get_json()
    return jsonify(
        standup_start(json['token'], int(json['channel_id']), json['length']))


@APP.route('/standup/active', methods=['GET'])
def standup_active_wsgi():
    json = request.args
    return jsonify(standup_active(json['token'], int(json['channel_id'])))


@APP.route('/standup/send', methods=['POST'])
def standup_send_wsgi():
    json = request.get_json()
    return jsonify(
        standup_send(json['token'], int(json['channel_id']), json['message']))


@APP.route('/admin/userpermission/change', methods=['POST'])
def admin_userpermission_change_wsgi():
    json = request.get_json()
    return jsonify(
        permission_change(json['token'], int(json['u_id']),
                               json['permission_id']))


@APP.route('/workspace/reset', methods=['POST'])
def workspace_reset_wsgi():
    return jsonify(workspace_reset())

@APP.route('/admin/user/remove', methods=['DELETE'])
def admin_user_remove():
    json = request.get_json()
    return jsonify(
            user_remove(json['token'], int(json['u_id']))
            )

# pylint: enable=missing-function-docstring

if __name__ == "__main__":
    APP.debug = True  #TODO: remove this for production
    APP.run(port=(int(sys.argv[1]) if len(sys.argv) == 2 else 8080))
