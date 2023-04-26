from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.forms.fields import 
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)