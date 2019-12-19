from django import forms
from .models import *


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CreateCourseForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    section = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))


CHOICES = [
        (1, 'TA'),
        (2, 'Instructor'),
        (3, 'Administrator'),
    ]


class CreateUserForm(forms.Form):
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    role = forms.CharField(widget=forms.Select(choices=CHOICES))


class EditCourseForm(forms.Form):
    name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    section = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    startTime = forms.TimeField(required=True, widget=forms.TimeInput(format='%H:%M'))
    endTime = forms.TimeField(required=True, widget=forms.TimeInput(format='%H:%M'))
    dates = forms.CharField(required=True, max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))


class EditUserForm(forms.Form):
    email = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    firstName = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastName = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    officeHours = forms.CharField(required=False, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    officeHoursDates = forms.CharField(required=False, max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    officeLocation = forms.CharField(required=False, max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    role = forms.CharField(widget=forms.Select(choices=CHOICES))
    resume = forms.CharField(required=False, max_length=5000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    schedule = forms.CharField(required=False, max_length=5000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    preferences = forms.CharField(required=False, max_length=5000, widget=forms.Textarea(attrs={'class': 'form-control'}))


class CreateLabForm(forms.Form):
    section = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))


class EditLabForm(forms.Form):
    section = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    startTime = forms.TimeField(required=True, widget=forms.TimeInput(format='%H:%M'))
    endTime = forms.TimeField(required=True, widget=forms.TimeInput(format='%H:%M'))
    dates = forms.CharField(required=True, max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))


'''class EditProfileForm(forms.Form):
    resume = forms.CharField(required=False, max_length=5000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    schedule = forms.CharField(required=False, max_length=5000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    preferences = forms.CharField(required=False, max_length=5000, widget=forms.Textarea(attrs={'class': 'form-control'}))'''


class AssignTaForm(forms.Form):
    course = forms.ModelChoiceField(widget=forms.Select, queryset=Course.objects.all(), to_field_name="name")
    tas = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=User.objects.all(), to_field_name="email")



