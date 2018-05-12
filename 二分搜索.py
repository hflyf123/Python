# Link:https://github.com/hflyf123
# @Author: LYF
# @Date: 2018-04-23 21:49:34
# @Last Modified by:   LYF
# @Last Modified time: 2018-04-23 21:49:34


def binarysearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        else:
            return None


print(binarySearch([1, 2, 3], 3))
print(binarySearch([1, 2, 3], 4))
