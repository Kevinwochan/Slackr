# COMP1531 Major Project

## Aims:

* To provide students with hands on experience testing, developing, and maintaining a backend server in python.
* To develop students' problem solving skills in relation to the software development lifecycle.
* Learn to work effectively as part of a team by managing your project, planning, and allocation of responsibilities among the members of your team<
* Gain experience in collaborating through the use of a source control and other associated modern team-based tools.
* Apply appropriate design practices and methodologies in the development of their solution
* Develop an appreciation for product design and an intuition of how a typical customer will use a product.

## Changelog

Nothing here yet

## Background

To manage the transition from trimesters to hexamesters in 2020, UNSW has established a new focus on building an in-house digital collaboration and communication tool for groups and teams.

Rather than re-invent the wheel, UNSW has decided that it finds the functionality of **<a href="https://slack.com/intl/en-au/">Slack</a>** to be nearly exactly what it needs. For this reason, UNSW has contracted out Rayden Pty Ltd (a small software business run by Rob and Hayden) to build the new product. In UNSW's attempt to connect with the younger and more "hip" generation that fell in love with flickr, Tumblr, etc, they would like to call the new UNSW-based product **slackr**.

Rayden Pty Ltd has sub-contracted two software firms:

* BananaPie Pty Ltd (two software developers, Sally and Bob, who will build the initial web-based GUI)
* YourTeam Pty Ltd (a team of talented misfits completing COMP1531 in 19T3), who will build the backend python server and possibly assist in the GUI later in the project

In summary, UNSW contracts Rayden Pty Ltd, who sub contracts:

* BananaPie (Sally and Bob) for front end work
* YourTeam (you and others) for backend work

Rayden Pty Ltd met with Sally and Bob (the front end development team) 2 weeks ago to brief them on this project. While you are still trying to get up to speed on the requirements of this project, Sally and Bob understand the requirements of the project very well.

Because of this they have already specified a **common interface** for the front end and backend to operate on. This allows both parties to go off and do their own development and testing under the assumption that both parties comply will comply with the common interface. This is the interface **you are required to use**

Beside the information available in the interface that Sally and Bob provided, you have been told (so far) that the features of slackr that UNSW would like to see implemented include:

1. Ability to login, register if not logged in, and log out
2. Ability to reset password if forgotten it
3. Ability to see a list of channels
4. Ability to create a channel, join a channel, invite someone else to a channel, and leave a channel
5. Within a channel, ability to view all messages, view the members of the channel, and the details of the channel
6. Within a channel, ability to send a message now, or to send a message at a specified time in the future
7. Within a channel, ability to edit, remove, pin, unpin, react, or unreact to a message
8. Ability to view user anyone's user profile, and modify a user's own profile (name, email, handle, and profile photo)
9. Ability to search for messages based on a search string
10. Ability to modify a user's admin privileges: (MEMBER, ADMIN, OWNER)
11. Ability to begin a "standup", which is a 15 minute period where users can send messages that at the end of the period will automatically be collated and summarised to all users

To get further information about the requirements, Rayden Pty Ltd will provide a pre-recorded video briefing (with verbal and visual descriptions) of what they'd like to see in the Slackr product. This will be released on September 23rd.

## Setup

After your week 2 tutorial, you should know who your team members are. Follow the instructions on the tutorial sheet to ensure your team is registered. You need to do this by **Thursday 9PM in week 2**.

If you registered your team on time, then on Sunday of week 2, you should have access to an individual repository at this URL:

https://gitlab.cse.unsw.edu.au/COMP1531/19T3/team_name

where *team-name* is the name of your group as registered on the course website.

## Progress check-in

During your lab class, in weeks without demonstrations (see below), you and your team will conduct a short stand-up in the presence of your tutor. Each member of the team will briefly state what they have done in the past week, what they intend to do over the next week, and what issues they faced or are currently facing. This is so your tutor, who is acting as a representative of the client, is kept informed of your progress. They will make note of your presence and may ask you to elaborate on the work you've done.

## Iteration 1: Tests and Stories

### Task

In this iteration, you are expected to:

