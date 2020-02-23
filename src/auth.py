def login(email, password):
    return {
        'u_id': 1,
        'token': '12345',
    }

def logout(token):
    return {
        'is_success': True,
    }

def register(email, password, name_first, name_last):
    return {
        'u_id': 1,
        'token': '12345',
    }
