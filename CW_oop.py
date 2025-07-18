# # question number 1


# class studentClass:
#     def __init__(self, name, *args):
#         self.name = name
#         self.args = args

#     def calculate_grades(self):
#         if len(self.args) < 0:
#             return 0
#         return sum(self.args) / len(self.args)


# user_name = input("please gimme ur name")
# user_grade = input("please gimme ur grades")
# grade = [float(n) for n in user_grade.split()]
# s1 = studentClass(user_name, *grade)

# print(s1.calculate_grades())


# # question number 2
# class Bank:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, add):
#         self.balance += add
#         return f"{add} added to ur acount new balance {self.balance}"

#     def withdraw(self, bardasht):
#         if self.balance < bardasht:
#             return "ur balance is low"
#         self.balance -= bardasht
#         return f"{bardasht} of ur balance , new balance{self.balance}"

#     def cheack_balance(self):
#         return f" here,its ur balance {self.balance}"


# question number 3


# class Recktangle:
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width

#     def area(self):
#         area_of_reactangle = (self.width + self.lenght) *2
#         return area_of_reactangle

#     def perimeter(self):

#         perimeter_of_recktangle = self.width * self.lenght
#         return perimeter_of_recktangle

# t1 = Recktangle(12,6)
# print(t1.area())
# print(t1.perimeter())


# question number 4 =
# class Book:
#     list_of_books = list()

#     def __init__(self, name, authtor, price):
#         self.name = name
#         self.author = authtor
#         self.price = price


# my_books = [
#     Book("math", "person1", 1200),
#     Book("physics", "person2", 1300),
#     Book("chemistry", "person2", 1100),
#     Book("python", "person4", 1500),
# ]


# def getting_book(books, price):
#     for book in books:
#         if book.price < price:
#             return book.name


# print(getting_book(my_books, 1200))


# question number 5
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def discribe(self):
#         print(f"this is an employee name {self.name} with a salary of {self.salary}")


# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         self.department = department
#         super().__init__(name, salary)

#     def discribe(self):
#         print(
#             f"this is {self.name} manager of {self.department} department with salary of {self.salary}"
#         )

# ali = Employee("ali" , 200)
# reza = Manager("reza" , 400 , "sells")
# for name in [ali , reza]:
#     name.discribe()


# question number 6

# class Robot:
#     counter = 0
#     def __init__(self):
#         Robot.counter += 1
#         self.robot_crated = Robot.counter

# r1 = Robot()
# r2 = Robot()
# r3 = Robot()
# r4 = Robot()
# print(Robot.counter)


# # question number 7
# class Thermometer:
#     def __init__(self, cel=None, far=None):
#         self.cel = cel
#         self.far = far

#     def to_cel(self):
#         if self.far is None:
#             return "You didn't enter the Fahrenheit temperature."
#         return (self.far - 32) * 5 / 9

#     def to_far(self):
#         if self.cel is None:
#             return "You didn't enter the Celsius temperature."
#         return (self.cel * 9 / 5) + 32
