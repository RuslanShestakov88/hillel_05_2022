FILENAME = "rockyou.txt"
SEARCH_KEYWORD = "user1234"


def read_lines_find_admin_generator() -> list:
    results = []
    with open(FILENAME, encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if SEARCH_KEYWORD in line:
                user_input = input("Sohranyat? {line}")
                if user_input == "y":
                    results.append(line.replace("\n", ""))
        return results


results: list = read_lines_find_admin_generator()
print(results)
