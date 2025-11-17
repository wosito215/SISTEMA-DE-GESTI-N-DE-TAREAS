import unittest
import os
from datetime import datetime
from source.storage_json import JSONStorage
from source.models import Task


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.file = "test_data.json"
        if os.path.exists(self.file):
            os.remove(self.file)

        self.storage = JSONStorage(self.file)

    def tearDown(self):
        if os.path.exists(self.file):
            os.remove(self.file)

    def test_save_and_load(self):
        tasks = [
            Task("A", "Desc A", "Personal", "2025-01-01", 5, "Pendiente"),
            Task("B", "Desc B", "Trabajo", "2025-02-01", 2, "Completada"),
        ]

        self.storage.save(tasks)
        loaded = self.storage.load()

        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].title, "A")
        self.assertEqual(loaded[1].priority, 2)
