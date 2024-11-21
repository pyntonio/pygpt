# assistants/personal_assistant.py
import datetime

class PersonalAssistant:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, due_date):
        task_data = {"task": task, "due_date": due_date}
        self.tasks.append(task_data)
        return f"Task '{task}' added."

    def view_tasks(self):
        return self.tasks

    def delete_task(self, task):
        self.tasks = [t for t in self.tasks if t["task"] != task]
        return f"Task '{task}' deleted."

    def check_due_tasks(self):
        today = datetime.date.today()
        due_tasks = [t for t in self.tasks if t["due_date"] == today]
        return due_tasks if due_tasks else "No tasks due today."
