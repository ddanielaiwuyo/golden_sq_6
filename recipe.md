As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

### REQUIREMENTS
* accept date
* compare to today
* compare user_age to 16
* send message to user


### FUNCTIONS
def check_user_age(age)
    * takes in dob as date
    * compare their current age to 16
    * "Accss Granted!" or "Access not granted, must be over 16 but your x years old"


