class Writer:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


class Story:
    def __init__(self, title, pages, content, author: Writer, checked=False):
        self.title = title
        self.pages = pages
        self.author = author
        self.content = content
        self.checked = checked  


class FileManager:
    def __init__(self, filename, mode="w"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


class StoryManager:
    def __init__(self, filename="stories.txt"):
        self.stories = []
        self.filename = filename  

    def add_story(self, story: Story):
        self.stories.append(story)

    def save_stories(self):

        with FileManager(self.filename, "w") as f:
            for story in self.stories:
                f.write(f"{story.title}\n")
                f.write(f"By: {story.author.name}\n")
                f.write(f"Content: {story.content}\n")
                f.write("-" * 40 + "\n")

    def check_stories(self):

        for story in self.stories:
            story.checked = True


        bad_words = ["bad", "ugly", "stupid"]
        filtered_lines = []

        with FileManager(self.filename, "r") as f:
            lines = f.readlines()

        for line in lines:
            for bad in bad_words:
                if bad in line:
                    line = line.replace(bad, "***")
            filtered_lines.append(line)


        with FileManager("stories_filtered.txt", "w") as f:
            f.writelines(filtered_lines)

        return filtered_lines

    def return_checked_ones(self):
        return [s.content for s in self.stories if s.checked]




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