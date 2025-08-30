class Writer:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

class Story:
    def __init__(self,Title,pages,content,author:Writer,cheacked = False):
        self.title = Title
        self.pages = pages
        self.author = author
        self.content = content
        self.cheackef = cheacked

class FileManager:

    def __init__(self, filename, mode="w"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

class StoryManager:
    def __init__(self):
        self.stories = []
    
    def add_story(self,story:Story):
        self.stories.append(story)

    def save_stories(self):
        # Save all stories' content into a file
        with FileManager(self.filename, "w") as f:
            for story in self.stories:
                f.write(f"{story.title}\n")
                f.write(f"By: {story.author.name}\n")
                f.write(f"Content: {story.content}\n")
                f.write("-" * 40 + "\n")

    def cheack_stories(self):
        # Mark stories as checked
        for story in self.stories:
            story.checked = True

        # Read from file and filter bad words
        bad_words = ["bad", "ugly", "stupid"]
        filtered_lines = []

        with FileManager(self.filename, "r") as f:
            lines = f.readlines()

        for line in lines:
            for bad in bad_words:
                if bad in line:
                    line = line.replace(bad, "***")
            filtered_lines.append(line)

        # Save the cleaned version
        with FileManager("stories_filtered.txt", "w") as f:
            f.writelines(filtered_lines)

        return filtered_lines

    def return_cheacl_ones(self):
        return [s.content for s in self.stories if s.checked]