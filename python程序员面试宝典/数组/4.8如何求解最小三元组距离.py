'''
题目描述：已知三个升序整数数组a[l],b[m],c[n],请在三个数组中各找一个元素，使得三元组距离最小。
三元组距离定义：假设a[i],b[j],c[k]为三元组，则距离为
max(abs(a[i]-b[j]),abs(a[i]-c[k]),abs(b[j]-c[k]))

方法一：蛮力法。直接遍历三个数组，求最小距离
'''
#方法一实现
def minDistance(a,b,c):
	import sys
	MinDist = sys.maxsize
	for i in range(len(a)):
		for j in range(len(b)):
			for k in range(len(c)):
				MinDist = min(MinDist,max(abs(a[i]-b[j]),abs(a[i]-c[k]),abs(b[j]-c[k])))
	return MinDist

if __name__ == '__main__':
	a = [3,4,5,7,15]
	b = [10,12,14,16,17]
	c = [20,21,23,24,37,30]
	print(minDistance(a,b,c))
