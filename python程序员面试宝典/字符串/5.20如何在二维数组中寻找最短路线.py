'''
题目描述：寻找一条从左上角(arr[0][0])到右下角(arr[m-1][n-1])的路线(每次只能向下或向右),使得沿途经过的
数组中整数和最小

方法思路：动态规划。
'''
def getMinPath(a):
	if type(a) != list or type(a[0]) != list:
		return
	m = len(a)
	n = len(a[0])
	f = []
	for i in range(m):
		f.append([None]*n)
	#初始化第一个元素为a[0][0]
	f[0][0] = a[0][0]
	#初始化第一列元素
	for i in range(1,m):
		f[i][0] = f[i-1][0] + a[i][0]
	#初始化第一行元素
	for i in range(1,n):
		f[0][i] = f[0][i-1] + a[0][i]
	#填表
	for i in range(1,m):
		for j in range(1,n):
			f[i][j] = min(f[i][j-1],f[i-1][j]) + a[i][j]
	return f[m-1][n-1]

if __name__ == '__main__':
	a = [[1,4,3],[8,7,5],[2,1,5]]
	print(getMinPath(a))
