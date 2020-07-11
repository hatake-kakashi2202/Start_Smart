
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('signup/', views.signup_main, name='signup_main'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    # path('signup/', views.signup_startup, name = 'signup_startup'),
    path('update_info/', views.update_info, name = 'update_info'),
    path('update_startup/', views.update_startup, name = 'update_startup'),
    path('update_user/', views.update_user, name = 'update_user'),
    path('email_auth/', views.email_auth, name = 'email_auth'),
    path('forget_pass/', views.forget_pass, name = 'forget_pass'),
    url(r'verify_pass/(?P<username>\w+?)/(?P<time_lim>\w+?)/(?P<rand>\w+?)/$', views.verify_pass, name = 'verify_pass'),
    url(r'new_pass/(?P<username>\w+?)/(?P<password>\w+?)/$', views.new_pass, name='new_pass'),
]
