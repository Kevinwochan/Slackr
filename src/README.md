# Type Defintions
There are 3 global variables:
- CHANNELS
    - Currently declared in scr.channels
- USERS
    - Currently declared in scr.auth
- TOKENS
    - Currently declared in scr.auth

## CHANNELS
Channels is a dictionary
``` 
    if you want channnel information you can access it using it's channel id like
    channel = CHANNELS[channel_id]

    each channel is a dictionary 
    { 
        'name': 'channel_name',
        'owners': [user_id1, user_id2],
        'members': [user_id2, user_id3],
        'messages' : [message1, message2],
        'is_public' : True
    }

    each message is a dictionary with a unix timestamp
    {
        'timestamp': 1584538791 ,
        'content' : 'this is the message content',
        'reacts' : [ 
                    'user_id': user_id1,
                     'emoji' : U+1F600  # this is a s mily face in unicode
                   ]
    }

```
## Messages
is a dictionary
```
    each message in CHANNELS[channel_id]['messges'] a dictionary with a unix timestamp
    {
        'timestamp': 1584538791 ,
        'message' : 'this is the message content',
        'reacts' : [ 
                    'user_id': user_id1,
                     'emoji' : U+1F600  # this is a s mily face in unicode
                   ]
    }

```



## USERS
USERS is a dictionary with each item in the list representing a user
each user in USERS is also a dictionary
```
    user = USERS[u_id] # Example of accessing a user with a u_id
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
```

# Backend
## Installation
In order for everything to run you need to have the following installed:

```
pip install flask pytest pylint yapf python-dotenv
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


