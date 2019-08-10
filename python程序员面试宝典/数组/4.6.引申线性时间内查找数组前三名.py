'''
题目描述：
在数组中找出前k大的数
'''
def findTop3(arr):
	if arr is None or len(arr) < 3:
		return
	import sys
	r1 = r2 = r3 = -sys.maxsize-1
	for i in range(len(arr)):
		if arr[i] > r1:
			r3 = r2
			r2 = r1
			r1 = arr[i]
		elif arr[i] > r2 and arr[i] != r1:
			r3 = r2
			r2 = arr[i]
		elif arr[i] > r3 and arr[i] != r2:
			r3 = arr[i]
	return r1,r2,r3

if __name__ == '__main__':
	print(findTop3([9,8,7,6,5,4,3,2,1]))
