from django.urls import path

from .views import patient_index, patient_vaccine_card, add_schedule, patient_schedule

app_name = 'app'

urlpatterns = [
    path('patient/', patient_index, name='patient_index'),
    path('patient/card/', patient_vaccine_card, name='patient_vaccine_card'),
    path('schedule/', add_schedule, name='add_schedule'),
    path('schedules/', patient_schedule, name='patient_schedule'),
]
