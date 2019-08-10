def Merge_sort(arr):
	if arr is None or arr == []:
		return
	#递归终止返回
	if len(arr) == 1:
		return arr
	n = len(arr) >> 1
	left = Merge_sort(arr[:n])
	right = Merge_sort(arr[n:])
	return merge(left,right)

def merge(left,right):
	i = 0
	j = 0
	res = []
	while i < len(left) and j < len(right):			
		if left[i] <= right[j]:
			res.append(left[i])
			i += 1
		else:
			res.append(right[j])
			j += 1
	res += left[i:]
	res += right[j:]
	return res

if __name__ == '__main__':
	arr = [2,3,4,5,4]	
	print(arr)
	print()
	print(Merge_sort(arr))
	print('=====')
	arr = [5,4,3,2,1,7,8,9,45,32]
	print(arr)
	print()
	print(Merge_sort(arr))
