# forms.py
from django import forms
from .models import Alarm
from datetime import datetime

class AlarmForm(forms.ModelForm):
    class Meta:
        model = Alarm
        fields = ['text', 'alarm_date', 'alarm_time']

    text = forms.CharField(max_length=200, label="Alarm Text")
    
  
    alarm_date = forms.DateField(initial=datetime.today, widget=forms.DateInput(attrs={
        'type': 'date',
    }), label='Set Date')

    alarm_time = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'time',
        'value': datetime.now().strftime('%H:%M'), 
    }), label='Set Time')
