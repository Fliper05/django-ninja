from django.urls import path
from . import api

urlpatterns = [
    path('tasks/', api.get_tasks),
    path('tasks/', api.create_task),
    path('tasks/<int:task_id>/', api.update_task),
    path('tasks/<int:task_id>/', api.delete_task),
]
