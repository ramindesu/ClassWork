# def fibonacci(n):
#     if n == 0:
#         yield 0
#         return
#     elif n == 1:
#         yield 0
#         yield 1
#         return
#     else:
#         prev = list(fibonacci(n - 1))
#         yield from prev
#         yield prev[-1] + prev[-2]
# print(list(fibonacci(23)))


# question number 2

import time


# def tim_cheaker(func):
#     def wrapper():
#         star = time.time()
#         result = func()
#         end = time.time()
#         duretion = end - star
#         print(duretion)
#         return result

#     return wrapper


# def counter():
#     count = 1
#     while True:
#         yield count
#         count += 1

# @tim_cheaker
# def seconds():
#     start = time.time()
#     for sec in counter():
#         print(sec)
#         if time.time() - start == 5.0:
#             break

# seconds()

# question numner 3


# def access(role_required):
#     def decorator(func):
#         def wrapper(self, *args, **kwargs):
#             if self.role == role_required:
#                 return func(self, *args, **kwargs)
#             else:
#                 print(f"Access denied. You need the '{role_required}' role to perform this action.")
#                 return None
#         return wrapper
#     return decorator

# class Project_System:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#         self.project = []
#     @access("manager")
#     def add_project(self, project):
#         self.project.append(project)
#     @access("manager")
#     def remove_project(self, project):
#         if project in self.project:
#             self.project.remove(project)
    
