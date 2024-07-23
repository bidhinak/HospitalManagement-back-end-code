from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="doctors/", null=True)
    qualification = models.CharField(max_length=100)


class Notification(models.Model):
    date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    description = models.TextField()


class doctoradd(models.Model):
    details = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    photo = models.CharField(max_length=100)


class schedule(models.Model):
    user = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    fee = models.CharField(max_length=100)
