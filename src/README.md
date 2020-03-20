# Type Defintions
There are 3 global variables:
- CHANNELS
- USERS
- SLACKR_OWNERS

## CHANNELS
Channels is a dictionary

``` 
    if you want channnel information you can access it using it's channel id like
    channel = CHANNELS[channel_id]

    each channel is a dictionary 
    { 
        'owners': []
        'members': []
        'messages' : [message1, message2] 
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

## SLACKR OWNER
Is a single u_id that can
- reset the workspace 
- make any user a owner of a channel
- Force any user that is now a channel owner to leave a channel

Change the slackr id by asssigning it to a valid user_id
```
    SLACKR_OWNER = 1
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
python3 server.py
```
e.g

```
$ ls
assumptions.md	Pipfile  README.md  src
$ cd src
$ ls       
app.py	auth.py  auth_test.py  channel.py  channels.py	conftest.py  echo.py  error.py	__init__.py  message.py  other.py  Pipfile  Pipfile.lock  __pycache__  README.md  tests  user.py  utils.py
$ flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You can now open firefox/google chrome at http://127.0.0.1:5000/ to view the api


## Testing TODO

# Frontend TODO


