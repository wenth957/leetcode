def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        more = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)


print(quick_sort([1, 20, 9, 188, 100]))
