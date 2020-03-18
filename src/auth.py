TOKENS = []
'''
TOKENS[u_id] = 'a valid token for u_id'
a list of TOKENS generated from a user successffully logging in
'''


USERS = {}
'''
a list of users.
each user is a dictionary like:
    user = USERS[u_id]
    user = {
        'u_id': 2,
        'email' : 'z5555555@unsw.edu.au',
        'name_first': 'Hayden', 
        'name_last' : 'Smith', 
         etc...
        handle_str,
        password,
        username
    }
'''

def auth_login(email, password):
    return {
        'u_id': 1,
        'token': '12345',
    }

def auth_logout(token):
    return {
        'is_success': True,
    }

def auth_register(email, password, name_first, name_last):
    return {
        'u_id': 1,
        'token': '12345',
    }
