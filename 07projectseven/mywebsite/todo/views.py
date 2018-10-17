from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.views.decorators.http import require_POST


# Create your views here.

def index(request):
    mytodo = Todo.objects.order_by('id')
    form = TodoForm()
    context = { 'mytodo': mytodo, 'form': form}
    return render(request, 'todo/index.html', context)

@require_POST 
def addNewTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        my_new_todo = Todo(todotext=request.POST['text'])
        my_new_todo.save()

    return redirect('index')


def completeTask(request, task_id):
    mytodo = Todo.objects.get(pk=task_id)
    mytodo.complete = True
    mytodo.save()
    return redirect('index')


def deleteTask(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def resetAll(request):
    Todo.objects.all().delete()
    return redirect('index')
