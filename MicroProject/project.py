class FavItems:
    def __init__(self, name, item_id):
        self.name = name
        self.item_id = item_id



    def __repr__(self):
        return f"name : {self.name} id: {self.item_id}"


class User:
    def __init__(self, name):
        self.name = name
        self.item = set()

    def add_item(self, item):
        self.item.add(item)

    def show_items(self):
        return list(self.item)


class Website:
    def __init__(self):
        self.user = []

    def add_user(self, user):
        if user not in self.user:
            self.user.append(user)
            return "user added"
        return "its already in the list"

    def user_fav_item(self, user):
        for ppl in self.user:
            if ppl.name == user:
                return ppl.show_items()

    def all_fav_items(self):
        all_items = []
        for user in self.user:
            all_items.extend(user.item)
        return all_items

    def most_popular(self):
        items = self.all_fav_items()
        max_count = 0
        popular_item = None
        for item in items:
            count = items.count(item)
            if count > max_count:
                max_count = count
                popular_item = item
        if popular_item:
            return popular_item.name, max_count
        


site = Website()
ramin = User("ramin")
sara = User("sara")
item1 = FavItems("Laptop", 1)
item2 = FavItems("Phone", 2)
item3 = FavItems("Tablet", 3)
ramin.add_item(item1)
ramin.add_item(item2)
sara.add_item(item2)
sara.add_item(item3)
print(site.add_user(ramin))
print(site.add_user(sara))
print(site.user_fav_item("ramin"))
print(site.all_fav_items())
print(site.most_popular())