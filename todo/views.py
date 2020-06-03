from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo


# Create your views here.

def todo_list(request):

    todos = Todo.objects.all()
    print(todos)

    context = {

        "todo_list": todos
    }
    return render(request, "todo/todo_list.html", context)



def todo_detail(request, id):
    todo= Todo.objects.get(id=id)
    context = {

    "todo": todo
    }

    return render(request, "todo/todo_detail.html", context)


def todo_create(request):

    #fill form if it is a post request
    form = TodoForm(request.POST or None)
    #check if fields filled out correctl
    if form.is_valid():
        form.save()
        return redirect ('/')

        """ all this is done by form.save()"""
        # print(form.cleaned_data)
        # name = form.cleaned_data['name']
        # due_date = form.cleaned_data['due_date']
        # print(name, due_date)
        #
        # new_todo = Todo.objects.create(name=name, due_date=due_date)
        #pass

    context = {'form': form}
    return render(request, "todo/todo_create.html", context)

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    #instance will prepolate the form with the info from todo id
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect ('/')
    context = {'form': form}
    return render(request, "todo/todo_update.html", context)

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("/")
