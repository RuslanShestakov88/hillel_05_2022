names = ["Dima", "Sasha", "Vanya", "Tanya"]

print("Out from for names")
for name in names:
    print(name)
print("\n")

data = iter(names)
print("Out iter names")
for d in data:
    print(d)
print("\n")

while True:
    try:
        print(data.__next__())
    except StopIteration:
        break
