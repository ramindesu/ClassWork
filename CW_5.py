# # question number 1
# # sentences = ["I love Python", "Lambda functions are powerful", "Map is veryuseful"]
# # counting = list(map(lambda x: len(x.split()),sentences))
# # print(counting)



# # question number 2


# # nested_list = [["apple" ,"banana" ,"apple"],["orange" ,"banana"],["grpae","apple","grape"]]
# # def same_detect(data):
# #     fruit_set = set()
# #     def extend(sub_data):
# #         for item in sub_data:
# #             if isinstance(item, list):
# #                 extend(item)
# #             else:
# #                 fruit_set.add(item)
# #     extend(data)
# #     return fruit_set

# # print(f"fruites : {same_detect(nested_list)}")


# # question number 3
# # files = ["image1.jpg", "doc1.pdf", "photo.png", "notes.txt", "data.csv"]
# # get_ext = lambda filename: filename.split(".")[-1]
# # image_ext = ["jpg", "png"]
# # text_ext = ["pdf", "txt"]
# # images = [f for f in files if get_ext(f) in image_ext]
# # texts = [f for f in files if get_ext(f) in text_ext]
# # others = [f for f in files if get_ext(f) not in image_ext + text_ext]
# # result = {"images": images, "texts": texts, "others": others}
# # print(result)


# # question number 4
# # accounts = {
# #  "Ali": {"balance": 1000, "transactions": [200, -100, 50]},
# #  "Sara": {"balance": 1500, "transactions": [-200, 300, -50]},
# # }
# # def apply_transactions(transactions):
# #     if not transactions:
# #         return 0
# #     return transactions[0] + apply_transactions(transactions[1:])



# # final_balances = {name: data["balance"] + apply_transactions(data["transactions"])
# #                   for name, data in accounts.items()}

# # print(final_balances)











# # def accounting(hessab):
# #     balance = dict()
# #     def extend(sub_hessab):
# #         if isinstance(sub_hessab,dict):
# #             for key,values in sub_hessab.items():
# #                 pool = values.get("balance",-1)
# #                 amaliat = values.get("transactions",[-1])
# #                 baqi_mande = pool + sum(amaliat)
# #                 balance[key] = baqi_mande
# #     extend(hessab)
# #     return balance

# # print(accounting(accounts))


# # question number 5
# moves = ["up", "up", "left", "down", "right","up","up","up","left","left","left","right"]
# def snake_game(moves):
#     x= 0 
#     y= 0
#     yield (x, y) 
#     for i in moves:
#         if i == "up":
#             y += 1
#         elif i == "down":
#             y -= 1
#         elif i == "left":
#             x -= 1
#         elif i == "right":
#             x += 1
#         yield (x, y)
# for i in snake_game(moves):
#     print(i)



         
