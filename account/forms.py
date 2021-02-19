from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from account.models import Account
class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Pasword',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]
        labels = {'username':'Username','first_name':'First Name','last_name':'Last Name','email':'Email'}