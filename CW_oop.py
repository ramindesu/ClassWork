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


# tem1 = Thermometer(cel=23)
# print(tem1.to_far())
# question number 8
# class Employee:
#     employee_counter = []

#     def __init__(self, name, age, salary):
#         Employee.employee_counter.append(self)
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.all_salary = []

#     def decribe(self):
#         return f"this employee {self.name} age: {self.age} with salary {self.salary}"

#     def give_raise(self, add):
#         self.salary += add
#         return f"{add} just added to the salary new salary is {self.salary}"

#     def validate_salary(self):
#         return f"this person{self.name} got his salary{self.salary}"

#     @classmethod
#     def give_raise_to_all(cls, add):
#         for employee in cls.employee_counter:
#             employee.salary += add
#         return "all employees got a raise"

#     @classmethod
#     def avg_salary(cls):
#         total = sum(employee.salary for employee in cls.employee_counter)
#         return total / len(cls.employee_counter)

#     @classmethod
#     def validate_name(cls, name):
#         for employee in cls.employee_counter:
#             if employee.name == name:
#                 return True
#         return False


# # question 9:
# class Class:
#     class_series = 10

#     def __init__(self, name, master, studens):
#         self.name_class = name
#         self.master = master
#         self.students = studens
#         Class.class_series += 10
#         self.class_id = Class.class_series

#     def avg_grades(self):
#         total = sum(student.grade for student in self.student)
#         return total // len(self.students)

#     def qty_of_students(self):
#         return len(self.students)

#     def top_five(
#         self,
#     ):
#         pass


# class Human:
#     def __init__(self, name_lname, number, age, email):
#         self.name = name_lname
#         self.number = number
#         self.age = age
#         self.mail = email


# class Master(Human):
#     master_id = 0

#     def __init__(self, name_lname, number, age, email):
#         Master.master_id += 10
#         self.master_id = Master.master_id
#         super().__init__(name_lname, number, age, email)


# class student(Human):
#     student_id = 0

#     def __init__(self, name_lname, number, age, email, grade):
#         self.grade = grade
#         super().__init__(name_lname, number, age, email)


# # question 1
# class User:
#     def __init__(self, password):

#         self.__password = None
#         self.change_pass = password

#     @property
#     def change_pass(self):
#         return self.__password

#     @change_pass.setter
#     def change_pass(self, value):
#         if isinstance(value, str) and len(str(value)) > 8:
#             self.__password = value
#         else:
#             raise ValueError(
#                 "the pass word must be more than 8 character and must be string"
#             )


# # questin number 2
# class Book:
#     def __init__(self, title, id, price, writers):
#         self.title = title
#         self.id = id
#         self.price = price
#         self.writers = writers

#     def show_info(self):
#         return f"{self.title} - ID: {self.id}, Price: {self.price}"


# class PrintedBook(Book):
#     def __init__(self, title, id, price, page, writers):
#         self.page = page
#         super().__init__(title, id, price, writers)

#     def show_info(self):
#         return f"{self.title} (Printed), ID: {self.id}, Price: {self.price}, Pages: {self.page}"


# class ElectronicBook(Book):
#     def __init__(self, title, id, price, file_size, writers):
#         self.file_size = file_size
#         super().__init__(title, id, price, writers)

#     def show_info(self):
#         return f"{self.title} (E-Book), ID: {self.id}, Price: {self.price}, File Size: {self.file_size}MB"


# class Author:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email


# a1 = Author("Ramin", "ramin@example.com")
# a2 = Author("Sara", "sara@example.com")

# book1 = PrintedBook("Python 101", 1, 150, 300, [a1, a2])
# book2 = ElectronicBook("JavaScript Guide", 2, 100, 5, [a1])

# print(book1.show_info())
# print(book2.show_info())


# question number 3
# class Score:
#     def __init__(self, value):
#         if isinstance(value, int):
#             self.value = value
#         else:
#             raise TypeError

#     def show_value(self):
#         return self.value

