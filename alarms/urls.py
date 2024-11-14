from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.set_alarm, name='home'),  
    path('set_alarm/', views.set_alarm, name='set_alarm'),
    path('delete/<int:pk>/', views.delete_alarm, name='delete_alarm'),
    path('api/alarms/', api.AlarmList.as_view(), name='alarm-list'),
    
]
