# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def get_default_user():
    return User.objects.first()

class Alarm(models.Model):
    text = models.CharField(max_length=200)
    alarm_date = models.DateField()
    alarm_time = models.TimeField()
    turned_off = models.BooleanField(default=False)  # New field to track if the alarm is turned off
    turned_off_time = models.DateTimeField(null=True, blank=True)  # Store the time when the alarm was turned off

    def __str__(self):
        return f"Alarm set for {self.alarm_date} {self.alarm_time} with text: {self.text}"