#     def __add__(self, other):
#         if isinstance(other, Score):
#             return Score(self.value + other.value)
#         return "not found"

#     def __sub__(self, other):
#         if isinstance(other, Score):
#             return Score(self.value - other.value)
#         return "not found"


# s1 = Score(23)
# s2 = Score(42)
# print(s1.show_value())
# print(s2.show_value())
# # print(s1.show_value())
# s3 = s1 + s2
# s4 = s2 - s1
# print(s3.show_value())
# print(s4.show_value())
# class Post:
#     def __init__(self, content, post_id, like=0, share=0):
#         self.content = content
#         self.post_id = post_id
#         self.like = like
#         self.share = share

#     def show_full_info(self):
#         return f"ID: {self.post_id} Content: {self.content}, Likes: {self.like}, Shares: {self.share}"

#     def show_limited_info(self):
#         return f"Content: {self.content}"


# class Profile:
#     def __init__(self, name, email, join_date,type):
#         self.name = name
#         self.email = email
#         self.join_date = join_date
#         self.type = type
#         self.posts = []

#     def create_post(self, post_id, content, like=0, share=0):
#         post = Post(content, post_id, like, share)
#         self.posts.append(post)

#     def show_posts(self):
#         raise NotImplementedError("Subclasses must implement this method")


# class PremiumUser(Profile):
#     def show_posts(self):
#         return [post.show_full_info() for post in self.posts]

#     def total_likes(self):
#         return sum(post.like for post in self.posts)

#     def total_shares(self):
#         return sum(post.share for post in self.posts)

#     def del_post(self, post_id):
#         for post in self.posts:
#             if post.post_id == post_id:
#                 self.posts.remove(post)
#                 return f"Post {post_id} deleted."
#         return "Post not found."

#     def edit(self, id, value):
#         for post in self.posts:
#             if post.post_id == id:
#                 post.content = value


# class StandardUser(Profile):
#     def show_posts(self):
#         return [post.show_limited_info() for post in self.posts]


# user1 =PremiumUser("name","email",2024,"permium")
# user1.create_post(103,"hello world",20,25)
# user1.create_post(104,"hello hell",20,25)

# # print(user1.show_posts())
# # print(user1.total_likes())
# # print(user1.total_shares())
# # print(user1.del_post(104))
# print(user1.edit(103,"made in heaven"))
# print(user1.show_posts())


# question number2
# class SchoolStaff:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role

#     def set_grade(self, student, grade):
#         if self.role == "teacher" and 0 <= grade <= 20:
#             student.grade = grade
#         else:
#             if self.role != "teacher":
#                 raise PermissionError("Only teachers can set grades")
#             if not 0 < grade <= 20:
#                 raise ValueError("Grade must be between 0 and 20")


# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade


# def question number 3
# class Book:
#     def __init__(self, title, author, published):
#         self.title = title
#         self.author = author
#         self.published = published

#     def __repr__(self):
#         return f"{self.title} by {self.author} ({self.published})"


# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         if book in self.books:
#             return "This book already exists."
#         self.books.append(book)

#     def delete(self, book):
#         if book in self.books:
#             self.books.remove(book)
#         else:
#             return "This book doesn't exist."

#     def searching(self, title):
#         for book in self.books:
#             if book.title == title:
#                 return book
#         return "Book doesn't exist."

#     def __len__(self):
#         return len(self.books)

#     def __getitem__(self, key):
#         if isinstance(key, int):
#             return self.books[key]
#         return "Not found."

#     def __iter__(self):
#         return iter(self.books)

#     def __contains__(self, book):
#         return any(b.title == book.title for b in self.books)


# # question number 1
from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape): #
#     def __init__(self, width, height):
#         if width > 0 and height > 0:
#             self.width = width
#             self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)


# class Circle(Shape):
#     def __init__(self,radius , pi =3.141629):
#         if radius > 0 :
#             self.pi = pi
#             self.radius = radius

#     def perimeter(self):
#         return self.pi * (self.radius **2)

