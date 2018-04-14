
def quicksort(arr):
    if len(arr) < 2:
        return arr  # 此为基线条件
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]  # 小于基准值的数组
        greater = [i for i in arr[1:] if i > pivot]  # 大于基准值的数组
        return quicksort(less)+[pivot]+quicksort(greater)


print(quicksort([3, 1, 2, 5, 4, 6]))
