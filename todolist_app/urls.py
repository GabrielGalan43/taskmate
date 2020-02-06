# ! python3
# -*- coding: utf-8 -*-

from django.urls import path
from todolist_app import views



urlpatterns = [
    # '' in the begining of the argumenst passed
    # to path(), means "task/".
    # The first path ( '' ), must always remain.
    # If it is deleted, the other paths won't work.
    path('', views.todolist, name='todolist'),
    # The next path means "/task/<path_name>"
    #path('todolist/', views.todolist, name='todolist'), # Don't forget to add "/" at the end.
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('complete/<task_id>', views.complete_task, name='complete_task'),
    path('pending/<task_id>', views.pending_task, name='pending_task'),    
]
