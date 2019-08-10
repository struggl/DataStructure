'''
方法思路：
1.非就地
2.就地
'''
#方法一实现
def rotate(arr,idx):
	if arr is None or len(arr) <= 1:
		return
	if type(idx) != int or idx < 0  or idx > len(arr) - 1:
		return
	if idx == 0 or idx == len(arr)-1:
		return arr
	return arr[idx+1:] + arr[:idx+1]

#方法二实现
def inplace_rotate(arr,idx):
	if arr is None or len(arr) <= 1:
		return
	if type(idx) != int or idx < 0  or idx > len(arr) - 1:
		return
	if idx == 0 or idx == len(arr)-1:
		return arr
	swap(arr,0,idx)
	swap(arr,idx+1,len(arr)-1)
	swap(arr,0,len(arr)-1)

def swap(arr,low,high):
	if low == high:
		return
	mid = low + ((high - low) >> 1)
	while low < high:
		arr[low],arr[high] = arr[high],arr[low]
		low += 1
		high -= 1	

if __name__ == '__main__':
	arr = [1,2,3,4,5,6,7,8,9]
	idx = 2
	print('testing: arr = '+str(arr)+' idx = '+str(idx))
	print(rotate(arr,idx))
	print('=====')	
	
	#arr = [1,2,3,4,5,6,7,8,9]
	arr = [1,2,3,4]
	idx = 2
	print('testing: arr = '+str(arr)+' idx = '+str(idx))
	inplace_rotate(arr,idx)
	print(arr)
	
