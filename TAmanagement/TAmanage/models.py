from django.db import models


# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=29, null=False, default='CS361')
    isFull = models.BooleanField(default=False)

    # Return if the class is full for TA's & Graders or not
    def isfull(self):
        pass

    # Return the course name
    def coursename(self):
        pass


class User(models.Model):
    userEmail = models.CharField(max_length=50, null=False)
    userPassword = models.CharField(max_length=100, null=False)
    USER_TYPES = [
        ('ADMIN', 'Admin'),
        ('PROF', 'Professor'),
        ('TA', 'TA / Grader'),
    ]
    user_type = models.CharField(max_length=5, choices=USER_TYPES, default='TA')

    # Return the user's email/username
    def username(self):
        pass

    # Reset the user's password
    def resetpassword(self):
        pass

    # Return the user's type
    def usertype(self):
        pass
