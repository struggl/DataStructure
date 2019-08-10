'''
题目描述:给定一个含有重复元素的数组，给定两个数字，求这两个数字在数组中出现的位置的最小距离

方法一：蛮力法。两层循环，外层循环遍历找到num1，每次找到num1，就从头到尾遍历一次数组，找到每个num2，计算最小距离
方法二：动态规划法。一次遍历，记录最近出现的num1和num2位置，计算最小距离
'''
#方法二实现
def minDist(arr,num1,num2):
	if arr is None or num1 is None or num2 is None:
		return
	p1,p2 = None,None
	import sys
	minDist = sys.maxsize
	for i in range(len(arr)):
		if arr[i] == num1:
			p1 = i
			if p2:
				minDist = min(minDist,abs(p1-p2))
		elif arr[i] == num2:
			p2 = i
			if p1:
				minDist = min(minDist,abs(p1-p2))
	return minDist

if __name__ == '__main__':
	arr = [4,5,6,4,7,4,6,4,7,8,5,6,4,3,10,8]
	num1 = 4
	num2 = 8
	print(minDist(arr,num1,num2))
				
