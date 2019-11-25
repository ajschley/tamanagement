from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CreateCourseForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))


class CreateUserForm(forms.Form):
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class EditCourseForm(forms.Form):
    name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    startTime = forms.TimeField(required=True, widget=forms.TimeInput(format='%H:%M'))
    endTime = forms.TimeField(required=True, widget=forms.TimeInput(format='%H:%M'))
    dates = forms.CharField(required=True, max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))


class EditProfileForm(forms.Form):
    resume = forms.CharField(required=False, max_length=5000, widget=forms.Textarea(attrs={'class': 'form-control'}))


class EditUserForm(forms.Form):
    email = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    firstName = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastName = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    officeHours = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    officeHoursDates = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    officeLocation = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
