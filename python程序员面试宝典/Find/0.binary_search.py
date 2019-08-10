#给定从小到大排好序的数组，从中查找一个值在数组中的位置，找不到则返回-1
#递归写法
def binary_search(arr,start,end,key):
	#参数边界处理
	if start > end:
		return -1
	mid = start + (end - start) // 2
	if arr[mid] < key:
		return binary_search(arr,mid+1,end,key)
	if arr[mid] > key:
		return binary_search(arr,start,end-1,key)
	#递归终止返回
	return mid
'''
#循环写法
def binary_search(arr,start,end,key):
	#参数边界处理
	if start > end:
		return -1
	while start <= end:
		mid = start + (end - start) // 2
		if key == arr[mid]:
			return mid
		elif key < arr[mid]:
			end = mid -1
		else:
			start = mid + 1
	return -1 
'''
if __name__ == '__main__':
	arr = [1,2,3,4,5,6]
	key = 5
	print('Testing:'+str(arr)+',key = {}'.format(key))
	print(binary_search(arr,0,len(arr)-1,key))
	arr = [1,2,3,4,5,6]
	key = 59
	print('Testing:'+str(arr)+',key = {}'.format(key))
	print(binary_search(arr,0,len(arr)-1,key))
	arr = [1]
	key = 1
	print('Testing:'+str(arr)+',key = {}'.format(key))
	print(binary_search(arr,0,len(arr)-1,key))
	arr = [1]
	key = 59
	print('Testing:'+str(arr)+',key = {}'.format(key))
	print(binary_search(arr,0,len(arr)-1,key))
