from django.contrib import admin
from todolist_app.models import TaskList


# Here we are registering the database model that we've created.
class TaskListAdmin(admin.ModelAdmin):
    list_display = ['task', 'done',]
    
admin.site.register(TaskList, TaskListAdmin)
