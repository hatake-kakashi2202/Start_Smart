
from django.urls import path,include
from . import views

urlpatterns = [
 
    path('',views.home,name='home' ),
    path('creat/',views.creat,name='creat' ),
    path('vote/<int:poll_id>',views.vote,name='vote' ),
    path('result/<int:poll_id>',views.result,name='result' ),
    

]