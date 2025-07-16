
# question number 1
# def prime_number(n):
#     if n <= 1:
#         print("It's not a prime number")
#         return
#     if n == 2 :
#         print("It's a prime number")
#         return
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             print("It's not a prime number")
#             return
#     print("It's a prime number")

# user_input = int(input("Gimme a number: "))
# prime_number(user_input)




# question number 2
# user_input = input("please gimme ur numbers ")
# user_input_int = [int(user_input) for user_input in user_input.split()]
# def calc_total_numbers(*nums):
#     total_sum = 0 
#     for i in nums:
#         total_sum+= i
#     print(total_sum)

# calc_total_numbers(*user_input_int)
# calc_total_numbers(1,2,3,4,5,6)




# question number 3
# user_city = input("ur city ") or "not entred"
# user_name = input("ur name ") or ("not entred")
# user_Lname = input("ur Lname ") or ("not entred")



# def greet(city=" not entred",name= "not entered",Lname = "not entred"):
#     print(f"ur name is {name} , ur city is {city} and ur last name {Lname}")
# greet(user_city,user_name,user_Lname)




# question number 4
# def calc(num1,num2,oper="sum"):
#     if oper=="sum":
#         return num1 + num2
#     if oper=="min":
#         return num1 - num2
#     if oper== "div":
#         return num1/num2
#     return num1 * num2

# print(calc(2,3,"mult"))

# question number 5
# def even_detact(n):
#     if n % 2 == 0:
#         return True
#     return False

# print(even_detact(5))


# question number 6 
# def avg(*n):
#     sum_of_list = 0
#     iter = 0
#     for i in n:
#         sum_of_list += i
#         iter += 1  
#         avg = int(sum_of_list/iter)
#         return avg
    
# print(avg(2,2,2,2,2))







# question number 7

# user_input = input("please gimme a name or number: ")
# user_input_list = user_input.split()
# user_nums= []
# user_others = []
# for i in user_input_list :
#     if i.isdigit():
#         user_nums.append(int(i))
#     user_others.append(i)
# with open("/Users/mohammadi/Downloads/BOOTCAMP/projects/text.txt", "a") as f:
#     f.write(user_others+user_nums + "\n") 
# numbers = []
# others = []
# with open("/Users/mohammadi/Downloads/BOOTCAMP/projects/text.txt", "r") as f:

#     for line in f:
#         line = line.strip()
#         digits = ''
#         letters = ''
        
#         for i in line:
#             if i.isdigit():
#                 if letters:
#                     others.append(letters)
#                     letters = ''
#                 digits += i
            
#             else:
#                 if digits:
#                     numbers.append(int(digits))
#                     digits = ''
#                 letters += i   

#         if digits:
#             numbers.append(int(digits))
#         if letters:
#             others.append(letters.strip())  


# def calc_average(*nums):
#     if len(nums) == 0:
#         return 0
#     return sum(nums) / len(nums)

# average = calc_average(*numbers)
# print("Numbers:", numbers)
# print("Others:", others)
# print("Average of numbers:", average)




# question 8
# user_fav_item = input("gimme the name of ur fav item ").strip()
# with open("/Users/mohammadi/Downloads/BOOTCAMP/projects/practice/text.txt", "r") as ff:
#     user_list = [line.strip() for line in ff.readlines()] 

#     try:
#         if user_fav_item in user_list:
#             raise Exception("this name is already exist") 
#         else:
#             with open("/Users/mohammadi/Downloads/BOOTCAMP/projects/practice/text.txt", "a") as f:
#                 f.write(f"{user_fav_item}\n")
#         print("done")
#         with open("/Users/mohammadi/Downloads/BOOTCAMP/projects/practice/text.txt", "r") as ff:
#             user_list = [line.strip() for line in ff.readlines()] 

#     except Exception as e:
#         print(e)

#     print(user_list)






# question number 9 :
# with open ("/Users/mohammadi/Downloads/BOOTCAMP/projects/text.txt","r") as f:
#     content = f.read()
# try:
#     if not content :
#         raise Exception("this list is empty")
#     print("done")
# except Exception as e:
#     print(e)



# question number 10


# user_input = input("gimme ur txt ")
# try:
#     user_index = int(input("now ur index "))
# except ValueError:
#     print("the value shoud be inteeger")
#     exit()
# def index_returner(name,index):
#     return name[index]
# try:
#     if user_index >= len(user_input):
#         raise Exception("the index is too high to return")
# except Exception as e:
#     print(e)

# print(index_returner(user_input,user_index))




# question number 11
# def extract_file(filename,keyword="ERROR"):
#     result = []
#     with open(filename) as f :
#         file = f.readlines()
#         for line in file:
#             if keyword in line:
#                 result.append(line.strip())
#     return result

# print(extract_file("/Users/mohammadi/Downloads/BOOTCAMP/projects/text.txt","INFO"))



# question number 12
# user_input = input("how are u feeling today ")
# def user_status(status="ur status",user_msg=""):
#     with open ("/Users/mohammadi/Downloads/BOOTCAMP/projects/text.txt","w") as f:
#         f.write(status + user_msg)
#         with open("/Users/mohammadi/Downloads/BOOTCAMP/projects/text.txt") as r:
#             reading = r.read()
#             return reading
# print(user_status(user_input))
