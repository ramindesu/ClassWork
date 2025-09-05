import argparse
import requests
import json
# # Create the parser
# parser = argparse.ArgumentParser(description="This program is a simple argparse example")

# # Add arguments
# parser.add_argument("name", help="Enter your name")
# parser.add_argument("--age", type=int, help="Enter your age")

# # Parse the arguments
# args = parser.parse_args()

# print(f"Hello {args.name}!")
# if args.age:
#     print(f"Your age is: {args.age}")
# part A 
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
all_posts = response.json()
required = []
for post in all_posts:
    required.append({
        "user_id" : post["userId"],
        "id": post["id"],
        "title": post["title"],
        "body": post["body"][:50]
    })

with open("required.json","w") as f:
    json.dump(required,f,indent=4)
    
