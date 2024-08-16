from rest_framework import serializers

from hospitalapp.forms import doctorsignup
from hospitalapp.models import Notification, Login, doctoradd, schedule, book


class Notificationserializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class doctorsignupserializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"


class usersignupserializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"


class doctoraddserializer(serializers.ModelSerializer):
    class Meta:
        model = doctoradd
        fields = "__all__"


class scheduleserializer(serializers.ModelSerializer):
    class Meta:
        model = schedule
        fields = "__all__"


class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = "__all__"
