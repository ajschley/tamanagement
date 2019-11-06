from datetime import timezone, datetime

from django.db import models


# Create your models here.
class Course(models.Model):
    # Each course has a name
    name = models.CharField(max_length=20, default='CS361')

    # Boolean field defining if a class is full or not
    isCourseFull = models.BooleanField(default=False)

    # Start and End Times for Each Course
    startTime = models.TimeField('Start Time:', default=datetime.now)
    endTime = models.TimeField('Start Time:', default=datetime.now)

    # Date Field for Dates, if it's online, it is "Online" instead of a combination of M, T, W, R, F, or S
    # Date cannot include Sundays, as classes are not on Sundays
    dates = models.CharField(max_length=6, default='MTWRFS')

    # Return if the class is full for TA's & Graders or not
    def isFull(self):
        return self.isCourseFull

    # Set the course to be full or not
    # b is a Boolean value
    def setIsFull(self, b):
        self.isCourseFull = b

    # Return the course name
    def courseName(self):
        return self.name

    # Check if a course is online or not
    def isOnline(self):
        return self.dates == 'Online'

    # Getter method for startTime
    def getStartTime(self):
        if self.dates == "Online":
            return None
        return self.startTime

    # Getter method for endTime
    def getEndTime(self):
        if self.dates == "Online":
            return None
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

    # Return the user's email/username
    def username(self):
        return self.userEmail

    # Reset the user's password
    def resetPassword(self):
        return self.userPassword

    # Return the user's type
    def userType(self):
        return self.user_type
