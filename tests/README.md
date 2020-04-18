# Testing

NOTE: these instructions from your the gitlab repo root directory i.e the directory with the folder src, requirements.txt etc..

### Running pytest
```
python3 -m pytest tests/
```
### Generating a report
```
python3 -m coverage run --source=src -m pytest tests
python3 -m coverage report # generates an terminal summary
python3 -m coverage html -d report # generates a html summary
```

This will work on your local machine or CSE machine. If you have any troubles delete all folders called "__pycache__"

### Examples
```
weber % ls -l
total 64
-rw-r----- 1 z5113136 z5113136   236 Mar 29 12:13 Pipfile
-rw-r----- 1 z5113136 z5113136 33607 Mar 29 12:13 README.md
-rw-r----- 1 z5113136 z5113136  3159 Mar 29 12:13 assumptions.md
-rw-r----- 1 z5113136 z5113136   249 Mar 29 12:13 package.json
-rw-r----- 1 z5113136 z5113136    39 Mar 29 12:18 requirements.txt
-rw-r----- 1 z5113136 z5113136    89 Mar 29 12:46 setup.py
drwxr-x--- 4 z5113136 z5113136  4096 Mar 29 13:00 src
drwxr-x--- 3 z5113136 z5113136  4096 Mar 29 12:20 tests
weber % python3 -m coverage run --source=src/pytest tests
Can't find '__main__' module in 'tests'
weber % python3 -m coverage run --source=src/ -m pytest tests
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.7.3, pytest-3.10.1, py-1.7.0, pluggy-0.8.0
rootdir: /tmp_amd/adams/export/adams/2/z5113136/1531/proj, inifile:
collected 110 items                                                                                                                                                                                               

tests/integration/auth_test.py ...........
tests/integration/channel_owner_test.py .........
tests/integration/channel_user_test.py ...................
tests/integration/channels_test.py ..............
tests/integration/message_test.py ...............
tests/integration/other_test.py FFFFFFF..        
tests/integration/user_test.py ..................
tests/integration/utils_test.py ...              

weber % python3 -m coverage report
Name                      Stmts   Miss  Cover
---------------------------------------------
src/__init__.py               0      0   100%
src/auth.py                  22      0   100%
src/auth_helper.py           62      1    98%
src/channel.py               98      2    98%
src/channels.py              19      0   100%
src/error.py                  7      0   100%
src/global_variables.py      28      0   100%
src/message.py              132     62    53%
src/other.py                  8      0   100%
src/server.py                27     27     0%
src/user.py                  63      4    94%
src/utils.py                 26      0   100%
---------------------------------------------
TOTAL                       492     96    80%

```

### Common Errors
#### Error
```
Module not found
```
#### Solution
dependencies need to be instaled, see the src/README.md for installing dependences


#### Error
```
ModuleNotFoundError: No module named 'src'
```
#### Solution
execute tests using `python3 -m pytest` instead of directly calling pytests, this is to preserve your current working directory as the project root directory 

#### Error
```
user['profile_img_url'] == 'None/imgurl/adfasdfawdf.png'
```
the profile image code relies on an environment variables to construct a valid image URL.
#### Solution
```
export URL=8080
```
or whichever port youre using for the backend

