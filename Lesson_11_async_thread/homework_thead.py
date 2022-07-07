from threading import Thread

lst = []


def make_list():
    global lst
    lst = list(range(1, 100000001))
    return lst


# print(make_list())


def sum_list(lst: list):
    result = sum(map(int, lst))
    print(result)


def sredn_arifm(lst: list):
    result = sum(lst) / len(lst)
    print(result)


def main():
    trd1 = Thread(target=make_list)
    trd1.start()
    trd1.join()
    # print(lst)
    trd2 = Thread(target=sum_list(make_list()))
    trd3 = Thread(target=sredn_arifm(make_list()))

    if trd1.is_alive() is False:
        trd2.start()
        trd3.start()
        # trd2.join()
        # trd3.join()
    # a = sum_list(make_list())
    # b = sredn_arifm(make_list())


if __name__ == "__main__":
    main()
