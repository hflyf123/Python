def search(arr, x):
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


def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionsort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findsmallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr


<<<<<<< HEAD
print(search(selectionsort([3, 1, 2, 4]), 5))
=======
print(search(selectionsort([3,1,2,3,5,6,7]), 3))
>>>>>>> 5a7fb33efe1b66a47375933bc23a4f7214dfb043
