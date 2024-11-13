from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Alarm
from .serializers import AlarmSerializer
from datetime import datetime, timedelta

class AlarmList(APIView):
    def get(self, request):
        
       
        current_datetime = datetime.now()
        
        alarms = Alarm.objects.filter(alarm_date__gte=current_datetime.date()).order_by('alarm_date', 'alarm_time')
        
       
        serializer = AlarmSerializer(alarms, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
