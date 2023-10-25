"""
URL configuration for spotify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from company import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('layout', views.layout, name='layout'),
    path('contact', views.contact, name='contact'),
    path('store_contact', views.store_contact, name='store_contact'),
    path('common_form', views.common_form, name='common_form'),
    path('register', views.register, name='register'),
    path('store_register', views.store_register, name='store_register'),
    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('add_song', views.add_song, name='add_song'),
    path('store_song', views.store_song, name='store_song'),
    path('all_song', views.all_song, name='all_song'),
    path('logout', views.logout, name='logout'),
    path('logout', views.logout, name='logout'),
    path('delete_song/<int:id>', views.delete_song, name='delete_song'),
    path('add_video', views.add_video, name='add_video'),
    path('store_video', views.store_video, name='store_video'),
    path('all_video', views.all_video, name='all_video'),
    path('delete_video/<int:id>', views.delete_video, name='delete_video'),
    
]
