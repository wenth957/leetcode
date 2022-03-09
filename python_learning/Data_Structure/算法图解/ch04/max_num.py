def max_num(arr):
    if arr == []:
        return None
    if len(arr) == 1:
        return arr[0]
    num = max_num(arr[1:])  # 一直传入少一位
    if arr[0] > num:     # 第一个元素和后面的最大值比较
        return arr[0]
    else:
        return num


print(max_num([1, 2, 3, 7, 55, 8]))
print(max_num([]))
