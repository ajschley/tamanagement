from django.forms import ModelForm
from Lab12 import models


class CreateUser(ModelForm):
    class Meta:
        model = models.User
        fields = ['email', 'username', 'password']
