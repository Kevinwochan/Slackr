Functions Assumptions(users_all)
    1. Assuming the dictionaries in the ouput list with the chronological order
    2. Assuming the input token is a valid token from one of the members
    3. Assuming the auth.auth_register and user.user_profile works well
    
Functions Assumptions(search)
    1. Assuming the orfer in messages list is chronological
    2. Assuming the time created of each message is 12345
    3. Assuming the search function only search for the latest fifty messages in every channel

Functions Assumptions(channel_invite)
    1. Functions AccessError, InputError, auth_register, channel_details, channels_create works well
    2. If the user is invited twice or more through a valid invitation, the user is still in that channel
    3. If the user invite itself to the channel where he/she is already a member, nothing will happens
    

