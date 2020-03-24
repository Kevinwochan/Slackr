# Type Defintions
- global_channels
    - accessed using the function get_channels()
- global_users
    - accessed using the function get_users()
- global_valid_tokens
    - accessed using the function get_valid_tokens()
- global_slackr_owners
    - provides the user_ids of the slackr owners
    - access with get_slackr_owners()

These are declared in the file global_variables.py. To access these global variables you must import the corresponding function from global_variables.py

For example, to access global_channels, use the following code:
'''
from global_variables import get_channels
channels = get_channels()
'''
Any variable name can be used in place of 'channels'.

## global_channels
global_channels is a dictionary
``` 
    if you want channnel information you can access it using it's channel id like:

    from global_variables import get_channels
    glob_channels = get_channels()
    channel = glob_channels[channel_id]

    each channel is a dictionary 
    { 
        'name': 'channel_name',
        'owners': [0, 1],  # a list of user_ids
        'members': [2, 3],
        'messages' : [message1, message2], # a lsit of messages sorted by most recent first, see below for type def
        'is_public' : True
    }
```

## Messages
is a dictionary
```
    each message in CHANNELS[channel_id]['messges'] a dictionary with a unix timestamp
    {
        'message_id': 1
        'timestamp': 1584538791 ,
        'message' : 'this is the message content',
        'reacts' : [ 
                    'user_id': user_id1,
                     'emoji' : U+1F600  # this is a s mily face in unicode
                   ]
    }

```



## global_users
global_users is a dictionary with each item in the list representing a user.
Each user in global_users is also a dictionary
```
    from global_variables import get_users
    glob_users = get_users()

    user = glob_users[u_id] # Example of accessing a user with a u_id
    user = {
        'email' : 'z5555555@unsw.edu.au',
        'name_first': 'Hayden', 
        'name_last' : 'Smith', 
         etc...
        handle_str,
    }
```

## global_valid_tokens
global_valid_tokens is a list of all active JWTs1.
Access this by using the function get_valid_tokens.

NOTE: If youre accessing this variable to check if a token is valid, USE THE FUNCTIONS IN utils.py. i.e. check_token()
Generally, you should not need to access this variable.


# Backend
## Installation
In order for everything to run you need to have the following installed:
```
pip install -r requirements.txt
```
Or if youre comfortable with pipenv run
```
pipenv install --dev
```
## Running
run the command below
```
python3.7 src/server.py
```
e.g

```
$ python3 src/server.py 
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 358-897-093
```

You can now open firefox/google chrome at http://127.0.0.1:8080/ to view the api


## Testing TODO

# Frontend TODO


