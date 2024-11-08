from django.urls import path
from .views import task_list, task_create, task_update, task_delete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/new/', task_create, name='task_create'),
    path('task/<int:pk>/edit/', task_update, name='task_update'),
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),
]
