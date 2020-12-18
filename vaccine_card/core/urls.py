from django.urls import path, include

from .views import index, logout

app_name = 'panel'

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout'),

    path('vaccination/', include('vaccine_card.vaccination.urls', namespace='vaccination'))
]
