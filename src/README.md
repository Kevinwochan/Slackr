# Backend Documentation
## Installation
In order for everything to run you need to have the following installed:
```
pip install -r requirements.txt # for pip users
pipenv install --dev # ONLY for pipenv users, don't know what this means? dw dont run this.
```
## Running
run the command below
```
sh .env
python3.7 -m flask run
```
e.g

```
$ sh .env
$ python3 -m flask run
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

## Common Errors
### Dependency missing
```
Module not found
```
**Solution**:
dependencies need to be instaled, see the src/README.md for installing dependences

### Incorrect working directory
```
ModuleNotFoundError: No module named 'src'
```
**Solution**:
run everything for the root project directory, ie the folder the contains these files
```
➜  backend git:(iteration-3) ✗ ls -l
total 144
-rw-r--r--  1 kwoc kwoc  3159 Mar 23 18:43 assumptions.md
drwxr-xr-x  2 kwoc kwoc  4096 Mar 26 04:34 htmlcov
drwxr-xr-x  4 kwoc kwoc  4096 Apr 18 23:22 images
drwxr-xr-x 98 kwoc kwoc  4096 Mar 24 00:55 node_modules
-rw-r--r--  1 kwoc kwoc   249 Apr  9 21:35 package.json
-rw-r--r--  1 kwoc kwoc 34884 Mar 24 00:55 package-lock.json
-rwxr-xr-x  1 kwoc kwoc   279 Apr 18 23:22 Pipfile
-rw-r--r--  1 kwoc kwoc 21534 Apr 11 05:26 Pipfile.lock
-rw-r--r--  1 kwoc kwoc 36301 Apr 18 16:45 README.md
-rw-r--r--  1 kwoc kwoc   662 Apr 18 23:22 requirements.txt
-rwxr-xr-x  1 kwoc kwoc   273 Apr 18 23:22 settings.py
-rw-r--r--  1 kwoc kwoc  4275 Apr 18 21:22 slackr_data.p
drwxr-xr-x  3 kwoc kwoc  4096 Apr 18 23:24 src
drwxr-xr-x  5 kwoc kwoc  4096 Apr 18 23:24 tests
➜  backend git:(iteration-3) ✗ python3 -m flask run
```

### Environment variables havent been set
```
"No such file or directory"
user['profile_img_url'] == 'None/imgurl/adfasdfawdf.png'
```
or 
```
No module named src
```
or 
```
Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
k
```
**Solution**: 
run the below command
```
sh .env
```
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

These are declared in the file global_variables.py. To access these global variables you must import the corresponding function from src.global_variables.py

For example, to access global_channels, use the following code:
'''
from src.global_variables import get_channels
channels = get_channels()
'''
Any variable name can be used in place of 'channels'.

## global_channels
global_channels is a dictionary
``` 
    if you want channnel information you can access it using it's channel id like:

    from src.global_variables import get_channels
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
is a list.
```
    each message in CHANNELS[channel_id]['messages'] a dictionary with a unix timestamp
    {
        'u_id': 1,
        'message_id': 1,
        'time_created': 1584538791 ,
        'message' : 'this is the message content',
        'reacts' : [ 
            {
                'react_id': react_id,
                'u_ids': [], #a list of u_id's of people who have reacted
                'is_this_user_reacted': True
            },
        ]
        'is_pinned': False
    }

```



## global_users
global_users is a dictionary with each item in the list representing a user.
Each user in global_users is also a dictionary
```
    from src.global_variables import get_users
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