#     def area(self):
#         return 2*self.pi*self.radius


# class Tingle(Shape):
#     def __init__(self,side_a,side_b,base,height):
#         if (side_a,side_b,base,height) > 0:
#             self.side_a = side_a
#             self.side_b = side_b
#             self.base = base
#             self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

#     def perimeter(self):
#         perimeter_of_tringle = self.side_a + self.side_b + self.base
#         return perimeter_of_tringle

# question number 2
# class ReprMixin:
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.__dict__})"

#     def __str__(self):
#         return f"{self.__class__.__name__} object"

# class Book(ReprMixin):
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year


# class Car(ReprMixin):
#     def __init__(self, brand, model, year, color):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color

# book = Book("The Alchemist", "Paulo Coelho", 1988)
# car = Car("Toyota", "Corolla", 2020, "White")

# # print(book)
# # print(repr(book))
# # print(car)
# # print(repr(car))


# # question number 3


# class VehicleFactory(ABC):

#     @abstractmethod
#     def create_vehicle(self):
#         pass


# class Car:
#     def __init__(self):
#         pass

#     def creat(self):
#         return "created a car"


# class Bike:
#     def __init__(self):
#         pass

#     def creat(self):
#         return "created a bike"


# class CarFactory(VehicleFactory):
#     def create_vehicle(self):
#         return Car()


# class BikeFactory(VehicleFactory):
#     def create_vehicle(self):
#         return Bike()


# def get_factory(vehicle_type):
#     if vehicle_type.lower() == "car":
#         return CarFactory()
#     elif vehicle_type.lower() == "bike":
#         return BikeFactory()

# f = get_factory("car")
# v = f.create_vehicle()
# print(v.creat())


# # question 4
# # class Song:
# #     def __init__(self,name,type,min):
# #         self.name = name
# #         self.type = type
# #         self.min = min

# # class Plylist:
# #     def __init__(self):
# #         self.song_list = []

# #     def add_songs(self,songs):
# #         self.song_list.append(songs)

# #     def remove_song(self,song):
# #         for songs in self.song_list:
# #             if songs.name == song:
# #                 self.song_list.remove(songs)

# #     def total_duration(self):
# #         all_min = 0
# #         for song in self.song_list:
# #             all_min += song.min
# #         return all_min

# # s1 = Song("Shape of You", "Pop", 4)
# # s2 = Song("Thunder", "Rock", 3)

# # pl = Plylist()
# # pl.add_song(s1)
# # pl.add_song(s2)

# # print("Total Duration:", pl.total_duration())
# # pl.remove_song("Shape of You")
# # print("Total Duration after removal:", pl.total_duration())


# # qustion 1
# class Employee(ABC):

#     @abstractmethod
#     def calc_salary(self):
#         pass


# class HourlyEmployee(Employee):
#     PAY_HOUR = 8

#     def __init__(self, name, hours, role, hourly_id):

#         self.name = name
#         self.hours = hours
#         self.role = role
#         self.id = hourly_id

#     def calc_salary(self):
#         return self.hours * self.PAY_HOUR


# class SalariedEmployee(Employee):

#     MONTH_DAY = 30

#     def __init__(self, name, role, days, emp_id, monthly_pay):
#         self.name = name
#         self.role = role
#         self.days = days
#         self.id = emp_id
#         self.monthly_pay = monthly_pay

#     def calc_salary(self):
#         return (self.monthly_pay / self.MONTH_DAY) * self.days


# class Manager(SalariedEmployee):
#     def __init__(self, name, role, days, emp_id, monthly_pay, section, commission):
#         self.commission = commission
#         self.section = section

#         super().__init__(name, role, days, emp_id, monthly_pay)

#     def calc_salary(self):
#         each_day = self.monthly_pay / self.MONTH_DAY
#         monthly = each_day * self.days
#         return monthly + self.commission


