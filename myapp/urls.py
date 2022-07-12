from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('success', views.success, name='success'),
]