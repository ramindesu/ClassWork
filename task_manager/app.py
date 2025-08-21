import validate as v
from datetime import datetime


class Task:
    def __init__(self, title, task_id, content, status, start, deadline):
        self.titlle = v.validation_title(title)
        self.task_id = task_id
        self.content = content
        self.status = status
        self.start = start
        self.deadline = deadline


class User:
    def __init__(self, name, gmail, phone, password, tasks: Task):
        self.name = v.validate_username(name)
        self.gmail = v.validate_email(gmail)
        self.phone = v.validate_phone(phone)
        self.password = v.validate_password(password)
        self.tasks = tasks if tasks else []

    def add_task(self, tasks: Task):
        if not isinstance(tasks, Task):
            raise v.ValidationError("must be object from task class")
        self.tasks.append(tasks)

    def remove_task(self, task: Task):
        if not isinstance(task, Task):
            raise v.ValidationError("must be object from task class")
        if task not in self.tasks:
            raise v.NotFound("not found")
        self.tasks.remove(task)
