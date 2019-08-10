def Select_sort(arr):
	if arr is None or arr == []:
		return
	for i in range(len(arr)):
		Min = i
		for j in range(i+1,len(arr)):
			if arr[j] < arr[Min]:
				Min = j
		if Min != i:
			arr[Min],arr[i] = arr[i],arr[Min]
	return arr

if __name__ == '__main__':
	arr = [5,4,3,2,1,7,8,9,45,32]
	print(arr)
	print()
	print(Select_sort(arr))

