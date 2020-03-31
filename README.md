# COMP1531 Major Project

A video describing this project and the background here can be found here.

## Aims:

* To provide students with hands on experience testing, developing, and maintaining a backend server in python.
* To develop students' problem solving skills in relation to the software development lifecycle.
* Learn to work effectively as part of a team by managing your project, planning, and allocation of responsibilities among the members of your team.
* Gain experience in collaborating through the use of a source control and other associated modern team-based tools.
* Apply appropriate design practices and methodologies in the development of their solution
* Develop an appreciation for product design and an intuition of how a typical customer will use a product.

## Changelog

* 03/03: Added description for users_all
* 05/03: Reiterated not to modify/move stub files as per week 2 lecture; submission open comment
* 09/03:
  * "set handle" minimum length set as 2
  * Clarification that all ids uniquely identify an entity
  * All "between" references clarified to be inclusive
  * Clarity on how search results are sorted
  * password reset, message sendlater, message react/pin, profile pic uploads, standups, and permision changes added
* 14/03: PLEASE READ
  * Added "reacts, is_pinned" to messages data type
  * Added "reacts" data type
  * Permission ID's clarified for global permissions
## Overview

An overview of this background and this project can be found in a short video found [HERE](https://youtu.be/Mzg3UGv3TSw). **Please note that this video is from 19T3, so the marking breakdown has changed slightly. This video should be used to supplement explanations in the lecture, which can be found in lecture 2 of week 2.**

To manage the transition from trimesters to hexamesters in 2020, UNSW has established a new focus on building an in-house digital collaboration and communication tool for groups and teams to support the high intensity learning environment.

Rather than re-invent the wheel, UNSW has decided that it finds the functionality of **<a href="https://slack.com/intl/en-au/">Slack</a>** to be nearly exactly what it needs. For this reason, UNSW has contracted out Lit Pty Ltd (a small software business run by Hayden) to build the new product. In UNSW's attempt to connect with the younger and more "hip" generation that fell in love with flickr, Tumblr, etc, they would like to call the new UNSW-based product **slackr**.

Lit Pty Ltd has sub-contracted two software firms:

* Catdog Pty Ltd (two software developers, Sally and Bob, who will build the initial web-based GUI)
* YourTeam Pty Ltd (a team of talented misfits completing COMP1531 in 20T1), who will build the backend python server and possibly assist in the GUI later in the project

In summary, UNSW contracts Lit Pty Ltd, who sub contracts:

* Catdog (Sally and Bob) for front end work
* YourTeam (you and others) for backend work

Lit Pty Ltd met with Sally and Bob (the front end development team) 2 weeks ago to brief them on this project. While you are still trying to get up to speed on the requirements of this project, Sally and Bob understand the requirements of the project very well.

Because of this they have already specified a **common interface** for the front end and backend to operate on. This allows both parties to go off and do their own development and testing under the assumption that both parties comply will comply with the common interface. This is the interface **you are required to use**

Beside the information available in the interface that Sally and Bob provided, you have been told (so far) that the features of slackr that UNSW would like to see implemented include:

1. Ability to login, register if not registered, and log out
2. Ability to reset password if forgotten it
3. Ability to see a list of channels
4. Ability to create a channel, join a channel, invite someone else to a channel, and leave a channel
5. Within a channel, ability to view all messages, view the members of the channel, and the details of the channel
6. Within a channel, ability to send a message now, or to send a message at a specified time in the future
7. Within a channel, ability to edit, remove, pin, unpin, react, or unreact to a message
8. Ability to view user anyone's user profile, and modify a user's own profile (name, email, handle, and profile photo)
9. Ability to search for messages based on a search string
10. Ability to modify a user's privileges: (MEMBER, OWNER)
11. Ability to begin a "standup", which is an X minute period where users can send messages that at the end of the period will automatically be collated and summarised to all users

To get further information about the requirements, Lit Pty Ltd has provided a pre-recorded video briefing (with verbal and visual descriptions) of what UNSW would like to see in the Slackr product. This can be found [HERE](https://youtu.be/0_jaxpOSoj4). Hint: **This video should be the main source of information from which you derive your user stories**

## Progress check-in

During your lab class, in weeks without demonstrations (see below), you and your team will conduct a short stand-up in the presence of your tutor. Each member of the team will briefly state what they have done in the past week, what they intend to do over the next week, and what issues they faced or are currently facing. This is so your tutor, who is acting as a representative of the client, is kept informed of your progress. They will make note of your presence and may ask you to elaborate on the work you've done.

## Iteration 1: Test Driven Development

**Completed**

## Iteration 2: Design and Implementation

**Completed**

## Iteration 3: Maintenance and Extensions

### Task

In this iteration, you will be demonstrating the long-term viability of your system by ensuring that it is maintainable and that it can be usefully extended if needed.

1. Fix any outstanding bugs and complete any components that were not full implemented for the iteration 2 deadline. In doing this, you should ensure that your code is of sufficiently high quality for it to be maintained. Consider principles like DRY, KISS, top-down thinking and encapsulation. Furthermore, ensure all your functions are documented with Pydoc using a consistent style. Also, you should ensure that your backend implements the interface in this document exactly. Note that, in this iteration, Sally and Bob fixed some minor issues they considered bugs in the interface specification.

2. Implement the `/passwordreset/request` and `/passwordreset/reset` routes that have been added to the table below. By doing this, the "Forgot your password" feature of the frontend should now work.

3. Modify your backend such that it is able to persist and reload its data store. The persistance should happen at regular intervals so that in the event of unexpected program termination (e.g. sudden power outage) a minimal amount of data is lost. You may implement this using whatever method of serialisation you prefer (e.g. pickle, JSON).

4. Implement the `/user/profile/uploadphoto` route as described in table below. If you do this correctly, you should be able to set a profile image when using the frontend. Note that you may need to do your own research into flask features not covered in this course, and python packages for manipulating images. Any additional packages you use need to be added to `requirements.txt`.

5. Add support for slackr owners to remove users from slackr. This requires modifying both the backend and frontend. You should modify the backend by implementing `/admin/user/remove` in the table below. For the frontend, add an additional entry to the admin menu that provides an interface for removing users.

6. Allow users to relax and play a game of [Hangman](https://en.wikipedia.org/wiki/Hangman_(game)) in slackr. If the command `/hangman` is typed into a channel, it should start a game where the users of the channel cooperatively try to guess a word or phrase letter by letter. See more details below.

### Hangman

After a game of Hangman has been started any user in the channel can type `/guess X` where `X` is an individual letter. If that letter is contained in the word or phrase they're trying to guess, the app should indicate *where* it occurs. If it does not occur, more of the hangman is drawn. There is a *lot* of flexibility in how you achieve this. It can be done only by modifying the backend and relying on messages to communicate the state of the game (e.g. after making a guess, the "Hangman" posts a message with a drawing of the hangman in ASCII/emoji art). Alternatively you can modify the frontend, if you want to experiment with fancier graphics.

The app should use words and phrases from an external source, not just a small handful hardcoded into the app. One suitable source is `/usr/share/dict/words` available on Unix-based systems. Alternatively, the python [wikiquote](https://github.com/federicotdn/wikiquote) module is available via pip and can be used to retrieve quotes and phrases from [Wikiquote](https://www.wikiquote.org/).

Note that this part of the specification is deliberately open-ended. You're free to make your own creative choices in exactly how the game should work, as long as the end result is something that could be fairly described as Hangman.

### Submission

This iteration is due to be submitted at 8pm Sunday 19th April (**week 9**). You will then be demonstrating this in your week 10. All team members **must** attend the online demonstration, or they will not receive a mark.

To submit, one team member must run this command in the CSE environment:

```sh
1531 submit iteration3
```

This will submit the contents of your repo on GitLab. **Make sure that everything you intend to submit is included in your repo on the master branch**.

### Marking Criteria

|Section|Weighting|Criteria|
|---|---|---|
|Maintenance|20%|<ul><li>Code contains minimal repetition or complexity</li><li>Code is generally understandable for an average python programmer</li><li>Functions are documented with Pydoc</li><li>Code is pylint compliant without unecessary warning suppression</li></ul>|
|Password reset|5%|<ul><li>Reset emails are sent</li><li>Emails contain valid reset codes</li></ul>|
|Persistence|15%|<ul><li>Data is persisted at regular intervals</li><li>Persisted data is reloaded on server start</li></ul>|
|Profile photo upload|10%|<ul><li>Appropriate use of external library to resize images</li><li>Images are stored such that they are reachable via an automatically generated URL</li></ul>|
|User removal|20%|<ul><li>Users can be removed via API call</li><li>Frontend modified to provide an interface for removal</li><li>Javascript code is consistent with the rest of the frontend in terms of style</li><li>Added UI components are simple, clear and consistent with the rest of the UI</li></ul>|
|Hangman|20%|<ul><li>A game of hangman can be played in the channel</li><li>Words/phrases taken from an appropriate source</li><li>The state of the game (incomplete word/phrase, hangman, previous guesses, etc.) are communicated effectively</li><li>Any changes to the frontend are consistent.</li></ul>|
|Teamwork and Git|10%|<ul><li>A generally equal contribution between team members</li><li>Effective use of merge requests (from branches being made) across the team (minimum 12 MRs)</li><li>Effective use of course-provided slack, demonstrating an ability to communicate and manage effectively digitally</li><li>Use of task board on Gitlab to track and manage tasks</li><li>Effective use of agile methods such as standups</li></ul>|

### Demonstration

When you demonstrate this iteration in your week 4 lab (week 5 for monday tutes), it will consist of a 15 minute Q&A in front of your tutorial class.

## Interface specifications from Sally and Bob

### Data types

|Variable name|Type|
|-------------|----|
|named exactly **email**|string|
|named exactly **id**|integer|
|named exactly **length**|integer|
|named exactly **password**|string|
|named exactly **token**|string|
|named exactly **message**|string|
|contains substring **name**|string|
|contains substring **code**|string|
|has prefix **is_**|boolean|
|has prefix **time_**|integer (unix timestamp), [check this out](https://www.tutorialspoint.com/How-to-convert-Python-date-to-Unix-timestamp)|
|has suffix **_id**|integer|
|has suffix **_url**|string|
|has suffix **_str**|string|
|has suffix **end**|integer|
|has suffix **start**|integer|
|(outputs only) named exactly **user**|Dictionary containing u_id, email, name_first, name_last, handle_str|
|(outputs only) named exactly **users**|List of dictionaries, where each dictionary contains types u_id, email, name_first, name_last, handle_str|
|(outputs only) named exactly **messages**|List of dictionaries, where each dictionary contains types { message_id, u_id, message, time_created, reacts, is_pinned  }|
|(outputs only) named exactly **channels**|List of dictionaries, where each dictionary contains types { channel_id, name }|
|(outputs only) name ends in **members**|List of dictionaries, where each dictionary contains types { u_id, name_first, name_last }|
|(outputs only) name ends in **reacts**|List of dictionaries, where each dictionary contains types { react_id, u_ids, is_this_user_reacted } where react_id is the id of a react, and u_ids is a list of user id's of people who've reacted for that react. is_this_user_reacted is whether or not the authorised user has been one of the reacts to this post|


### profile_img_url & image uploads

For outputs with data pertaining to a user, a profile_img_url is present. When images are uploaded for a user profile, after processing them you should store them on the server such that your server now locally has a copy of the cropped image of the original file linked. Then, the profile_img_url should be a URL to the server, such as http://localhost:5001/imgurl/adfnajnerkn23k4234.jpg (a unique url you generate).

Note: This is most likely the most challenging part of the project. Don't get lost in this, we would strongly recommend most teams complete this capability *last*.

### Token

Many of these functions (nearly all of them) need to be called from the perspective of a user who is logged in already. When calling these "authorised" functions, we need to know:
1) Which user is calling it
2) That the person who claims they are that user, is actually that user

We could solve this trivially by storing the user ID of the logged in user on the front end, and every time the front end (from Sally and Bob) calls your background, they just sent a user ID. This solves our first problem (1), but doesn't solve our second problem! Because someone could just "hack" the front end and change their user id and then log themselves in as someone else.

To solve this when a user logs in or registers the backend should return a "token" (an authorisation hash) that the front end will store and pass into most of your functions in future. When these "authorised" functions are called, you can check if a token is valid, and determine the user ID.

### Error raising for the frontend

For errors to be appropriately raised on the frontend, they must be raised by the following:

```python
if True: # condition here
    raise InputError(description='Description of problem')
```

The types in error.py have been modified appropriately for you.

### Reacts

The only React ID currently associated with the frontend is React ID 1, which is a thumbs up. You are welcome to add more (this will require some frontend work)


### Permissions:
 * Members in a channel have one of two channel permissions.
   * 1) Owner of the channel (the person who created it, and whoever else that creator adds)
   * 2) Members of the channel
 * Slackr user's have two global permissions
   * 1) Owners, who can also modify other owners' permissions. (permission_id 1)
   * 2) Members, who do not have any special permissions. (permission_id 2)
 * All slackr users are by default members, except for the very first user who signs up, who is an owner

