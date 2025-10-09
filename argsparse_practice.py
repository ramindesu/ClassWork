
import argparse
# # import requests
# # import json

# # url = 'https://jsonplaceholder.typicode.com/posts'
# # response = requests.get(url)
# # all_posts = response.json()
# # required = []
# # for post in all_posts:
# #     required.append({
# #         "user_id" : post["userId"],
# #         "id": post["id"],
# #         "title": post["title"],
# #         "body": post["body"][:50]
# #     })

# # with open("required.json","w") as f:
# #     json.dump(required,f,indent=4)
    
# # # # part b 
# # import argparse
# # import requests
# # import json
# # from pprint import pprint
# # url = 'https://jsonplaceholder.typicode.com/posts'
# # response = requests.get(url)
# # all_posts = response.json()

# # parser = argparse.ArgumentParser()
# # parser.add_argument("-p", "--user", type=int, help="Filter by userId")
# # parser.add_argument("-f", "--format", default="json", help="Output format (only json supported)")
# # args = parser.parse_args()

# # posts = all_posts
# # if args.user:
# #     posts = [post for post in all_posts if post["userId"] == args.user]


# # parsed_posts = [
# #     {"userId": p["userId"], "id": p["id"], "title": p["title"], "body": p["body"][:50]}
# #     for p in posts
# # ]


# # with open("output.json", "w") as f:
# #     json.dump(parsed_posts, f, indent=4)

# # print("Data saved successfully to output.json")

# # # PART c 

# import requests
# from pprint import pprint

# class PostFetcher:
#     def __init__(self, api="https://jsonplaceholder.typicode.com/posts"):
#         self.__api = api

#     @property
#     def posts(self):
#         response = requests.get(self.__api)
#         posts = response.json()
#         return posts

#     def fetch_posts(self):
#         required = []
#         for post in self.posts:
#             required.append({
#                 "user_id": post["userId"],
#                 "id": post["id"],
#                 "title": post["title"],
#                 "body": post["body"][:50]
#             })
#         pprint(required)  

#     def filter_posts(self, userId):
#         filtered = [post for post in self.posts if post["userId"] == userId]
#         pprint(filtered) 
    
# fetcher = PostFetcher()

# print("all post :")
# fetcher.fetch_posts()

# print("only 3")
# fetcher.filter_posts(3)
# ------------------------------------------------------------------------------------------------------------------------------------
# question number 1
# parser = argparse.ArgumentParser()
# parser.add_argument('numbers' , type=float, nargs="+" , help="u have to insert couple of  bro")
# args = parser.parse_args()

# if not args.numbers:
#     print('there is no number sir')

# number = args.numbers
# total = sum(number)
# avg = total / len(number)
# maximum = max(number)

# print(f"Numbers: {number}")
# print(f"Sum: {total}")
# print(f"Average: {avg}")
# print(f"Max: {maximum}")
# ------------------------------------------------------------------------------------------------------------------------------------