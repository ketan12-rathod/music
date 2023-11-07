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
from myadmin import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('layout', views.layout, name='layout'),
    path('common_form', views.common_form, name='common_form'),
    path('add_country', views.add_country, name='add_country'),
    path('store_country', views.store_country, name='store_country'),
    path('common_table', views.common_table, name='common_table'),
    path('all_country', views.all_country, name='all_country'),
    path('delete_country/<int:id>', views.delete_country, name='delete_country'),
    path('add_state', views.add_state, name='add_state'),
    path('store_state', views.store_state, name='store_state'),

]
