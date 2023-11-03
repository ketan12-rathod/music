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
from user import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('layout', views.layout, name='layout'),
    # # path('contact', views.contact, name='contact'),
    # # path('store_contact', views.store_contact, name='store_contact'),
    # path('common_table', views.common_table, name='common_table'),
    path('register', views.register, name='register'),
    path('register_store', views.register_store, name='register_store'),
    # path('login', views.login, name='login'),
    # path('login_check', views.login_check, name='login_check'),
    # path('profile', views.profile, name='profile'),
    # path('edit_profile/<int:id>', views.edit_profile, name='edit_profile'),
    # path('update_profile', views.update_profile, name='update_profile'),
    # # path('logout', views.logout, name='logout'),
    # # path('logout', views.logout, name='logout'),
    
]
