from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def index(request):
    input_dict = {
        'page_title': "Home",
    }
    return render(request, 'index.html', input_dict)

def todolistapp(request):
    try:
        todo_instance = TodoModel.objects.all()
    except:
        pass
    if request.method == "POST":
        new_todo = TodoModel(
            title = request.POST['title'],
        )
        new_todo.save()
        return redirect('todo')
    
    data = {
        'page_title': "App",
        'todo_instance': todo_instance,
    }

    return render(request, 'todo.html', data)

def delete_item(request, pk):
    todo_instance = TodoModel.objects.get(id=pk)
    todo_instance.delete()
    return redirect('todo')
