from django.urls import path

from .views import health_centers, add_health_center

app_name = 'logistic'

urlpatterns = [
    path('health_centers', health_centers, name='health_centers'),
    path('heath_center/add/', add_health_center, name='add_health_center'),
]
