from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from .models import Task, Tag, Subtask
from .forms import TaskForm, TagForm



# Create your views here.
def task_list(request):
    tasks= Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks':tasks})



def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request,'task/task_detail.html',{'task':task})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task/task_create.html',{'form':form})  


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail',pk=pk)
        else:
            form = TaskForm(instance=task)
        return render(request,'task/task_list.html',{'form':form})