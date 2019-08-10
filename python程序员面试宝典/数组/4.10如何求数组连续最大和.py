'''
题目描述：求数组连续最大和
输入样例
[1,-2,4,8,-4,7,-1,-5]
输出
15(最大连续和对应的子数组为[4,8,-4,7])

方法一：蛮力法,O(N**3)
方法二：在方法一基础上，计算子数组和时，保留之前的结果，即利用arr[i:j] = arr[i:j-1] + arr[j-1],(N**2)
方法三：动态规划法
step1:假设已经得到n-1规模的最优解，最优解对应的子数组是n-1个元素内任意的连续子数组。从n-1规模到n规模的递进，
实际上是引入了一种新的待考察情况：包含第n个元素的最大子数组和，因此n规模问题的最优解即为
max{n-1规模最优解，包含第n个元素的最大子数组和}
step2:假设已经得到包含第n-1个元素的最大子数组和pre，则包含第n个元素的最大子数组和为
max{第n个元素+以第n-1个元素结尾的最大连续子数组和，第n个元素}

'''
#方法一实现
def maxSubArray(arr):
	if arr is None or arr == []:
		return 
	import sys
	Max = -sys.maxsize - 1
	for i in range(len(arr)):
		for j in range(i,len(arr)):
			Sum = 0
			for k in range(i,j+1):
				Sum += arr[k]
				if Sum > Max:
					Min_index = i
					Max_index = k
					Max = max(Max,Sum)
	return Max,Min_index,Max_index

#方法二实现
def maxSubArray2(arr):
	if arr is None or arr == []:
		return 
	import sys
	Max = -sys.maxsize - 1
	Sum = 0
	for i in range(len(arr)):
		for j in range(i,len(arr)):
			Sum += arr[j]
			if Sum > Max:
				Min_index = i
				Max_index = j
				Max = max(Max,Sum)
		Sum = 0
	return Max,Min_index,Max_index
	
#方法三动态规划实现
def maxSubArray3(arr):
	if arr is None or len(arr) < 1:
		return
	if len(arr) == 1:
		return arr[0]
	#包含末尾元素的最大子数组和
	End = arr[0]
	#问题规模为1的问题最优解
	All = arr[0]
	for i in range(1,len(arr)):
		End = max(End+arr[i],arr[i])
		All = max(All,End)
	return All

#引申：求得数组最大连续和的同时，返回最大子数组的上下标
def maxSubArray4(arr):
	if arr is None or len(arr) < 1:
		return
	if len(arr) == 1:
		return arr[0],0,0
	#包含末尾元素的最大子数组和
	End = arr[0]
	#问题规模为1的问题最优解
	All = arr[0]
	#初始化最大子数组上下标	
	left = 0
	right = 0
	for i in range(1,len(arr)):
		End = max(End+arr[i],arr[i])
		All = max(All,End)
		if All == End:
			if End == arr[i]:
				left = right = i
			else:
				right = i
	return All,left,right	


if __name__ == '__main__':
	#arr = [1,-2,4,8,-4,7,-1,-5]
	#arr = [6,-5,3]
	arr = [1,2,3,-4,1]
	print(maxSubArray(arr))
	print(maxSubArray2(arr))
	print(maxSubArray3(arr))
	print(maxSubArray4(arr))
