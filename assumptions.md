
## **Other**
**users_all**
1. Assuming the dictionaries in the ouput list with the chronological order
2. Assuming the input token is a valid token from one of the members
3. Assuming the auth.auth_register and user.user_profile works well
    
**search assumptions**
N/A

 1. Assuming the orfer in messages list is chronological
 2. Assuming the time created of each message is 12345
 3. Assuming the search function only search for the latest fifty messages in every channel

## **Channel**
**channel_invite**
 1. Functions AccessError, InputError, auth_register, channel_details, channels_create works well
 2. If the user is invited twice or more through a valid invitation, the user is still in that channel
 3. If the user invite itself to the channel where he/she is already a member, nothing will happens



## **Channels**
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
