from main import *
w1 = Writer("Ramin", 21, "ramin@example.com")
w2 = Writer("Ali", 25, "ali@example.com")

s1 = Story("My First Story", 3, "This is a good story but has a bad ending.", w1)
s2 = Story("Adventure Time", 5, "An ugly monster appeared but the hero was smart.", w2)

manager = StoryManager()
manager.add_story(s1)
manager.add_story(s2)

manager.save_stories()

print("=== Filtered Output ===")
filtered = manager.check_stories()  
for line in filtered:
    print(line, end="")

print("\n Checked Stories ")
print(manager.return_checked_ones())
