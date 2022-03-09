def sum_arr(arr):
    if arr == []:
        return 0
    else:
        first = arr.pop(0)
        return first + sum(arr)


print(sum_arr([1, 2, 3, 4, 5, 6, 7, 8, 9]))
