from tkinter import Spinbox
from typing import Generator
from unittest import result
FILENAME = "rockyou.txt"
SEARCH_KEYWORD = "user123"

results = []
def read_lines_find_admin_generator() -> Generator:
    
    with open(FILENAME, encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if SEARCH_KEYWORD in line:
                yield line.replace("\n", "")
                results.append(line)
                continue
        return results



#for line in read_lines_find_admin_generator():
#    print(line)
