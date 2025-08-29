PATH = "/Users/mohammadi/Downloads/BOOTCAMP/projects/CW/text.txt"

replacements = {
    "nigga": "white ppl",
    "killing": "hugging",
    "blood": "water",
    "hate": "love",
    "indians": "not scammer ppl"
}

class FileFilter:
    def __init__(self, filename, replacements):
        self.filename = filename
        self.replacements = replacements
        self.old_text = "" 
        self.new_text = ""
    
    def __enter__(self):
        with open(self.filename, "r") as f:
            self.old_text = f.read()  

        self.new_text = self.old_text
        for old, new in self.replacements.items():
            self.new_text = self.new_text.replace(old, new)  
        
        return self.new_text

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.filename, "w") as f:
            f.write(self.new_text)
        print("DONE")


with FileFilter(PATH, replacements) as f:
    print(f)