1. Create extensive tests (using pytest) for all of the functions in the agreed upon interface.

    These should all be in files of the formn `*_test.py`. See below for more information.

2. Create user stories for your current understanding of the product based on your previous understanding of a slack-like app.

    Each individual story should form its own card on the project task board.

3. Write assumptions that you feel you are making in your interpretation of the specification and of the functions provided.

    Write these in markdown in `assumptions.md`.

4. Write a brief 1-page plan highlighting how you will approach the following iteration (the development stage).

    Write these in markdown in `plan.md`. You may include diagrams, tables or whatever other information you believe conveys your plan.

5. Write a brief 1-page reflection on how this iteration has gone and how you successfully operated as a well-functioning team.

    Write these in markdown in `reflection.md`.

You are **not** expected to begin developing or completing the actual functions themselves.

The files described above should all be in the root of your repository. If you've not written markdown before (which we assume most of you haven't), it's not necessary to research the format. Markdown is essentially plain text with a few extra features for basic formatting. You can just stick with plain text if you find that easier.

### Tests

It is up to you how you structure your tests, but we do require that you write all of your stubs and tests in the /server/ folder.

Our recommendation is to break all of the functions to test up into 1 or many files (this is a decision for you and your team), and then create test files in the same directory as the files the tests are testing. An example of this has been done with:

* `/server/echo.py`
* `/server/echo_test.py`

Remember that we encourage you to write stub functions for all of the functions we provide. Stub functions are dummy implementations of functions that allow them to be trivially tested. E.G. A stub function for a user to login may always return a dummy auth token "123456". This will allow your tests to successfully compile. It is expected that *some* errors may appear in your tests as you write them that you won't discover until you develop the backend in iteration 2.

You may also wish to create some helper files with extra helper functions if that would assist you writing your tests.

### (More info) User Stories

The scaffold for user stories will be provided in the lecture on Monday 23rd September. Please refer to that lecture for information about the structure of the user stories.

### Submission

This iteration is due to be submitted at 5pm Sunday 6th October (**week 3**). You will then be demonstrating this in your week 4 lab. All team members **must** attend this lab session.

To submit, run this command in the CSE environment:

```sh
1531 submit iteration1
```

This will submit the contents of your repo on GitLab and perform a check to make sure that the files above are present. **Make sure that everything you intend to submit is included in your repo**. User stories should be entered into GitLab on the task board for your project.

### Marking Criteria

|Section|Weighting|Criteria|
|---|---|---|
|Pytests|40%| <ul><li>Demonstrated an understanding of good test **coverage**</li><li>Demonstrated an understanding of the importance of **clarity** on the communication of test purposes</li><li>Demonstrated an understanding of good test **design**</li><li>Tests not under or over engineered</li></ul>|
|Stories PDF|25%|<ul><li>Demonstration of an understanding of a user's needs when using a product</li><li>Clear sense of the coverage needed for requirements (i.e. all reasonable possibilities explored)</li><li>Strong understanding of the granularity in which to express requirements (not too specific, not too broad)</li><li>Demonstration of an understanding of the language typically used when writing user stories</li><li>Demonstration of an understanding of the difference between high-level/epic user stories and their subsequent user story components</li></ul>|
|Assumptions PDF|10%|<ul><li>Clear and obvious effort and time gone into thinking about possible assumptions that are being made when interpreting the specification</li></ul>|
|Reflection & Plan PDF|10%|<ul><li>Communication of plan for development in a written format</li><li>Communication of plan for development in a diagramatic format</li><li>Demonstration of understanding of how to draw and anticipate a timeline</li><li>Demonstration of thoughtfullness regarding software tools to assist the team in meeting the development iteration</li></ul>|
|Teamwork PDF|15%|<ul><li>Highlighting the timing and outcome of team meetings</li><li>Demonstration that responsibilities were allocated across team members</li><li>Clear reflection on areas for improvement</li><li>Impression that team has worked together collaboratively</li><li>Impression that team had processes in place to work through disagreements or tension</li><li>Impression that team had a thought out methodology for completing this iteration</li></ul>|

### Advice

