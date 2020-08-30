def binary_search(sorted_array, val):
    if not sorted_array:
        return -1

    beg = 0
    end = len(sorted_array) - 1

    while beg <= end:
        mid = int((beg + end) / 2)
        if sorted_array[mid] == val:
            return mid
        elif sorted_array[mid] > val:
            end = mid - 1
        else:
            beg = mid + 1
    return -1


a = list(range(10))

# 正常值
print(binary_search(a, 1))
print(binary_search(a, -1))

# 边界值
print(binary_search(a, 0))
