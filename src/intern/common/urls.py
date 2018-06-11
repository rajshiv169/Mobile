from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.register,name='register'),
    re_path(r'^(?P<id>\d+)/$', views.mob_details, name='details'),
    path('search/',views.search, name='search'),
]