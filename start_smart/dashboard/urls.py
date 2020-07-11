from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('extend/', views.extend, name = 'extend'),
]
