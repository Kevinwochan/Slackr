# **Assumptions**
## General assumptions

- user ids begin with id 0
- channel ids begin with id 0
- Before each test function is run, there is no existing slackr data
- After each test function is run, slackr data is deleted

## Authenication
- there is a method of deleting/de-registering users
- Registration has been implemented
- logging in has been implemented

## Channel
- there isn't a Slackr Owner in these tests
- when you create a channel, you automatically join it as Owner
- there are no existing channels or users when each test is run
- channels_details is implemented to verify members have been added/removed
- the first person to join/create a channel is Owner of that channel there isn't a Slackr owner


## Channels
- channels_test.py assumes that auth_register, auth_logout have been tested

**channels_create**
- channels_create raises an InputError if given empty name
- 2 or more channels can be created with the same name - they will have to be differentiated by channel_id alone
  
**channels_list**
- channels_list will return an empty list (in a dictionary) if there are no existing channels
- channels_list lists channels in the order that the the user became a member of them

**channels_listall**
- channels_listall() will return an empty list (in a dictionary) if there are no existing channels
- channels_listall lists channels in the order that they are created
- All channels are listed by channels_listall, regardless of if they are private or not
