from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Alarm
from .serializers import AlarmSerializer
from datetime import datetime, timedelta

class AlarmList(APIView):
    def get(self, request):
        
        # Get current date and time
        current_datetime = datetime.now()
        a_current_datetime = datetime.now() - timedelta(minutes=4)
        Alarm.objects.filter(
            alarm_date__lt=a_current_datetime.date()
        ).delete()
        # Filter alarms that are for today or in the future
        alarms = Alarm.objects.filter(alarm_date__gte=current_datetime.date()).order_by('alarm_date', 'alarm_time')
        
        # Serialize alarms
        serializer = AlarmSerializer(alarms, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
