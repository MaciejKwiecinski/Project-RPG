"""ProjektRPG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from ProjektRPGtekstowy.views import main,PlayerView,EventView,StatView,CharacterView,instruction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main),
    path('create/',PlayerView.as_view()),
    path('story/<int:id>',EventView.as_view()),
    path('stats/',StatView.as_view(),name='stats'),
    path('character/',CharacterView.as_view()),
    path('instruction/',instruction)
]