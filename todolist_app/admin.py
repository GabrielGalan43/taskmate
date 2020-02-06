from django.contrib import admin
from todolist_app.models import TaskList

admin.site.register(TaskList) # Here we are registering the model that we've created.
