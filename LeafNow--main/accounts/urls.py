from django.contrib import admin
from django.urls import path
from django.http import FileResponse

from . import views
urlpatterns = [
    path('',views.login),
    path('login',views.login),
    path('index.html',views.login),
    path('index',views.index),
    path('donation',views.donation),
    path('signup',views.signup),
    path('forum',views.forum),
]
