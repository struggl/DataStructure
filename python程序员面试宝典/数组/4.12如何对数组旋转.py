'''
题目描述：将n*n的二维数组逆时针旋转45°后打印
输入样例
1 2 3
4 5 6
7 8 9
输出
3
2 6
1 5 9
4 8
7
方法思路：
step1:先输出对角线以上部分
step2:输出对角线以及对角线以下部分
'''
def rotateArr(arr):
	if type(arr) != list or type(arr[0]) != list:
		return
	if len(arr) != len(arr[0]):
		return
	i = len(arr) - 1
	#step1:先输出对角线以上部分
	while i > 0:
		row = 0
		col = i	
		while col < len(arr):
			print(arr[row][col])
			row += 1
			col += 1
		print('\n')
		i -= 1
	#step2:输出对角线以及对角线以下部分
	for i in range(len(arr)):
		row = i
		col = 0
		while row < len(arr):
			print(arr[row][col])
			row += 1
			col += 1		
		if i != len(arr)-1:
			print('\n')
if __name__ == '__main__':
	arr = [[1,2,3],[4,5,6],[7,8,9]]
	rotateArr(arr)