# class Executive(SalariedEmployee):
#     def __init__(
#         self,
#         name,
#         role,
#         days,
#         emp_id,
#         monthly_pay,
#         department,
#     ):
#         self.department = department
#         super().__init__(name, role, days, emp_id, monthly_pay)


# class Company:
#     def __init__(self):
#         self.emps = []

#     def hire_emp(self, emp):
#         self.emps.append(emp)
#         return f"u just hired {emp.name}"

#     def fire_emp(self, id):
#         for emp in self.emps:
#             if emp.id == id:
#                 self.emps.remove(emp)

#     def give_raise(self, id, amuont):
#         for emp in self.emps:
#             if emp.id == id:
#                 if isinstance(emp, HourlyEmployee):
#                     HourlyEmployee.PAY_HOUR += amuont
#                 else:
#                     emp.monthly_pay += amuont
#         return "Employee not found."


# c = Company()
# e1 = HourlyEmployee("Ali", 40, "cleaner", 1)
# print(e1.name)
# print(e1.calc_salary())
# e2 = Manager("Sara", "IT", 30, 2, 2000, "develop", 200)

# print(c.hire_emp(e1))
# print(c.hire_emp(e2))

# print("Ali's Salary:", e1.calc_salary())
# print("Sara's Salary:", e2.calc_salary())
# print(c.give_raise(1, 2))
# print("Ali's New Salary:", e1.calc_salary())


# question 2

# class Logger:
#     def __init__(self,filename):
#         self.filename = filename
#         self.file = open(self.filename,"a")
#         print(f"opened {self.filename}")

#     def write(self,massage):
#         self.file.write(massage + "\n")

#     def __del__(self):
#         self.file.close()
#         print(f"{self.filename} is closed")

# logger = Logger("log.txt")
# logger.write("hello world")
# logger.write("Something")


# del logger


# questiom 3


# def calc_circle_area(radius):
#  """
#     Calculate the area of a circle using the formula:
#         circumference = 2 * π * radius

#     Args:
#         radius:  radius of the circle.

#     Returns:
#         float:  area of the circle.
#     """
# return 2 * 3.14 * radius


# class ReportGenerator:
#     def generate(self) :
#         """
#         Generates the content of the report.
#         Returns:
#             str: The content of the report.
#         """
#         return "Report content"


# class FileSaver:
#     def save_to_file(self, content, filename):
#         """
#         Saves the given content to a file.

#         """
#         with open(filename, 'w') as f:
#             f.write(content)


# def read_file(filename):
#     """
#     Reads all lines from the given file.

#     """
#     with open(filename) as f:
#         return f.readlines()


# def clean_lines(lines) :
#     """
#     Removes whitespace and newline characters from each line.
#     """
#     return [line.strip() for line in lines]


# def parse_numbers(lines):
#     """
#     Filters lines that are purely digits and converts them to integers.
#     """
#     return [int(x) for x in lines if x.isdigit()]

# def process_data(filename):
#     """
#     Reads, cleans, and parses numeric data from a file.
#     """
#     raw_lines = read_file(filename)
#     cleaned = clean_lines(raw_lines)
#     numbers = parse_numbers(cleaned)
#     print(len(numbers))

# def process_data(filename):
#     with open(filename) as f:
#         lines = f.readlines()
#     cleaned = [line.strip() for line in lines]
#     data = [int(x) for x in cleaned if x.isdigit()]
#     print("Processed", len(data), "items")


def role_requires(role):
    def role_dec(func):
        def wrapper(self):
            if self.role == role:
                return func(self)
            else:
                raise PermissionError("u dont have the accses")
        return wrapper
    return role_dec



class User:
    def __init__(self,name,role):
        self.name = name
        self.role = role

    def view_profile(self):
        return "veiwing profile"
    
    def edit_profile(self):
        return "editing profile"
    
    @role_requires("admin")
    def delete_account(self):
        return "deleting acount"
        
admin = User("ramin", "admin")
guest = User("guest", "viewer")
try:
    print(admin.delete_account())  

    print(guest.delete_account())  
except Exception as e:
    print (e)