from django.urls import path
from .import views

urlpatterns = [
    # path('', views.mentor, name = 'mentor'),
    path('mentor/', views.mentor, name = 'mentor'),
    path('incubators/', views.incubators, name = 'incubators'),
    path('student/', views.student, name = 'student'),
]
