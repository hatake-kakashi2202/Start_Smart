"""start_smart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import finances.views as v
from forum import views
from django.conf import settings
from django.conf.urls.static import static
from forum.views import SearchResultsView,HomePageView
# from .import views



   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('accounts/', include('accounts.urls')),
    path('blogs/', include('blogs.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('finances/', include('finances.urls')),
    path('networking/', include('networking.urls')),
    # path('register/',views.register,name="register"),
    # path('user_login/',views.user_login,name="user_login"),
    # path('logout/',views.user_logout,name='logout'),
    path('forum/',views.forum,name='forum'),
    path('like/',views.like_post, name='like_post'),
    # path('finances/<user_name>/', views.finances, name='finances_sp'),
    # path('finances/', views.finances, name='finances'),
    path('forum_details/<int:forum_id>/', views.forum_details, name='forum_details_sp'),
    path('forum_details/', views.forum_details, name='forum_details'),
    path('search/', SearchResultsView.as_view(), name='forumsearch'),
    path('forum/', HomePageView.as_view(), name='forum'),
    path('poll/',include('poll.urls')),
    path('contact/',v.contact,name="contact"),
    path('appointment/',v.appointment,name="appointment"),
    path('advice/',v.graph,name='advice'),
    path('upfin/',v.update_fin,name='upfin'),
    path('update/',v.update,name='update'),
    path('soon/',views.soon,name='comingsoon'),
    path('contacts/',include('contacts.urls')),
   path('aboutus/',views.aboutus,name="aboutus"),

   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
