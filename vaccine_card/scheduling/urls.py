from django.urls import path

from .views import schedules

app_name = 'scheduling'

urlpatterns = [
    path('', schedules, name='schedules')
]
