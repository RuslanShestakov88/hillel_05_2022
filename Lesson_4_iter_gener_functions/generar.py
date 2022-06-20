import sys
from random import choice
from string import ascii_letters


def get_random_string(n: int) -> str:
    return "".join((choice(ascii_letters) for _ in range(n)))


data = [get_random_string(100) for _ in range(10_000)]
enum_data = enumerate(data)

new_data = tuple(data)

dict_from_enum = {k: v for k, v in enum_data}

# print(len(data))
print("List size", sys.getsizeof(data), sep=" ")
print("Enum data", sys.getsizeof(enum_data), sep=" ")
print("Dict from enum data", sys.getsizeof(dict_from_enum), sep=" ")
print("Tuple", sys.getsizeof(new_data), sep=" ")
