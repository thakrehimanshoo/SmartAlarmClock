from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_alarm, name='home'),  # Make set_alarm the default home page
    path('set_alarm/', views.set_alarm, name='set_alarm'),
    path('delete/<int:pk>/', views.delete_alarm, name='delete_alarm'),
    
]
