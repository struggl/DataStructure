'''
题目描述：给定一个字符串数组，找出数组中最长的字符串，使其能由数组中其他的字符串组成。
输入样例：
['test','tester','testertest','testing','apple',
'seattle','banana','batting','ngcat','batti',
'bat','testingtester','testbattingcat','bat']
输出：
'testbattingcat'

方法思路：
首先将字符串按长度由大到小进行排序，逐个进行判断
对当前字符串，取每个前缀进行判断，若某前缀在字符串数组中出现，则递归地判断剩余部分能否在字符串数组中出现。
复杂度：O(nlogn+n*m*n),其中m为字符串数组元素的平均长度
'''
def getLongestStr(arr):
	if '' in arr:
		return 
	arr = sorted(arr,key=lambda a:len(a),reverse=True)
	print(arr)
	for i in range(len(arr)):
		Str = arr[i]
		if isContain(arr,Str,i):
			return Str
	return False

def isContain(arr,Str,pos):
	length = len(Str)	
	#子问题划分
	i = 1
	while i < length:
		if find(arr,Str[:i],pos) and isContain(arr,Str[i:],pos):
			return True
		i += 1
	if find(arr,Str,pos):
		return True
	return False

def find(arr,Str,pos):
	for i in range(len(arr)):
		if i <= pos:
			continue
		if arr[i] == Str:
			return True
	return False	

if __name__ == '__main__':
	arr = ['test','tester','testertest','testing','apple',
		'seattle','banana','batting','ngcat','batti',
		'bat','testingtester','testbattingcati','bat']
	print(getLongestStr(arr))
