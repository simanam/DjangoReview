
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('add', views.addNewTodo, name='add'),
    path('complete/<task_id>', views.completeTask, name='complete'),
    path('delete', views.deleteTask, name='delete'),
    path('reset', views.resetAll, name='reset'),
    
    
]
