from django.db import models


# Create your models here.
class Course(models.Model):
    # Each course has a name
    courseName = models.CharField(max_length=20, null=False, default='CS361')

    # Boolean field defining if a class is full or not
    isFull = models.BooleanField(default=False)

    # Start and End Times for Each Course
    startTime = models.TimeField('Start Time:')
    endTime = models.TimeField('Start Time:')

    # Date Field for Dates, if it's online, it is "online" instead of a combination of M, T, W, R, F, or S
    # Date cannot include Sundays, as classes are not on Sundays
    dates = models.CharField(max_length=6, default='MTWRFS')

    # Return if the class is full for TA's & Graders or not
    def isFull(self):
        return self.isFull

    # Set the course to be full or not
    # b is a Boolean value
    def setIsFull(self, b):
        self.isFull = b

    # Return the course name
    def courseName(self):
        return self.courseName

    # Check if a course is online or not
    def isOnline(self):
        return self.dates == 'Online'

    # Getter method for startTime
    def getStartTime(self):
        return self.startTime

    # Getter method for endTime
    def getEndTime(self):
        return self.endTime

    # Getter method for dates
    def getDates(self):
        return self.dates

    def setDates(self, dates):
        self.dates = dates


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
        return self.userEmail

    # Reset the user's password
    def resetPassword(self):
        if not self.loggedIn:
            return 'Not logged in. Cannot run function.'
        return self.userPassword

    # Return the user's type
    def userType(self):
        if not self.loggedIn:
            return 'Not logged in. Cannot run function.'
        return self.user_type
