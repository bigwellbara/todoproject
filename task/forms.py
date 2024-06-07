# forms.py
from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'start_date', 'end_date', 'completed_status', 'priority', 'tags', 'assigned_to', 'reminder', 'attachment']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
