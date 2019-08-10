#n级楼梯，每次只能走一级或者两级，问有多少种走法
#f(n) = f(n-1) + f(n-2),f(1) = 1,f(2) = 2
#DP方法时间复杂度为O(n),空间复杂度为O(1)。
#最简单的方法是把通项公式求出来，时空复杂度都为O(1)
def howmany(n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	a,b = 1,2
	'''for 循环写法
	for i in range(n-2):
		tmp = a + b
		a = b
		b = tmp
	return tmp
	'''
	#while循环写法
	i = 3
	while i <= n:
		tmp = a+ b
		a = b
		b = tmp
		i += 1
	return tmp

if __name__ == '__main__':
	print('Testing:n=3')
	print(howmany(3))
	print('Testing:n=5')
	print(howmany(5))

'''
动态规划思想：
1.找到问题的递推公式
2.利用递推公式自底向上地求解
'''
