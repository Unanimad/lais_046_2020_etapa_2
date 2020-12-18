from django.urls import path

from .views import index, logout

app_name = 'panel'

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout')
]
