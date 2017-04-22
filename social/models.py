from django.db import models
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from django import forms

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

# class Profile(models.Model):
    
# class Department(models.Model):
#     dept_name = models.CharField(max_length = 30)
#     dept_code = models.CharField(max_length = 5)
#     dept_

class Group(models.Model):
    group_name = models.CharField(max_length = 20)
    group_type = models.CharField(max_length = 10)

class Post(models.Model):
    posted_by = models.ForeignKey(User)
    posted_in = models.ForeignKey(Group)
    posted_on = models.DateTimeField("posted_on")
    text = models.CharField(max_length = 1000)

class 