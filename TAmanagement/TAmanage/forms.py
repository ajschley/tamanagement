from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CreateCourseForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#TODO

class CreateUserForm(forms.Form):
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#TODO

class EditCourseForm(forms.Form):
    name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    startTime = forms.TimeField(required=True, widget=forms.TimeInput(format='%H:%M'))
    endTime = forms.TimeField(required=True, widget=forms.TimeInput(format='%H:%M'))
    dates = forms.CharField(required=True, max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))


class EditProfileForm(forms.Form):
    resume = forms.CharField(required=False, max_length=5000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    schedule = forms.CharField(required=False, max_length=5000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    preferences = forms.CharField(required=False, max_length=5000, widget=forms.Textarea(attrs={'class': 'form-control'}))


class AssignTaForm(forms.Form):
    ta = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    course = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #TODO

