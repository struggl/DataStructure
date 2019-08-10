#如何不使用除法操作符实现两个正整数的除法
#法一:减法。被除数减去除数，直到差小于除数。时间复杂度为O(m/n).此方法同时也解决了不使用%运算法求余数的问题。
#法二:等价于法一，也可以采用加法。除数n加上n，直到和大于等于被除数。时间复杂度与法一相同
#法三:移位法.以m>=n为外层循环，每次循环使除数n逐次乘以2的1,2,3，...,k次方(指数增加过程通过移位实现)，直到乘积大于被除数n，累加2的(k-1)次方。
#累加和即为商。最终的m即为余数。时间复杂度为O(log(m/n))

'''
#法一
def divide(m,n):
	#m为被除数，n为除数
	#返回商和余数
	if m < n:
		return 0,m
	cnt = 0
	while m >= n:#边界条件是=还是>=,只需要以最简单的m=n和m=n+1的情况分析即可得到结论
		m -= n
		cnt += 1	
	return cnt,m
'''
'''
#法二:加法.
def divide(m,n):
	if m < n:
		return 0,m
	cnt = 0
	Sum = 0
	while m >= Sum:#边界条件是=还是>=,只需要以最简单的m=n和m=n+1的情况分析即可得到结论
		Sum += n
		cnt += 1
	cnt -= 1
	remain = m - Sum + n 
	return (cnt,remain)
'''

#法三:移位法
def divide(m,n):
	if m < n:
		return 0,m
	result = 0
	while m >= n:
		multi = 1
		while 2*multi*n <= m:
			multi <<= 1
		result += multi
		m -= multi*n
	return result,m

if __name__ == '__main__':
	m = 14
	n = 4
	print('Testing: m = {},n = {}'.format(m,n))
	print(divide(m,n))
	m = 16
	n = 4
	print('Testing: m = {},n = {}'.format(m,n))
	print(divide(m,n))
