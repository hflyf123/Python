'''def sum(arr):
	total=0
	for x in arr:
		total=total+x
	return total
print(sum([1,2,3,4,5]))
'''


def supersum(arr):
    if arr == []:
        return 0
    return arr[0] + supersum(arr[1:])


print(supersum([1, 2, 3, 4, 5]))
