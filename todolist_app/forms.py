from django import forms
from todolist_app.models import TaskList

class TaskForm(forms.ModelForm):    
    class Meta:
        model = TaskList # We pass the model name.
        fields = ['task', 'done'] # We pass the fields of the model.