* Do NOT attempt to try and write or start a web server. Don't overthink how these functions are meant to connect to a frontend yet. This is for the next iteration. In this iteration you are just focusing on the high level functions that will eventually be used for a web server.
* While we don't encourage you to implement the functions (because the specification may change, and there are no marks for implementation), we do encourage you to sufficiently "stub" out the functions to ensure they're testable and that your python tests can actually compile and run</li>

### Demonstration

When you demonstrate this iteration in your week 4 lab, the breakdown will go approximately like this:

* 5 minutes of demonstration of the code you produced
* 5 minutes of demonstration of your stories, assumptions, and plan
* 10 minutes of Q&A from the tutor(s)

## Iteration 2: Servers and Products

Details will be released in week 4

## Iteration 3: Improvements from customer feedback

Details will be released in week 7

## Interface pecifications from Sally and Bob

### Data types

|Variable name|Type|
|-------------|----|
|named exactly **email**|string|
|named exactly **id**|integer|
|named exactly **password**|string|
|named exactly **token**|string|
|named exactly **message**|string|
|contains substring **name**|string|
|contains substring **code**|string|
|has prefix **is_**|boolean|
|has prefix **time_**|datetime|
|has suffix **_id**|integer|
|has suffix **_url**|string|
|has suffix **_str**|string|
|has suffix **end**|integer|
|has suffix **start**|integer|
|named exactly **messages**|List of dictionaries, where each dictionary contains types { u_id, message, time_created, is_unread }|
|named exactly **channels**|List of dictionaries, where each dictionary contains types { id, name }|
|named exactly **members**|List of dictionaries, where each dictionary contains types { u_id, name_first, name_last }|

### Functions

|Function name|Parameters|Return type|
|-------------|----------|-----------|
|auth_login|(email, password)|{ token }|
|auth_logout|(token)|{}|
|auth_register|(email, password, name_first, name_last)|{ token }|
|auth_passwordreset_request|(email)|{}|
|auth_passwordreset_reset|(reset_code)|{}|
|channel_invite|(token, channel_id, u_id)|{}|
|channel_details|(token, channel_id)|{ name, owner_members, all_members }|
|channel_messages|(token, channel_id, start)|{ messages, start, end }|
|channel_leave|(token, channel_id)|{}|
|channel_join|(token, channel_id)|{}|
|channel_addowner|(token, channel_id, u_id)|{}|
|channel_removeowner|(token, channel_id, u_id)|{}|
|channels_list|(token)|{ channels }|
|channels_listall|(token)|{ channels }|
|channels_create|(token, name, is_public)|{ channel_id }|
|message_sendlater|(token, message, time_sent)|{}|
|message_send|(token, message)|{}|
|message_remove|(token, message_id)|{}|
|message_edit|(token, message, message_id)|{}|
|message_react|(token, message_id, react_id)|{}|
|message_unreact|(token, message_id)|{}|
|message_pin|(token, message_id)|{}|
|message_unpin|(token, message_id)|{}|
|user_profile|(token)|{ email, name_first, name_last, handle_str }|
|user_profile_setname|(token, name_first, name_last)|{}|
|user_profile_setemail|(token, email)|{}|
|user_profile_sethandle|(token, handle_str)|{}|
|user_profiles_uploadphoto|(token, img_url, x_start, y_start, x_end, y_end)|{}|
|standup_start|(token)|{ time_finish }|
|standup_send|(token, message)|{}|
|search|(token, query_str)|{ messages }|
|admin_userpermission_add|(token, u_id, permission_id)|{}|
|admin_userpermission_remove|(token, u_id, permission_id)|{}|

## Due Dates and Weightings

|Iteration|Code and report due                  |Demonstration to tutor(s)      |Assessment weighting of project (%)|
|---------|-------------------------------------|-------------------------------|-----------------------------------|
|   1     |8pm Sunday 6th October (**week 3**)  |In YOUR **week 4** laboratory  |30%                                |
|   2     |8pm Sunday 27th October (**week 6**) |In YOUR **week 7** laboratory  |40%                                |
|   3     |8pm Sunday 17th November (**week 9**)|In YOUR **week 10** laboratory |30%                                |

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
