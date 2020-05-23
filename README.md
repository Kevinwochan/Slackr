# Slackr

## Table of Contents
- Features
- Installation
- Specification

## Features
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
12. Implement the `/passwordreset/request` and `/passwordreset/reset` routes that have been added to the table below. By doing this, the "Forgot your password" feature of the frontend should now work.
13. Modify your backend such that it is able to persist and reload its data store. The persistance should happen at regular intervals so that in the event of unexpected program termination (e.g. sudden power outage) a minimal amount of data is lost. You may implement this using whatever method of serialisation you prefer (e.g. pickle, JSON).
14. Implement the `/user/profile/uploadphoto` route as described in table below. If you do this correctly, you should be able to set a profile image when using the frontend. Note that you may need to do your own research into flask features not covered in this course, and python packages for manipulating images. Any additional packages you use need to be added to `requirements.txt`.
15. Add support for slackr owners to remove users from slackr. This requires modifying both the backend and frontend. You should modify the backend by implementing `/admin/user/remove` in the table below. For the frontend, add an additional entry to the admin menu that provides an interface for removing users.
16. Allow users to relax and play a game of [Hangman](https://en.wikipedia.org/wiki/Hangman_(game)) in slackr. If the command `/hangman` is typed into a channel, it should start a game where the users of the channel cooperatively try to guess a word or phrase letter by letter. See more details below.

### Hangman

After a game of Hangman has been started any user in the channel can type `/guess X` where `X` is an individual letter. If that letter is contained in the word or phrase they're trying to guess, the app should indicate *where* it occurs. If it does not occur, more of the hangman is drawn. There is a *lot* of flexibility in how you achieve this. It can be done only by modifying the backend and relying on messages to communicate the state of the game (e.g. after making a guess, the "Hangman" posts a message with a drawing of the hangman in ASCII/emoji art). Alternatively you can modify the frontend, if you want to experiment with fancier graphics.

The app should use words and phrases from an external source, not just a small handful hardcoded into the app. One suitable source is `/usr/share/dict/words` available on Unix-based systems. Alternatively, the python [wikiquote](https://github.com/federicotdn/wikiquote) module is available via pip and can be used to retrieve quotes and phrases from [Wikiquote](https://www.wikiquote.org/).

Note that this part of the specification is deliberately open-ended. You're free to make your own creative choices in exactly how the game should work, as long as the end result is something that could be fairly described as Hangman.

## Installation
- Installing the backend
- Installing the frontend

