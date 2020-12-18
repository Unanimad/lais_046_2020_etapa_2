from django.urls import path

from .views import *

app_name = 'vaccination'

urlpatterns = [
    path('vaccines/', vaccines, name='vaccines'),
    path('vaccine/add/', add_vaccine, name='add_vaccine'),
    path('vaccine/del/', del_vaccine, name='del_vaccine'),
    path('vaccine/<int:pk>/', vaccine, name='vaccine'),
    path('vaccine/<int:pk>/edit/', edit_vaccine, name='edit_vaccine'),
]
