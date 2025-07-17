# question number 1

class studentClass:
    def __init__(self,name,*args):
        self.name = name
        self.args = args
    
    def calculate_grades(self):
       if len(self.args) < 0 :
           return 0
       return sum(self.args) / len(self.args)
    
user_name = input("please gimme ur name")
user_grade = input("please gimme ur grades")
grade = [float(n) for n in user_grade.split()]
s1 = studentClass(user_name , *grade)

print(s1.calculate_grades())

    

        