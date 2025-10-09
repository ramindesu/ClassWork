from models import TodoService

data = "dbname=todo_app user=mohammadi password=shir8844 host=localhost port=5432"


service = TodoService(data)


service.create_tables()

todo_id = service.add_todo(
    user_id=2,
    title="Learning",
    description="Practice DB with Python",
    due_time="2025-10-05 12:00:00"
)
print("Todo created:", todo_id)


# todos = service.list(2)
# print("Todos:", todos)


# service.update(1, todo_id, "done")


# service.delete(1, todo_id)