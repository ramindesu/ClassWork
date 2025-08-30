import requests
import os
os.system("clear")
# imagine u go to a resturant and order somthing from the menu the waiter(api) sends ur request to the kitchen(back-end) and it gives ur food(ur respond)
# so yeah it a way that machines talk to eachother 
# EXAMPLE:
# hows the weather in tehran?
# response:  {"temp": 29, "description": "Sunny"}

# --------------------------------------------------
# PART B
# ---------------------------------------------------
# part C
# -------------------------------------------------------

# QUESTION 2 PART 1
# def status_checker(url):

#     url_get = requests.get(url)
#     url_status = url_get.status_code
#     if 200 <= url_status < 300:
#         print("Successful")
#     elif 300 <= url_status < 400:
#         print("Redirection")
#     elif 400 <= url_status < 500:
#         print("Bad request")
#     elif 500 <= url_status < 600:
#         print("Server error")
#     else:
#         print(url_status)


# status_checker("https://www.w3schools.com/tags/ref_httpmessages.asp")
# status_checker("https://www.w3schools.com/tags/ref_httpmessages.asp/qweqweq")

# -------------------------------------------------------------------------------
# QUESTION 2 PART 2
# def status_checker(url):

#     url_get = requests.get(url)
#     url_status = url_get.status_code
#     if 200 <= url_status < 300:
#         print("Successful")
#     else:
#         print("somthing went wrong")
    
# status_checker("https://www.w3schools.com/tags/ref_httpmessages.asp")
# status_checker("https://www.w3schools.com/tags/ref_httpmessages.asp/qweqweq")
# -------------------------------------------------------------------------------
URL = "https://jsonplaceholder.typicode.com/todos"

res = requests.get(URL)
todos = res.json()

done_per_user = {}

for t in todos:
    if t["completed"]:
        uid = t["userId"]
        done_per_user[uid] = done_per_user.get(uid, 0) + 1

print(done_per_user)