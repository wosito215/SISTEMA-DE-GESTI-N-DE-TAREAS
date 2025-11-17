import json
import os
from source.models import Task

class JSONStorage:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write("[]")

    def save(self, tasks):
        """Guarda una lista de objetos Task en el archivo JSON."""
        data = [task.to_dict() for task in tasks]

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load(self):
        """Carga tareas desde el JSON y devuelve una lista de Task."""
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []

            data = json.loads(content)

        return [Task.from_dict(item) for item in data]
