from models import TodoService

data = "dbname=todo_app user=mohammadi password=shir8844 host=localhost port=5432"


service = TodoService(data)


service.create_tables()
