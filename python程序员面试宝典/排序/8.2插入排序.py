def Insert_sort(arr):
	if arr is None or arr == []:
		return
	for i in range(1,len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0:
			if arr[j] > key:
				arr[j],arr[j+1] = arr[j+1],arr[j]
			j -= 1
	return arr		



if __name__ == '__main__':
	arr = [2,3,4,5,4]	
	print(arr)
	print()
	print(Insert_sort(arr))
	print('=====')
	arr = [5,4,3,2,1,7,8,9,45,32]
	print(arr)
	print()
	print(Insert_sort(arr))
