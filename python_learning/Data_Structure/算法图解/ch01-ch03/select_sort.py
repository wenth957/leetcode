def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def select_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))  # 每次删除最小元素
    return newArr


print(select_sort([3, 52, 65, 2, 99, 123, 242, 211]))
# 两次循环 平方次的时间复杂度
