from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from django.db.models import Q

def todo_list_view(request):
    todo = Todo.objects.all()
    query = ''
    if request.method == "POST":
        if 'delete' in request.POST:
            id = request.POST.get("id")
            Todo.objects.get(id = id).delete()
            messages.success(request, "Todo deleted successfully!")
        elif 'search' in request.POST:
            query = request.POST.get("searchquery")
            todo = Todo.objects.filter(Q(task__icontains=query) | Q(date__icontains=query))
            
            
    content = {
        'todo': todo,
        'query': query
    }
    return render(request, 'todo.html', content)

def add_todo_view(request):
    todo = Todo.objects.all()
    
    if request.method == "POST":
        if 'add' in request.POST:
            task = request.POST.get("task")
            description = request.POST.get("description")
            date = request.POST.get("date")
            Todo.objects.create(
                task = task,
                description = description,
                date = date
            )
            messages.success(request, "Todo added Successfully!")
            return redirect('/todos')
            
    content = {"todo": todo}
    return render(request, 'add.html', content)

def edit_todo_view(request,id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        if 'save' in request.POST:
            update_todo = Todo.objects.get(id=id)
            id = request.POST.get("id")
            update_todo.task = request.POST.get("task")
            update_todo.description = request.POST.get("description")
            update_todo.date = request.POST.get("date")
            
            update_todo.save()
            
            messages.success(request, 'Todo updated successfully!')
            return redirect('/todos')
            
            
    
    return render(request, 'edit.html', {'todo':todo})


def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    print(todo)
    
    todo.delete()
    print('deleted')
    # message
    return redirect('todo:todolist')
    
