# views.py
from django.shortcuts import render, redirect
from .forms import AlarmForm
from .models import Alarm
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

def set_alarm(request):
    if request.method == 'POST':
        form = AlarmForm(request.POST)
        if form.is_valid():
            alarm_date = form.cleaned_data['alarm_date']
            alarm_time = form.cleaned_data['alarm_time']
            alarm_datetime = datetime.combine(alarm_date, alarm_time)
            
            # Save the alarm with combined datetime
            Alarm.objects.create(text=form.cleaned_data['text'], alarm_date=alarm_date, alarm_time=alarm_time)
            return redirect('set_alarm')
    else:
        form = AlarmForm()

    upcoming_alarms = Alarm.objects.all().order_by('alarm_date', 'alarm_time')
    
    return render(request, 'set_alarm.html', {'form': form, 'upcoming_alarms': upcoming_alarms})

def delete_alarm(request, pk):
    alarm = get_object_or_404(Alarm, pk=pk)
    
    # Delete the alarm
    alarm.delete()
    
    # Add a success message (optional)
    messages.success(request, "Alarm has been deleted successfully.")
    
    # Redirect back to the list of alarms
    return redirect('set_alarm')  # Change 'list_alarms' to the name of your alarm list view