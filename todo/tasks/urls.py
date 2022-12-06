from django.urls import path
from . import views
urlpatterns = [
    path('helloworld/', views.helloworld),
    
    path('', views.taskList, name='task-list'),
    
    path('task/<int:id>', views.taskView, name="task-view"),
    
    path("newtask/", views.newTask, name="new-task"),
    
    path('yourname/<str:name>', views.yourname, name= 'yourname'),
    
    path('edit/<int:id>', views.editTask, name='edit-task'),
    
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    
    path("delete/<int:id>", views.deleteTask, name='delete-task'),
    
   
]
