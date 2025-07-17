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
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, add):
        self.balance += add
        return f"{add} added to ur acount new balance {self.balance}"

    def withdraw(self, bardasht):
        if self.balance < bardasht:
            return "ur balance is low"
        self.balance -= bardasht
        return f"{bardasht} of ur balance , new balance{self.balance}"

    def cheack_balance(self):
        return f" here,its ur balance {self.balance}"


