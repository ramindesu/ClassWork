from context import *

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




class StoryManager:
    def __init__(self, filename="short-story/stories.txt"):
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




