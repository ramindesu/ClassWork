from models import UniService
import pprint

data = "dbname=uni user=mohammadi password=shir8844 host=localhost port=5432"

service = UniService(data)
service.create_tables()
