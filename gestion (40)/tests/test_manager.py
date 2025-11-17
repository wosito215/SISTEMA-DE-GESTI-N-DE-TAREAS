from source.models import Task

class TaskManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, task):
        self.tasks.append(task)
        self.sort_tasks()
        self.storage.save(self.tasks)

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.storage.save(self.tasks)

    def update_task(self, updated_task):
        for index, task in enumerate(self.tasks):
            if task.id == updated_task.id:
                self.tasks[index] = updated_task
                break

        self.sort_tasks()
        self.storage.save(self.tasks)

    def get_all_tasks(self):
        return self.tasks

    def sort_tasks(self):
        """Ordena de mayor a menor prioridad."""
        self.tasks.sort(key=lambda t: t.priority, reverse=True)