A user's primary permissions are their global permissions. Then the channel permissions are layered on top. For example:
* An owner of slackr has owner privileges in every channel they've joined
* A member of slackr is a member in channels they are not owners of
* A member of slackr is an owner in channels they are owners of

### Standups

Once standups are finished, all of the messages sent to standup/send are packaged together in *one single message* posted by *the user who started the standup* and sent as a message to the channel the standup was started in, timestamped at the moment the standup finished.

The structure of the packaged message is like this:

[message_sender1_handle]: [message1]

[message_sender2_handle]: [message2]

[message_sender3_handle]: [message3]

[message_sender4_handle]: [message4]

For example:

```txt
hayden: I ate a catfish
rob: I went to kmart
michelle: I ate a toaster
isaac: my catfish ate a toaster
```

Standups can be started on the frontend by typing "/standup X", where X is the number of seconds that the standup lasts for, into the message input and clicking send.

### Errors for all functions

**AccessError**
 * For all functions except auth/register, auth/login
 * Error thrown when token passed in is not a valid token

### Pagination
The behaviour in which channel_messages returns data is called **pagination**. It's a commonly used method when it comes to getting theoretially unbounded amounts of data from a server to display on a page in chunks. Most of the timelines you know and love - Facebook, Instagram, LinkedIn - do this.

