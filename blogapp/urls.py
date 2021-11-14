from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.PostList.as_view(),name='Home'),
    path('<slug:slug>/',views.PostList.as_view(),name='post_detail'),
]