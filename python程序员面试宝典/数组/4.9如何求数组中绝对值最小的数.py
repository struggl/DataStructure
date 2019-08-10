'''
题目描述：有一个升序的数组，数组中可能有正数、负数、0，求数组中元素的绝对值最小的数。
输入样例：
[-10,-5,-2,7,15,50]
输出：
2

方法一：顺序遍历法,O(N)
方法二：二分法,O(log2N)
(1)如果数组全为正数(只需arr[0] > 0)，则arr[0]即所求
(2)如果数组全为负数(只需arr[-1] < 0)，则arr[-1]即所求
(3)数组有正有负(也可能有0),则需要比较正负交界两个正负元素的绝对值
取中点mid = start + (end-start)//2 
a.若arr[mid] == 0,则arr[mid]即为所求
b.若arr[mid] < 0
若arr[mid+1] == 0，返回arr[mid+1]
若arr[mid+1] < 0,start = mid+1,继续在右半边查找
此时arr[mid+1] > 0,则arr[mid]和arr[mid+1]即为正负交界元素
c.若arr[mid] > 0
若arr[mid-1] == 0,返回arr[mid-1]
若arr[mid-1] < 0,则arr[mid-1]和arr[mid]即为正负交界元素
此时arr[mid-1] > 0，end = mid - 1,继续在左半边查找
'''

#方法一实现
def findMin(arr):
	if arr is None or len(arr) < 1:
		return 
	if len(arr) == 1:
		return arr[0]
	Min = 0
	for i in range(1,len(arr)):
		if abs(arr[i]) < abs(arr[Min]):
			Min = i
	return arr[Min]

#方法二实现
'''
(1)如果数组全为正数(只需arr[0] > 0)，则arr[0]即所求
(2)如果数组全为负数(只需arr[-1] < 0)，则arr[-1]即所求
(3)数组有正有负(也可能有0),则需要比较正负交界两个正负元素的绝对值
取中点mid = start + (end-start)//2 
a.若arr[mid] == 0,则arr[mid]即为所求
b.若arr[mid] < 0
若arr[mid+1] == 0，返回arr[mid+1]
若arr[mid+1] < 0,start = mid+1,继续在右半边查找
此时arr[mid+1] > 0,则arr[mid]和arr[mid+1]即为正负交界元素
c.若arr[mid] > 0
若arr[mid-1] == 0,返回arr[mid-1]
若arr[mid-1] < 0,则arr[mid-1]和arr[mid]即为正负交界元素
此时arr[mid-1] > 0，end = mid - 1,继续在左半边查找

实现细节，考虑mid-1和mid+1会不会数组越界。越界的情况就是数组分割到只剩下两个，例如为[1,2]，此时
mid为第2个元素，此时会用到mid-1，并不越界。假设分割到只剩下[-2,-1]，则会考虑mid+1，越界。
但是事实上不会分割到只剩下[-2,-1]]这种情形，
考虑[-2,-1(mid),1,2],此时使用mid+1，由于mid+1对应正数，已经找到了正负边界
考虑[-2,-1(mid),0,2],mid+1对应元素0，直接返回
考虑[-2,-1(mid),-0.5,1],此时会在右半边继续搜索，而对于[-0.5,1]，会找到正负边界
综上，循环入口设置为while True即可
'''
def findMin2(arr):
	if arr is None or len(arr) < 1:
		return
	if len(arr) == 1:
		return arr[0]
	if arr[0] > 0:
		return arr[0]
	if arr[-1] < 0:
		return arr[-1]
	start = 0
	end = len(arr) - 1
	while True:
		mid = start + (end-start)//2
		#a.若arr[mid] == 0,则arr[mid]即为所求
		if arr[mid] == 0:
			return arr[mid]
		#b.若arr[mid] < 0
		#若arr[mid+1] == 0，返回arr[mid+1]
		#若arr[mid+1] < 0,start = mid+1,继续在右半边查找
		#此时arr[mid+1] > 0,则arr[mid]和arr[mid+1]即为正负交界元素
		if arr[mid] < 0:
			if arr[mid+1] == 0:
				return arr[mid+1]
			if arr[mid+1] < 0:
				start = mid+1
			else:
				if abs(arr[mid]) < arr[mid+1]:
					return arr[mid]
				else:
					return arr[mid+1]
		#c.若arr[mid] > 0
		#若arr[mid-1] == 0,返回arr[mid-1]
		#若arr[mid-1] < 0,则arr[mid-1]和arr[mid]即为正负交界元素
		#此时arr[mid-1] > 0，end = mid - 1,继续在左半边查找
		else:
			if arr[mid-1] == 0:
				return arr[mid-1]
			if arr[mid-1] < 0:
				if abs(arr[mid-1]) < arr[mid]:
					return arr[mid-1]
				else:
					return arr[mid]
			end = mid - 1
	

if __name__ == '__main__':
	arr = [-10,-5,-2,7,15,50]
	print(findMin(arr))
	print(findMin2(arr))
