from django.db import models


# Create your models here.
class Ticket(models.Model):
    location = models.CharField(max_length=50, blank=False, null=False)
    datetime = models.DateTimeField(max_length=50, blank=False, null=False)
