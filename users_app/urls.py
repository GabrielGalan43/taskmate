# ! python3
# -*- coding: utf-8 -*-

from django.urls import path
from users_app import views



urlpatterns = [
    # '' in the begining of the argumenst passed
    # to path(), means "task/".
    # The first path ( '' ), must always remain.
    # If it is deleted, the other paths won't work.
    path('register', views.register, name='register'),
    
]
