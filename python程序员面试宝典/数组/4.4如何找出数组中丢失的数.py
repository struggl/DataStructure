'''
题目描述：
给定一个由n-1个整数组成的未排序的数组序列，其元素都是1到n中不同整数。
请写出一个寻找数组序列中缺失整数值的线性时间算法。

方法一：累加求和法。累加1到n，减去数组之和
方法二：异或法。异或1到n，然后异或数组所有元素，所得结果即为所求
'''
#方法一实现
def getNum(arr):
	if arr is None or arr == []:
		return
	Sum = 0
	for i in range(len(arr)+2):
		Sum += i
	arrSum = sum(arr)
	return Sum - arrSum

#方法二实现
def getNum2(arr):
	if arr is None or arr == []:
		return
	res = 0
	for i in range(len(arr)+2):
		res ^= i
	for v in arr:
		res ^= v
	return res

if __name__ == '__main__':
	arr = [1,2,4,5,3,7]
	print(getNum2(arr))
	
