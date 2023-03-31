from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from todos_app.forms import TodoForm
from todos_app.models import ToDo


# Create your views here.
def index(request, form=None, form_action='create task', pk=None):
    if not form:
        form = TodoForm()

    context = {
        'todos': ToDo.objects.all().order_by('title'),
        'todo_form': form,
        'form_action': form_action,
        'pk': pk,
    }

    return render(request, 'todo.html', context)


@require_POST
def create_task(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        task = ToDo(title=form.cleaned_data['title'], description=form.cleaned_data['description'], is_done=False)
        task.save()
        return redirect('todo index')

    context = {
        'todos': ToDo.objects.all(),
        'todo_form': form,
    }

    return render(request, 'todo.html', context)


def edit_task(request, pk):
    todo = ToDo.objects.get(pk=pk)

    if request.method == 'GET':
        form = TodoForm(initial=todo.__dict__)
        return index(request, form, 'edit todo', pk=pk)

    form = TodoForm(request.POST)
    if form.is_valid():
        todo.title = form.cleaned_data['title']
        todo.description = form.cleaned_data['description']
        todo.save()
    return index(request, form)


@require_POST
def do_task(request, pk):
    todo = ToDo.objects.get(pk=pk)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect('todo index')


def delete_task(request):
    pass
