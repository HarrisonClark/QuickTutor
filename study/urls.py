from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'study'
urlpatterns = [
    path('', views.index, name="index"),
    path('tutor-request/', views.tutor_request, name="tutor_request"),
    path('requests/', login_required(views.RequestsView.as_view()), name="requests")
]
