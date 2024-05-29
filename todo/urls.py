from django.urls import path
from .views import *

app_name = 'todo'

urlpatterns = [
    path('todos/', todo_list_view, name='todolist'),
    path('add/', add_todo_view, name='add'),
    path('edit/<int:id>', edit_todo_view, name='edit'),
    path('delete/<int:id>', delete_todo, name='delete'),
    
]