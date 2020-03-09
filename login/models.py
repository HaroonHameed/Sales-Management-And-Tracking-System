from django.db import models
from django import forms
# Create your models here.
class users(forms.Form):
    userName = forms.CharField(label="user name", max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
    typeOfUser = forms.CharField(label="user type", max_length=50)