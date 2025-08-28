# # part A
import json
# def json_translate(data:dict):
#     output = json.dumps(data)
#     return output
    

# personal_dict = {
#     "name": "Ramin",
#     "age": 21,
#     "skills": ["python", "django", "yapping"],
#     "eamil": "ramindesu88@gmail.com"
# }

# print(json_translate(personal_dict))

# part B
# PATH = "/Users/mohammadi/Downloads/BOOTCAMP/projects/CW/data.json"

# with open(PATH,"r") as f:
#     data = json.load(f)

# for stu in data["students"]:
#     print(stu["name"])

# part C

import json

PATH = "students.json"

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

students = []
for i in range(3):
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    students.append(Student(name, age, grade))

school = {"students": [s.to_dict() for s in students]}

with open(PATH, "w") as f:
    json.dump(school, f, indent=1)
    print(f" Student information saved to {PATH}")

with open(PATH, "r") as f:
    data = json.load(f)
    print(json.dumps(data, indent=1))