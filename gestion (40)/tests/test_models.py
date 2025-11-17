import unittest
from datetime import datetime
from source.models import Task

class TestTaskModel(unittest.TestCase):

    def test_create_task(self):
        task = Task(
            title="Prueba",
            description="Descripción",
            category="Académico",
            deadline="2025-01-15",
            priority=3,
            status="pendiente"
        )

        self.assertEqual(task.title, "Prueba")
        self.assertEqual(task.priority, 3)
        self.assertIsInstance(task.deadline, datetime)

    def test_to_dict(self):
        task = Task(
            "Test", "Desc", "Trabajo", "2025-05-20", 4, "hecho"
        )
        d = task.to_dict()

        self.assertEqual(d["title"], "Test")
        self.assertEqual(d["priority"], 4)

    def test_from_dict(self):
        data = {
            "id": "abc123",
            "title": "Tarea",
            "description": "Algo",
            "category": "Personal",
            "deadline": "2025-02-10",
            "priority": 2,
            "status": "pendiente"
        }

        task = Task.from_dict(data)

        self.assertEqual(task.id, "abc123")
        self.assertEqual(task.category, "Personal")
