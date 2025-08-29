# PATH = "/Users/mohammadi/Downloads/BOOTCAMP/projects/CW/text.txt"
import os
os.system("clear")

# replacements = {
#     "nigga": "white ppl",
#     "killing": "hugging",
#     "blood": "water",
#     "hate": "love",
#     "indians": "not scammer ppl"
# }

# class FileFilter:
#     def __init__(self, filename, replacements):
#         self.filename = filename
#         self.replacements = replacements
#         self.old_text = "" 
#         self.new_text = ""
    
#     def __enter__(self):
#         with open(self.filename, "r") as f:
#             self.old_text = f.read()  

#         self.new_text = self.old_text
#         for old, new in self.replacements.items():
#             self.new_text = self.new_text.replace(old, new)  
        
#         return self.new_text

#     def __exit__(self, exc_type, exc_value, traceback):
#         with open(self.filename, "w") as f:
#             f.write(self.new_text)
#         print("DONE")


# with FileFilter(PATH, replacements) as f:
#     print(f)

# --------------------------------------------------
import time

class Timer:
    def __init__(self, unit="seconds"):
        self.unit = unit
        self.start = ""
    
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        final_time = end - self.start
        print(f"This code executed in {final_time}s")
    

with Timer("seconds"):
    li = []
    for i in range(1000):
        for j in range(1000):
            li.append((i, j))


with Timer("seconds"):
    li = [(i, j) for i in range(1000) for j in range(1000)]