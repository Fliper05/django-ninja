from ninja import NinjaAPI, Schema
from .models import Task
import datetime

api = NinjaAPI()

class TaskSchema(Schema):
    title: str
    description: str
    created_at: datetime.datetime
    completed_at: datetime.datetime
    status: str

@api.get("/tasks", response={200: list[TaskSchema]})
def get_tasks(request):
    tasks = Task.objects.all()
    return [TaskSchema.from_orm(task) for task in tasks]

@api.post("/tasks", response={201: TaskSchema})
def create_task(request, task: TaskSchema):
    task_obj = Task.objects.create(**task.dict())
    return TaskSchema.from_orm(task_obj)

@api.put("/tasks/{task_id}", response={200: TaskSchema})
def update_task(request, task_id: int, task: TaskSchema):
    task_obj = Task.objects.get(id=task_id)
    for attr, value in task.dict().items():
        setattr(task_obj, attr, value)
    task_obj.save()
    return TaskSchema.from_orm(task_obj)

@api.delete("/tasks/{task_id}", response={200: {"message": str}})
def delete_task(request, task_id: int):
    task_obj = Task.objects.get(id=task_id)
    task_obj.delete()
    return {"message": "Task deleted"}
