# question number 1
# def summer_69(*args):
#     result = []
#     ignore = False
#     temp = []

#     for num in args:
#         if num == 6:
#             ignore = True
#             temp = [6]
#         elif ignore:
#             temp.append(num)
#             if num == 9:
#                 ignore = False
#                 temp = []
#         else:
#             result.append(num)
#     if ignore:
#         result += temp

#     return sum(result)

# print(summer_69(1,2,3,6,5,4,2,6,5,6,9,1,6))




# question number 2 
# def fibo(n):

#     try:
#         if n < 0:
#          raise Exception ("the number must be upper than 0")
#         else :  
#             return fibo(n-1)+fibo(n-2)
#     except Exception as e:
#        print(e)

# print(fibo(12))





# question number 3
# color_list= ["red", "green", "Blue", "yellow", "Orange","hello","ali","reza"]
# def changing(color):
#     new_list = []
#     for i in color:
#         if  i[0].islower():
#             new_list.append(i.capitalize())
#         else:
#             new_list.append(i)
#     return new_list

# print(changing(color_list))



# last_names = {
#     "ramin" : "mohammadi",
#     "romina" : "mahmood",
#     "majid" : "maleki"
# }

# print(last_names,type(last_names))
# )
# 