For example, if we imagine a user with token "12345" is trying to read messages from channel with ID 6, and this channel has 124 messages in it, 3 calls from the client to the server would be made. These calls, and their corresponding return values would be:
 * channel_messages("12345", 6, 0) => { [messages], 0, 50 }
 * channel_messages("12345", 6, 50) => { [messages], 50, 100 }
 * channel_messages("12345", 6, 100) => { [messages], 100, -1 }

### Other Comments
* All IDs (e.g. user id, channel id) uniquely identify a data item for its entire existence. Even if that item is removed, the ID cannot be reused for any new or other existing items.

### Interface

|HTTP Route|HTTP Method|Parameters|Return type|Exceptions|Description|
|------------|-------------|-------------|----------|-----------|----------|
|auth/login|POST|(email, password)|{ u_id, token }|**InputError** when any of:<ul><li>Email entered is not a valid email using the method provided [here](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) (unless you feel you have a better method)</li><li>Email entered does not belong to a user</li><li>Password is not correct</li></ul> | Given a registered users' email and password and generates a valid token for the user to remain authenticated |
|auth/logout|POST|(token)|{ is_success }|N/A|Given an active token, invalidates the taken to log the user out. If a valid token is given, and the user is successfully logged out, it returns true, otherwise false. |
|auth/register|POST|(email, password, name_first, name_last)|{ u_id, token }|**InputError** when any of:<ul><li>Email entered is not a valid email using the method provided [here](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) (unless you feel you have a better method).</li><li>Email address is already being used by another user</li><li>Password entered is less than 6 characters long</li><li>name_first not is between 1 and 50 characters inclusive in length</li><li>name_last is not between 1 and 50 characters inclusive in length</ul>|Given a user's first and last name, email address, and password, create a new account for them and return a new token for authentication in their session. A handle is generated that is the concatentation of a lowercase-only first name and last name. If the concatenation is longer than 20 characters, it is cutoff at 20 characters. If the handle is already taken, you may modify the handle in any way you see fit to make it unique. |
|auth/passwordreset/request|POST|(email)|{}|N/A|Given an email address, if the user is a registered user, send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, shows that the user trying to reset the password is the one who got sent this email.|
|auth/passwordreset/reset|POST|(reset_code, new_password)|{}|**InputError** when any of:<ul><li>reset_code is not a valid reset code</li><li>Password entered is not a valid password</li>|Given a reset code for a user, set that user's new password to the password provided|
|channel/invite|POST|(token, channel_id, u_id)|{}|**InputError** when any of:<ul><li>channel_id does not refer to a valid channel that the authorised user is part of.</li><li>u_id does not refer to a valid user</li></ul>**AccessError** when<ul><li>the authorised user is not already a member of the channel</li>|Invites a user (with user id u_id) to join a channel with ID channel_id. Once invited the user is added to the channel immediately|
|channel/details|GET|(token, channel_id)|{ name, owner_members, all_members }|**InputError** when any of:<ul><li>Channel ID is not a valid channel</li></ul>**AccessError** when<ul><li>Authorised user is not a member of channel with channel_id</li></ul>|Given a Channel with ID channel_id that the authorised user is part of, provide basic details about the channel|
|channel/messages|GET|(token, channel_id, start)|{ messages, start, end }|**InputError** when any of:<ul><li>Channel ID is not a valid channel</li><li>start is greater than the total number of messages in the channel</li></ul>**AccessError** when<ul><li>Authorised user is not a member of channel with channel_id</li></ul>|Given a Channel with ID channel_id that the authorised user is part of, return up to 50 messages between index "start" and "start + 50" exclusive. Message with index 0 is the most recent message in the channel. This function returns a new index "end" which is the value of "start + 50", or, if this function has returned the least recent messages in the channel, returns -1 in "end" to indicate there are no more messages to load after this return.|
|channel/leave|POST|(token, channel_id)|{}|**InputError** when any of:<ul><li>Channel ID is not a valid channel</li></ul>**AccessError** when<ul><li>Authorised user is not a member of channel with channel_id</li></ul>|Given a channel ID, the user removed as a member of this channel|
|channel/join|POST|(token, channel_id)|{}|**InputError** when any of:<ul><li>Channel ID is not a valid channel</li></ul>**AccessError** when<ul><li>channel_id refers to a channel that is private (when the authorised user is not an owner)</li></ul>|Given a channel_id of a channel that the authorised user can join, adds them to that channel|
|channel/addowner|POST|(token, channel_id, u_id)|{}|**InputError** when any of:<ul><li>Channel ID is not a valid channel</li><li>When user with user id u_id is already an owner of the channel</li></ul>**AccessError** when the authorised user is not an owner of the slackr, or an owner of this channel</li></ul>|Make user with user id u_id an owner of this channel|
|channel/removeowner|POST|(token, channel_id, u_id)|{}|**InputError** when any of:<ul><li>Channel ID is not a valid channel</li><li>When user with user id u_id is not an owner of the channel</li></ul>**AccessError** when the authorised user is not an owner of the slackr, or an owner of this channel</li></ul>|Remove user with user id u_id an owner of this channel|
|channels/list|GET|(token)|{ channels }|N/A|Provide a list of all channels (and their associated details) that the authorised user is part of|
|channels/listall|GET|(token)|{ channels }|N/A|Provide a list of all channels (and their associated details)|
|channels/create|POST|(token, name, is_public)|{ channel_id }|**InputError** when any of:<ul><li>Name is more than 20 characters long</li></ul>|Creates a new channel with that name that is either a public or private channel|
|message/send|POST|(token, channel_id, message)|{ message_id }|**InputError** when any of:<ul><li>Message is more than 1000 characters</li></ul>**AccessError** when: <li> the authorised user has not joined the channel they are trying to post to</li></ul>|Send a message from authorised_user to the channel specified by channel_id|
|message/sendlater|POST|(token, channel_id, message, time_sent)|{ message_id }|**InputError** when any of:<ul><li>Channel ID is not a valid channel</li><li>Message is more than 1000 characters</li><li>Time sent is a time in the past</li></ul>**AccessError** when: <li> the authorised user has not joined the channel they are trying to post to</li></ul>|Send a message from authorised_user to the channel specified by channel_id automatically at a specified time in the future|
|message/react|POST|(token, message_id, react_id)|{}|**InputError** when any of:<ul><li>message_id is not a valid message within a channel that the authorised user has joined</li><li>react_id is not a valid React ID. The only valid react ID the frontend has is 1</li><li>Message with ID message_id already contains an active React with ID react_id from the authorised user</li></ul>|Given a message within a channel the authorised user is part of, add a "react" to that particular message|
|message/unreact|POST|(token, message_id, react_id)|{}|**InputError** 	<ul><li>message_id is not a valid message within a channel that the authorised user has joined</li><li>react_id is not a valid React ID</li><li>Message with ID message_id does not contain an active React with ID react_id</li></ul>|Given a message within a channel the authorised user is part of, remove a "react" to that particular message|
|message/pin|POST|(token, message_id)|{}|**InputError** when any of:<ul><li>message_id is not a valid message</li><li>Message with ID message_id is already pinned</li></ul>**AccessError** when any of:<ul><li>The authorised user is not a member of the channel that the message is within</li><li>The authorised user is not an owner</li></ul>|Given a message within a channel, mark it as "pinned" to be given special display treatment by the frontend|
|message/unpin|POST|(token, message_id)|{}|**InputError** when any of:<ul><li>message_id is not a valid message</li><li>Message with ID message_id is already unpinned</li></ul>**AccessError** when any of:<ul><li>The authorised user is not a member of the channel that the message is within</li><li>The authorised user is not an owner</li></ul>|Given a message within a channel, remove it's mark as unpinned|
|message/remove|DELETE|(token, message_id)|{}|**InputError** when any of:<ul><li>Message (based on ID) no longer exists</li></ul>**AccessError** when none of the following are true:<ul><li>Message with message_id was sent by the authorised user making this request</li><li>The authorised user is an owner of this channel or the slackr</li></ul>|Given a message_id for a message, this message is removed from the channel|
|message/edit|PUT|(token, message_id, message)|{}|**AccessError** when none of the following are true:<ul><li>Message with message_id was sent by the authorised user making this request</li><li>The authorised user is an owner of this channel or the slackr</li></ul>|Given a message, update it's text with new text. If the new message is an empty string, the message is deleted.|
|user/profile|GET|(token, u_id)|{ user }|**InputError** when any of:<ul><li>User with u_id is not a valid user</li></ul>|For a valid user, returns information about their user id, email, first name, last name, and handle|
|user/profile/setname|PUT|(token, name_first, name_last)|{}|**InputError** when any of:<ul><li>name_first is not between 1 and 50 characters inclusive in length</li><li>name_last is not between 1 and 50 characters inclusive in length</ul></ul>|Update the authorised user's first and last name|
|/user/profile/setemail|PUT|(token, email)|{}|**InputError** when any of:<ul><li>Email entered is not a valid email using the method provided [here](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) (unless you feel you have a better method).</li><li>Email address is already being used by another user</li>|Update the authorised user's email address|
|/user/profile/sethandle|PUT|(token, handle_str)|{}|**InputError** when any of:<ul><li>handle_str must be between 2 and 20 characters inclusive</li><li>handle is already used by another user</li></ul>|Update the authorised user's handle (i.e. display name)|
|/user/profile/uploadphoto|POST|(token, img_url, x_start, y_start, x_end, y_end)|{}|**InputError** when any of:<ul><li>img_url returns an HTTP status other than 200.</li><li>any of x_start, y_start, x_end, y_end are not within the dimensions of the image at the URL.</li><li>Image uploaded is not a JPG</li></ul>|Given a URL of an image on the internet, crops the image within bounds (x_start, y_start) and (x_end, y_end). Position (0,0) is the top left.|
|users/all|GET|(token)|{ users}|N/A|Returns a list of all users and their associated details|
|/search|GET|(token, query_str)|{ messages }|N/A|Given a query string, return a collection of messages in all of the channels that the user has joined that match the query. Results are sorted from most recent message to least recent message|
|standup/start|POST|(token, channel_id, length)|{ time_finish }|**InputError** when any of:<ul><li>Channel ID is not a valid channel</li><li>An active standup is currently running in this channel</li></ul>|For a given channel, start the standup period whereby for the next "length" seconds if someone calls "standup_send" with a message, it is buffered during the X second window then at the end of the X second window a message will be added to the message queue in the channel from the user who started the standup. X is an integer that denotes the number of seconds that the standup occurs for|
|standup/active|GET|(token, channel_id)|{ is_active, time_finish }|**InputError** when any of:<ul><li>Channel ID is not a valid channel</li></ul>|For a given channel, return whether a standup is active in it, and what time the standup finishes. If no standup is active, then time_finish returns None|
|standup/send|POST|(token, channel_id, message)|{}|**InputError** when any of:<ul><li>Channel ID is not a valid channel</li><li>Message is more than 1000 characters</li><li>An active standup is not currently running in this channel</li></ul>**AccessError** when<ul><li>The authorised user is not a member of the channel that the message is within</li></ul>|Sending a message to get buffered in the standup queue, assuming a standup is currently active|
|admin/userpermission/change|POST|(token, u_id, permission_id)|{}|**InputError** when any of:<ul><li>u_id does not refer to a valid user<li>permission_id does not refer to a value permission</li></ul>**AccessError** when<ul><li>The authorised user is not an owner</li></ul>|Given a User by their user ID, set their permissions to new permissions described by permission_id|
|admin/user/remove|DELETE|(token, u_id)|{}|**InputError** when:<ul><li>u_id does not refer to a valid user</li></ul>**AccessError** when<ul><li>The authorised user is not an owner of the slackr</li></ul>|Given a User by their user ID, remove the user from the slackr. |
|workspace/reset|POST|()|{}||Resets the workspace state|

