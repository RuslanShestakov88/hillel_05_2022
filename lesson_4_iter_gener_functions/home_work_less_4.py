from tkinter import Spinbox
from typing import Generator
FILENAME = "rockyou.txt"
SEARCH_KEYWORD = "user123"

def read_lines_find_admin_generator() -> Generator:
    
    with open(FILENAME, encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if SEARCH_KEYWORD in line:
                yield line.replace("\n", "")
                continue

question = input ("dobavlyat?")
spisok = []
for line in read_lines_find_admin_generator():
    print(line)
    if question == ("y"):
        spisok.append(line)
###