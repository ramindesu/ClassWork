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
# question number 2
# parser = argparse.ArgumentParser()
# parser.add_argument('text', type=str,help='some text')
# parser.add_argument('--verbose' , action="store_true" , help='shows details')

# args = parser.parse_args()

# if args.verbose:
#     print(args.text)
#     print(len(args.text))
#     print(args.text.upper())
#     print(args.text.lower())
# else:
#     print(args.text)
# ------------------------------------------------------------------------------------------------------------------------------------
# question number 3

# parser = argparse.ArgumentParser()
# parser.add_argument("--x", type=float, required=True, help="first num")
# parser.add_argument("--y", type=float, required=True, help="secend num")
# parser.add_argument("--operation", type=str, required=True, choices=['add' , "subtract", "multiply", "divide"], help='the agriration')

# parser.add_argument(
#     "--verbose",
#     action="store_true",
#     help="Show detailed output"
# )

# args = parser.parse_args()
# if args.operation == "add":
#     result = args.x + args.y
# elif args.operation == "subtract":
#     result = args.x - args.y
# elif args.operation == "multiply":
#     result = args.x * args.y
# elif args.operation == "divide":
#     if args.y == 0:
#         print("Error: cannot divide by zero!")
#         exit()
#     result = args.x / args.y
# if args.verbose:
#     print(f"Operation: {args.operation}, x={args.x}, y={args.y}, result={result}")
# else:
#     print(result)
# ------------------------------------------------------------------------------------------------------------------------------------
# question 4
# import json
# parser = argparse.ArgumentParser()
# parser.add_argument('--config' , type=str , required=True,help='turns json to normal text')
# args = parser.parse_args()
# data = json.loads(args.config)
# for key , val in data.items() :
#     print(f'{key}:{val}')
