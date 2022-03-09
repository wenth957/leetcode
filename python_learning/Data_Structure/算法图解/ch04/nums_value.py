def nums_value(arr):
    if arr == []:
        return 0
    return 1 + nums_value(arr[1:])


print(nums_value([1, 2, 3, 4, 5]))
