from django.db import models


# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=29, null=False, default='CS361')
    isFull = models.BooleanField(default=False)


class User(models.Model):
    userEmail = models.CharField(max_length=50, null=False)
    userPassword = models.CharField(max_length=100, null=False)
    isAdmin = models.BooleanField(default=False)