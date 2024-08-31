from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import TimeInput


# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="doctors/", default="doctors/default admin.png")
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
    mobile = models.CharField(max_length=10)
    qualification = models.CharField(max_length=100)


class schedule(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    fee = models.CharField(max_length=100)


class book(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    schedule = models.ForeignKey(schedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)


class statusreport(models.Model):
    schedule_id = models.ForeignKey(schedule, on_delete=models.CASCADE)
    doc_id = models.ForeignKey(Login, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)
