#不使用循环输出1到100
#子问题划分:n --> n-1,子问题解决：print传入的参数即可，递归边界:满足n > 0才继续分解
def prints(n):
	if n > 0:
		prints(n-1)
		print(n)

if __name__ == '__main__':
	n = 100
	print('Testing:n = '+str(n))
	prints(n)
