from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/city-stats/', views.api_city_stats, name='api_city_stats'),
]
