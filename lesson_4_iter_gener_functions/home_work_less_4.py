FILENAME = "rockyou.txt"


def read_lines_count() -> int:
    with open(FILENAME, encoding="utf-8") as file:
        lines = file.readlines()
        return len(lines)


print("Lines: ", read_lines_count())