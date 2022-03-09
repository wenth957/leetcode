def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


result1 = binary_search(range(0, 100, 2), 70)
result2 = binary_search(range(1, 101, 2), 70)
print(result1)  # 35
print(result2)  # None
