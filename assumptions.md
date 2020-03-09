# **Assumptions**
## General assumptions

- Parameters are given as the correct type
- Functions that result in errors perform no actions

Functions should be implemented in this order:
1. Registration
2. Login
3. Logout

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
  
**channel_invite**
 - Functions AccessError, InputError, auth_register, channel_details, channels_create works well
- If the user is invited twice or more through a valid invitation, the user is still in that channel
 - If the user invite itself to the channel where he/she is already a member, nothing will happens


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

- channels_test.py assumes that auth_register, auth_logout have been tested

## User


## **Other**
**users_all**
1. Assuming the dictionaries in the ouput list with the chronological order
2. Assuming the input token is a valid token from one of the members
3. Assuming the auth.auth_register and user.user_profile works well
    
**search**
 1. Assuming the orfer in messages list is chronological
 2. Assuming the time created of each message is 12345
 3. Assuming the search function only search for the latest fifty messages in every channel


### **Message**
- channels_create, channel_join and auth_register have already been implemented
- Message id's are not unique to a channel
- there are no existing channels or users before each test
- no new features will cause a conflict in the keys returned by auth_register and channel_create
- channels and users are deleted after each test
- channels are initialised with 0 messages
- channels begin with message_id 0

**def message_send**
- A user cannot send an empty message, empty messages will throw an input error

**def message_edit**
- A user cannot replace a message with an empty string. This will throw an input error
