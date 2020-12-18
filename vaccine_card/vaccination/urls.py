from django.urls import path

from .views import *

app_name = 'vaccination'

urlpatterns = [
    path('vaccines/', vaccines, name='vaccines'),
    path('vaccine/add/', add_vaccine, name='add_vaccine')
]
