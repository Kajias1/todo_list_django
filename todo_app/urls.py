# my_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.get_tasks, name='get_tasks'),
    path("task/", views.get_task, name='get_task'),
]
