# Slackr
## Tech Stack
### Backend
- Python 3.7
- Flask
- Pipenv
- PyTest
- Coverage

### Frontend
- ReactJS
- Material UI
- Axios

## Table of Contents
- Features
- Installation
- Specification

## Features
### Authenticate Users
- Ability to login
- register if not registered
- log out
- reset password via email

### Instant Messaging
- Groups chatrooms into channels
- Users can see a list of channels
- Create a channel, join a channel, invite someone else to a channel, and leave a channel
- Within a channel, ability to view all messages, view the members of the channel, and the details of the channel-
- Within a channel, ability to send a message now, or to send a message at a specified time in the future
- Within a channel, ability to edit, remove, pin, unpin, react, or unreact to a message
- Begin a "standup", which is an X minute period where users can send messages that at the end of the period will automatically be collated and summarised to all users


### User Profiles
- View user anyone's user profile, and modify a user's own profile (name, email, handle, and profile photo)
- Search for messages based on a search string
- Modify a user's privileges: (MEMBER, OWNER)

### Server Backups
- Persistant data that can be loaded after a server shutdown

### Admin Priviledges
- support for slackr owners to remove users from slackr

### Hangman
After a game of Hangman has been started any user in the channel can type `/guess X` where `X` is an individual letter. If that letter is contained in the word or phrase they're trying to guess, the app should indicate *where* it occurs. If it does not occur, more of the hangman is drawn. There is a *lot* of flexibility in how you achieve this. It can be done only by modifying the backend and relying on messages to communicate the state of the game (e.g. after making a guess, the "Hangman" posts a message with a drawing of the hangman in ASCII/emoji art). Alternatively you can modify the frontend, if you want to experiment with fancier graphics.

The app should use words and phrases from an external source, not just a small handful hardcoded into the app. One suitable source is `/usr/share/dict/words` available on Unix-based systems. Alternatively, the python [wikiquote](https://github.com/federicotdn/wikiquote) module is available via pip and can be used to retrieve quotes and phrases from [Wikiquote](https://www.wikiquote.org/).

Note that this part of the specification is deliberately open-ended. You're free to make your own creative choices in exactly how the game should work, as long as the end result is something that could be fairly described as Hangman.


