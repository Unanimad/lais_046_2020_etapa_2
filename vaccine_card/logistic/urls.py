from django.urls import path

from .views import health_centers, add_health_center, health_center, del_health_center

app_name = 'logistic'

urlpatterns = [
    path('health_centers/', health_centers, name='health_centers'),
    path('health_center/add/', add_health_center, name='add_health_center'),
    path('health_center/del/', del_health_center, name='del_health_center'),
    path('health_center/<int:pk>/', health_center, name='health_center'),
]
