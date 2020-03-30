from django.contrib import admin
from django.urls import path,include

from . import views

app_name = 'userprofile'
urlpatterns = [
    path('', views.index, name="index"),
    path('edit/', views.edit_profile, name="edit")
]
