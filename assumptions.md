# Assumptions
## Authentication

|## Type defintions|
---
| email | string|
| password | string|
| token | string|
| name_first | string|
| name_last | string|
---

## Tests
The core assumption is that the user database is empty and is cleaned after each test is run. Some tests for specific functions depend on other functions being implemented. The recommended order of implementation is:
1. Registration
2. Login
3. Logout

### def test_register_email_invalid
- user z5555555@unsw.edu.au does not already exist

### def test_register_email_in_use
- user z5555555@unsw.edu.au does not already exist

### def test_register_password_too_short():
- user z5555555@unsw.edu.au does not already exist

### def test_register_name_length():
- user z5555555@unsw.edu.au does not already exist

### def test_login_email_invalid():
- user z5555555@unsw.edu.au does not exist

### def test_login_no_user_found():
- user z5555555@unsw.edu.au does not exist

### def test_login_password_incorrect():
- register is implemetned
- new_user is deleted after testing


### def test_logout():
- register and login are already correctly implemented
- user is deleted after creation


### def test_valid_credentials();
- all functions ave been implemented
