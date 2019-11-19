from django.db import models


class User(models.Model):
    email = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    gifts = models.CharField(max_length=32)
