# part A
import json
def json_translate(data:dict):
    output = json.dumps(data)
    return output
    

personal_dict = {
    "name": "Ramin",
    "age": 21,
    "skills": ["python", "django", "yapping"],
    "eamil": "ramindesu88@gmail.com"
}

print(json_translate(personal_dict))

