from django.contrib import admin
from django.urls import path, include
from .import views
from blogs.views import SearchResultsView,HomePageView

urlpatterns = [
    path('', views.allblogs, name = 'allblogs'),
    path('create/', views.create, name='create'),
    path('<int:blog_id>/', views.detail, name = 'detail'),
    path('myblogs/',views.myblogs, name = 'myblogs'),
    path('<int:blog_id>/interest/', views.interest, name = 'interest'),
    path('<int:blog_id>/likers/', views.likers, name = 'likers'),
    path('<int:blog_id>/delete_blog/', views.delete_blog, name = 'delete_blog'),
    # path('listing/', views.listing, name = 'listing')
    path('search/', SearchResultsView.as_view(), name='blogsearch'),
    path('', HomePageView.as_view(), name='allblogs'),
]
