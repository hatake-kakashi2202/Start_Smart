from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('startupandCoorporate/', views.startupandCoorporate, name = 'startupandCoorporate'),
    path('Individual/', views.Individual, name = 'Individual'),
    path('Mentors/', views.Mentors, name = 'Mentors'),
]
