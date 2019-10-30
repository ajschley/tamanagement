from django.db import models


# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=29, null=False, default='CS361')
    isFull = models.BooleanField(default=False)

    # Return if the class is full for TA's & Graders or not
    def isfull(self):
        return self.isFull;

    # Return the course name
    def coursename(self):
        return self.courseName;


class User(models.Model):
    userEmail = models.CharField(max_length=50, null=False)
    userPassword = models.CharField(max_length=100, null=False)
    USER_TYPES = [
        ('ADMIN', 'Admin'),
        ('PROF', 'Professor'),
        ('TA', 'TA / Grader'),
    ]
    user_type = models.CharField(max_length=5, choices=USER_TYPES, default='TA')
    loggedIn = False

    # User login
    def login(self, username, password):
        if username == self.userEmail and password == self.userPassword:
            self.loggedIn = True
            return 'Login successful.'
        else:
            return 'Login failed'

    # User logout
    def logout(self):
        if not self.loggedIn:
            return 'Not logged in. Cannot logout.'
        else:
            self.loggedIn = False
            return 'Logout successful.'

    # Return the user's email/username
    def username(self):
        if not self.loggedIn:
            return 'Not logged in. Cannot run function.'
        return self.username

    # Reset the user's password
    def resetpassword(self):
        if not self.loggedIn:
            return 'Not logged in. Cannot run function.'
        pass

    # Return the user's type
    def usertype(self):
        if not self.loggedIn:
            return 'Not logged in. Cannot run function.'
        pass
