from typing import Any, Dict
from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import TaskModel
from django.views.generic import TemplateView, CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request,'home.html')

class TaskFormView(CreateView):
    model = TaskModel
    template_name = 'add_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('show_tasks')
    
    
class ShowTaskView(ListView):
    model = TaskModel
    template_name = 'show_tasks.html'
    context_object_name = 'data'
    
class CompletedTaskView(ListView):
    model = TaskModel
    template_name = 'completed_tasks.html'
    context_object_name = 'data'
    
class TaskUpdateView(UpdateView):
    model = TaskModel
    form_class = TaskForm
    template_name = 'edit_task.html'
    success_url = reverse_lazy('show_tasks')
    
class TaskDeleteView(DeleteView):
    model = TaskModel
    template_name = 'con_delete.html'
    success_url = reverse_lazy('show_tasks')
    
class Completed_pageTaskDeleteView(DeleteView):
    model = TaskModel
    template_name = 'con_delete.html'
    success_url = reverse_lazy('completed_tasks')
    
def CompleteTaskUpdate(request, id):
    task = TaskModel.objects.get(pk = id)
    task.is_completed = True
    task.save()
    
    return redirect('completed_tasks')
