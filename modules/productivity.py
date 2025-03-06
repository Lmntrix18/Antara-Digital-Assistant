import json
import os

class TaskManager:
    def __init__(self):
        self.todo_file = "data/todo.json"
        self._init_todo()

    def _init_todo(self):
        if not os.path.exists(self.todo_file):
            with open(self.todo_file, "w") as f:
                json.dump({"tasks": []}, f)

    def add_task(self, task: str):
        with open(self.todo_file, "r+") as f:
            data = json.load(f)
            data["tasks"].append({"task": task, "done": False})
            f.seek(0)
            json.dump(data, f)

    def complete_task(self, index: int):
        with open(self.todo_file, "r+") as f:
            data = json.load(f)
            if 0 <= index < len(data["tasks"]):
                data["tasks"][index]["done"] = True
                f.seek(0)
                json.dump(data, f)
                return True
            return False
