from django.db import models
from django.contrib.auth.models import User



class Tag(models.Model):
    name = models.CharField(max_length=50)
    def _str_(self):
        return self.name



class Task(models.Model):

    PRIORITY_CHOICES =[
        ('L','Low'),
        ('M','Medium'),
        ('H','High'),
    ]


    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    completed_status = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    tags = models.ManyToManyField(Tag, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    progress = models.PositiveIntegerField(default=0)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reminder = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
      
        return self.title
        #return f"{self.title} - {self.description}"

class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,related_name='subtasks')
    title = models.CharField(max_length=200)
    completed_status = models.BooleanField(default=False)

    def _str_(self):
        return self.title