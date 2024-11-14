from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Alarm
from .serializers import AlarmSerializer
from datetime import datetime, timedelta
from django.utils import timezone

class AlarmList(APIView):
    def get(self, request):
        current_datetime = timezone.now()

        threshold_time = current_datetime + timedelta(minutes=328)

        expired_alarms = Alarm.objects.filter(
            alarm_date__lt=threshold_time.date()
        ) | Alarm.objects.filter(
            alarm_date=threshold_time.date(),
            alarm_time__lte=threshold_time.time()
        )

        expired_alarms.delete()

        upcoming_alarms = Alarm.objects.filter(
            alarm_date__gt=current_datetime.date()
        ) | Alarm.objects.filter(
            alarm_date=current_datetime.date(),
            alarm_time__gt=current_datetime.time()
        ).order_by('alarm_date', 'alarm_time')

        serializer = AlarmSerializer(upcoming_alarms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
