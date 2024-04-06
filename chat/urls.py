"""
URL configuration for russpass_chat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views


urlpatterns = [
    #path('test/', views.test_view, name='test'),
    path('chat/', views.chat_view, name='chat'),
        path('chat/chat/', views.chat_view, name='chat'),
    path('map/', views.map_view, name='map'),
    path('game/', views.game_view, name='game'),
    path('', views.index_view, name='index'),

]
