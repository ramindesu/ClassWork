from models import TodoService

data = "dbname=todo_app user=mohammadi password=shir8844 host=localhost port=5432"


service = TodoService(data)


service.create_tables()

todo_id = service.add_todo(
    user_id=1,
    title="Learn psycopg",
    description="Practice DB with Python",
    due_time="2025-10-05 12:00:00"
)
print("Todo created:", todo_id)


todos = service.list_todos(1)
print("Todos:", todos)


service.update_todo_status(1, todo_id, "done")


service.delete_todo(1, todo_id)