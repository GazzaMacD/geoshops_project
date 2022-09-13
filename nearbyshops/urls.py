from django.contrib import admin
from django.urls import path, include
from nearbyshops import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
]
