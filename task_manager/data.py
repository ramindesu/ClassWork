from app import Task,User,TaskManager
from datetime import datetime ,timedelta
import pickle
path = "/Users/mohammadi/Downloads/BOOTCAMP/projects/CW/task_manager/data.pkl"


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



users = manager.user
action = manager.actions
with open(path,"wb") as f:
    pickle.dump(users,f)
    pickle.dump(action,f)

with open(path,"rb") as f:
    loaded_date = pickle.load(f)
    print(loaded_date)