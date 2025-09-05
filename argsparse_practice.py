
# import argparse
# import requests
# import json

# url = 'https://jsonplaceholder.typicode.com/posts'
# response = requests.get(url)
# all_posts = response.json()
# required = []
# for post in all_posts:
#     required.append({
#         "user_id" : post["userId"],
#         "id": post["id"],
#         "title": post["title"],
#         "body": post["body"][:50]
#     })

# with open("required.json","w") as f:
#     json.dump(required,f,indent=4)
    
# # part b 
# import argparse
# import requests
# import json

# url = 'https://jsonplaceholder.typicode.com/posts'
# response = requests.get(url)
# all_posts = response.json()


# parser = argparse.ArgumentParser()
# parser.add_argument("-p", "--user", type=int, help="Filter by userId")
# parser.add_argument("-f", "--format", default="json", help="Output format (only json supported)")
# args = parser.parse_args()


# posts = all_posts
# if args.user:
#     posts = [post for post in all_posts if post["userId"] == args.user]


# parsed_posts = [
#     {"userId": p["userId"], "id": p["id"], "title": p["title"], "body": p["body"][:50]}
#     for p in posts
# ]


# with open("output.json", "w") as f:
#     json.dump(parsed_posts, f, indent=4)

# print("Data saved successfully to output.json")

