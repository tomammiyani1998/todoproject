from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Task
from .forms import TodoForm


# Create your views here.
class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task_value'


class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task_value'


class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task_value'
    fields = ['name', 'priority', 'date']

    def get_success_url(self):
        return reverse_lazy('todoapp:detailview', kwargs={'pk': self.object.id})


class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:homelistview')


def add(request):
    task_value = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'home.html', {'task_value': task_value})


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')


def update(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'task': task})