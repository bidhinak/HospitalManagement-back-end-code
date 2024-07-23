from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import models

from hospitalapp.models import Login, doctoradd


class usersignup(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Login
        fields = ('username', 'password1', 'password2', 'email', 'mobile')


class doctorsignup(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Login
        fields = ('username', 'password1', 'password2', 'email', 'mobile', 'department', 'photo', 'qualification')



