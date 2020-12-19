from django.urls import path

from .views import patient_index, patient_vaccine_card

app_name = 'app'

urlpatterns = [
    path('patient/', patient_index, name='patient_index'),
    path('patient/card/', patient_vaccine_card, name='patient_vaccine_card')
]
