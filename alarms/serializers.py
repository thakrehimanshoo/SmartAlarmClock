from rest_framework import serializers
from .models import Alarm

class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm
        fields = ['text', 'alarm_date', 'alarm_time']  # Include your model fields
