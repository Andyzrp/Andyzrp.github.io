number_list = [0, 1, 2, 3, 4, 5, 6, 7]


def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index
    return -1


print(linear_search(5, number_list))
