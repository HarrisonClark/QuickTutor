from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.Login, name="index"),
    path('', include('django.contrib.auth.urls')),
]
