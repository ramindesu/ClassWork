import validate as v
from datetime import datetime, timedelta


class Task:
    def __init__(self, title, task_id, content, status, start, deadline):
        self.title = v.validation_title(title)
        self.task_id = task_id
        self.content = content
        self._status = status
        self.start = start
        self.deadline = deadline

    def __repr__(self):
        return f"Task({self.title}, status={self._status})"

    @property
    def status(self):
        if self._status == "done":
            return "task is completed"
        now = datetime.now()
        if now > self.deadline:
            self._status = "behind the schedule"
            return "its behind the schedule"
        else:
            self._status = "in process"
            return "in process"


class User:
    def __init__(self, name, gmail, phone, password, tasks=None):
        self.name = v.validate_username(name)
        self.gmail = v.validate_email(gmail)
        self.phone = v.validate_phone(phone)
        self.password = v.validate_password(password)
        self.tasks = tasks if tasks else []

    def add_task(self, task: Task):
        if not isinstance(task, Task):
            raise v.ValidationError("must be object from Task class")
        self.tasks.append(task)

    def remove_task(self, task: Task):
        if not isinstance(task, Task):
            raise v.ValidationError("must be object from Task class")
        if task not in self.tasks:
            raise v.NotFound("not found")
        self.tasks.remove(task)

    def change_status(self, task: Task, status):
        task._status = status
        return "done"

    def show_tasks(self):
        for task in self.tasks:
            print(task)

    def search_date(self, date):
        return [task for task in self.tasks if task.start == date or task.deadline == date]

    def search_content(self, content):
        return [task for task in self.tasks if task.content == content]


class TaskManager:
    def __init__(self):
        self.user = []
        self.actions = {"actions": {}}

    def _actions(self, time, job):
        self.actions["actions"][time] = job

    def add_user(self, user: User):
        self.user.append(user)
        self._actions(datetime.now(), f"add {user.name}")

    def remove_user(self, user: User):
        self.user.remove(user)
        self._actions(datetime.now(), f"remove user {user.name}")




# fake validate 
class FakeValidate:
    def validation_title(self, x): return x
    def validate_username(self, x): return x
    def validate_email(self, x): return x
    def validate_phone(self, x): return x
    def validate_password(self, x): return x
    class ValidationError(Exception): pass
    class NotFound(Exception): pass

v = FakeValidate()


t1 = Task("Finish project", 1, "coding", "in process", datetime.now(), datetime.now() + timedelta(days=1))
t2 = Task("Go to gym", 2, "fitness", "in process", datetime.now(), datetime.now() - timedelta(days=1))


u1 = User("ramin", "r@gmail.com", "123456", "pass")
u1.add_task(t1)
u1.add_task(t2)


u1.show_tasks()
print("Search content = coding →", u1.search_content("coding"))
print("Task statuses:")
for task in u1.tasks:
    print(task.title, ":", task.status)


manager = TaskManager()
manager.add_user(u1)
print("Actions log:", manager.actions)