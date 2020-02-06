# ! python3
# -*- coding: utf-8 -*-


from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', include('todolist_app.urls')), # In this line we use "include" because we are including todolist_app.
    path('account/', include('users_app.urls')), # In this line we use "include" because we are including users_app.

    path('', todolist_views.index, name='index'),
    path('contact', todolist_views.contact, name='contact'),
    path('about', todolist_views.about, name='about'),

    
]
