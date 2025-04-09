from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('toggle/<uuid:task_id>/', views.toggle_task_completion, name='toggle_task'),
    path('delete/<uuid:task_id>/', views.delete_task, name='delete_task'),
    path('incomplete/', views.task_list_incomplete, name='task_list_incomplete'),
    path('complete/', views.task_list_complete, name='task_list_complete'),
    path('overdue/', views.task_list_overdue, name='task_list_overdue'),
]
