def reverse(func):
    def wrapper(x):
        if isinstance(x, str):
            result = x[::-1]
        else:
            result = None
        return result

    return wrapper


@reverse
def primer(x):
    return x


print(primer("3ffff2"))
print(primer(444))
