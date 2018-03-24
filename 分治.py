'''def sum(arr):
	total=0
	for x in arr:
		total=total+x
	return total
print(sum([1,2,3,4,5]))
'''


def sumpro(list):
    if list == []:
        return 0
    return list[0] + sumpro(list[1:])


print(sumpro([1, 2, 3]))
