from django.test import TestCase, Client
from .models import Task
from .api import TaskSchema
import json

class APITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            status="created"
        )

    def test_get_tasks(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
        tasks = json.loads(response.content)
        self.assertEqual(len(tasks), 1)

    def test_create_task(self):
        task_data = {
            "title": "New Task",
            "description": "This is a new task",
            "status": "created"
        }
        response = self.client.post('/tasks/', data=json.dumps(task_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        task = Task.objects.get(title="New Task")
        self.assertIsNotNone(task)

    def test_update_task(self):
        task_data = {
            "title": "Updated Task",
            "description": "This is an updated task",
            "status": "completed"
        }
        response = self.client.put(f'/tasks/{self.task.id}/', data=json.dumps(task_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.title, "Updated Task")

    def test_delete_task(self):
        response = self.client.delete(f'/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=self.task.id)

