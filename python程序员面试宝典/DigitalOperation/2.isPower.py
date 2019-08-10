#判断一个数字n是否能表达成2的m次方
#法一:左移位法。从1开始，每次左移一位，分别得到2的0,1,2，...,m次方。假设移动m次后等于n，则n = 2的m次方，即m=log(n)
#故时间复杂度为O(log(n))
#法二:与操作法。每个能表示为2的m次方的整数n，其二进制表示必然仅含有一个1，而n-1与n每个二进制位都不同，因此可以根据与操作来判断
#时间复杂度为O(1)
'''
#左移位法
def isPower(n):
	#参数边界处理
	if n <= 0:
		return False
	i = 1
	while i <= n:
		if i == n:
			return True
		i <<= 1
	return False
'''
#与操作法
def isPower(n):
	if n <= 0:
		return False
	m =  n & (n-1)
	return m == 0

if __name__ == '__main__':
	n = 16
	print('Testing:n = '+str(n))
	print(isPower(n))
	n = 15
	print('Testing:n = '+str(n))
	print(isPower(n))
		
