from django.urls import path, include

from .views import index, logout

app_name = 'panel'

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout'),

    path('panel/logistic/', include('vaccine_card.logistic.urls', namespace='logistic')),
    path('panel/vaccination/', include('vaccine_card.vaccination.urls', namespace='vaccination')),

    path('app/', include('vaccine_card.app.urls', namespace='app')),
]
