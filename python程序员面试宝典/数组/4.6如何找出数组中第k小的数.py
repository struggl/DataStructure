'''
题目描述：
给定一个整数数组，如何快速地求出该数组中第k小的数。
输入样例：
arr=[4,0,1,0,2,3] k=3
输出：
1

方法一：排序法。先将数组排序，然后返回下标为[k-1]的元素,O(Nlog2(N))
方法二：部分排序法。改写选择排序，外层循环跑k次，每次都找到右边数组中的最小值。O(k*n)
方法三：类快速排序法。
随机选出当前数组中一个元素，记录其下标为i
若i-low == k-1,则arr[i]即为第k小的数
若i-low > k-1，则递归地在arr[:i]中查找第k小的数
若i-low < k-1,则递归地在arr[i+1:]中找第(k-1)-(i-low)小的数
'''
#方法一实现
def findSmallK(arr,k):
	if arr is None:
		return
	if type(k) != int or len(arr) < k or k <= 0:
		return
	arr = quick_sort(arr)
	return arr[k-1]

def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	L = []
	E = []
	G = []
	import random
	key = random.choice(arr)
	for v in arr:
		if v < key:
			L.append(v)
		elif v == key:
			E.append(v)
		else:
			G.append(v)
	return quick_sort(L) + E + quick_sort(G)

#方法二实现
def findSmallK2(arr,k):
	if arr is None:
		return
	if type(k) != int or len(arr) < k or k<= 0:
		return
	for i in range(k):
		Min = i
		for j in range(i,len(arr)):
			if arr[j] < arr[Min]:
				Min = j
		arr[i],arr[Min] = arr[Min],arr[i]
	return arr[i]

#方法三类快速排序实现
def findSmallK3(arr,k,low,high):
	if arr is None:
		return
	if type(k) != int or len(arr) < k or k<= 0:
		return
	L = []
	E = []
	G = []
	import random
	i = random.choice(range(low,high+1))
	key = arr[i]
	for j in range(len(arr)):
		if j == i:
			continue
		if arr[j] <= key:
			L.append(arr[j])
		else:
			G.append(arr[j])
	if i-low == k-1:
		return arr[i]
	if i-low > k-1: 
		return findSmallK3(L,k,0,i-1)
	print('-')
	return findSmallK3(arr,(k-1)-(i-low),i+1,len(arr)-1) 

if __name__ == '__main__':
	arr = [4,0,1,0,2,3]
	k = 4
	print(findSmallK3(arr,k,0,len(arr)-1))	
