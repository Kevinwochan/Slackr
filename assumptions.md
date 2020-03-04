# Assumptions
- All parameters to functions will be of the correct type

### **Authenication**

**Type defintions**
 
| variable   | type   |
| ---------- | ------ |
| email      | string |
| password   | string |
| token      | string |
| name_first | string |
| name_last  | string |

Functions should be implemented in this order:
1. Registration
2. Login
3. Logout

Before the authentication tests are run, the user database should be empty and is cleaned after each test is run

#### Functions

 **def test_register_email_invalid**
- user z5555555@unsw.edu.au does not already exist

 **def test_register_email_in_use**
- user z5555555@unsw.edu.au does not already exist

 **def test_register_password_too_short**
- user z5555555@unsw.edu.au does not already exist

 **def test_register_name_length**
- user z5555555@unsw.edu.au does not already exist

 **def test_login_email_invalid**
- user z5555555@unsw.edu.au does not exist

 **def test_login_no_user_found**
- user z5555555@unsw.edu.au does not exist

 **def test_login_password_incorrect**
- register is implemetned
- new_user is deleted after testing


 **def test_logout**
- register and login are already correctly implemented
- user is deleted after creation

 **def test_valid_credentials**
- all functions have been implemented


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