## Due Dates and Weightings

|Iteration|Code and report due                  |Demonstration to tutor(s)      |Assessment weighting of project (%)|
|---------|-------------------------------------|-------------------------------|-----------------------------------|
|   1     |8pm Monday 9th March (**week 4**)    |In YOUR **week 4** laboratory  |30%                                |
|   2     |8pm Sunday 29th March (**week 6**)   |In YOUR **week 7** laboratory  |40%                                |
|   3     |8pm Sunday 19th April (**week 9**)   |In YOUR **week 10** laboratory |30%                                |

## Working with the frontend

Every group has had a new repository created for them since iteration 2. It's URL is *https://gitlab.cse.unsw.edu.au/COMP1531/20T1frontend/[yourgroupname]*. Instructions of how to have your frontend use your backend are there.

If you run the frontend at the same time as your flask server is running on the backend, then you can power the frontend via your backend.

### Frontend Demo

A **working example of the frontend** can be used at [https://www.slackr.com.au](https://www.slackr.com.au)

The data is reset daily, but you can use this link to play around and get a feel for how the application should behave.

## Expectations

While it is up to you as a team to decide how work is distributed between you, for the purpose of assessment there are certain key criteria all members must.

* Code contribution
* Documentation contribution
* Usage of git/GitLab
* Attendance
* Peer assessment
* Academic conduct

The details of each of these is below.

While, in general, all team members will receive the same mark (a sum of the marks for each iteration), **if you as an individual fail to meet these criteria your final project mark may be scaled down**, most likely quite significantly.

### Code contribution

All team members must contribute code to the project. Tutors will assess the degree to which you have contributed by looking at your **git history** and analysing lines of code, number of commits, timing of commits, etc. If you contribute significantly less code than your team members, your work will be closely examined to determine what scaling needs to be applied.

### Documentation contribution

All team members must contribute documentation to the project. Tutors will assess the degree to which you have contributed by looking at your **git history** but also **asking questions** (essentially interviewing you) during your demonstration.

Note that, **contributing more documentation is not a substitute for not contributing code**.

### Peer Assessment

You will be required to complete a form in week 10 where you rate each team member's contribution to the project and leave any comments you have about them. Information on how you can access this form will be released closer to Week 10. Your other team members will **not** be able to see how you rated them or what comments you left.

If your team members give you a less than satisfactory rating, your contribution will be scrutinised and you may find your final mark scaled down.

### Attendance

It is generally assumed that all team members will be present at the demonstrations and at weekly check-ins. If you're absent for more than 80% of the weekly check-ins or any of the demonstrations, your mark may be scaled down.

If, due to exceptional circumstances, you are unable to attend your lab for a demonstration, inform your tutor as soon as you can so they can record your absence as planned.

### Plagiarism

The work you and your group submit must be your own work. Submission of work partially or completely derived from any other person or jointly written with any other person is not permitted. The penalties for such an offence may include negative marks, automatic failure of the course and possibly other academic discipline. Assignment submissions will be examined both automatically and manually for such submissions.

Relevant scholarship authorities will be informed if students holding scholarships are involved in an incident of plagiarism or other misconduct.

Do not provide or show your project work to any other person, except for your group and the teaching staff of COMP1531. If you knowingly provide or show your assignment work to another person for any reason, and work derived from it is submitted you may be penalized, even if the work was submitted without your knowledge or consent. This may apply even if your work is submitted by a third party unknown to you.

Note, you will not be penalized if your work has the potential to be taken without your consent or knowledge.
