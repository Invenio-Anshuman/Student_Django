from django.contrib import admin
from django.urls import path
from StudentApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("all", views.all, name='all'),
    path("create", views.create, name='create'),
    # path("edit", views.edit, name='edit'), 
]