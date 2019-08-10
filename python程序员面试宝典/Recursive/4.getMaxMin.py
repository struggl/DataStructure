#返回数组中的最大值和最小值，递归解法的代码神似归并排序
#蛮力法(擂台法)需要2n-2次比较
def getMaxMin(List):
	#参数边界处理
	if List is None or len(List) == 0:
		return False
	#递归终止返回
	if len(List) == 1:
		Max = List[0]
		Min = List[0]
		return Max,Min
	if len(List) == 2:
		if List[0] >= List[1]:
			Max,Min = List[0],List[1]
			return Max,Min
		else:
			Max,Min = List[1],List[0]
			return Max,Min
	#划分子问题
	n = len(List) // 2
	max_left,min_left = getMaxMin(List[:n])
	max_right,min_right = getMaxMin(List[n:])
	if max_left >= max_right:
		Max = max_left
	else:
		Max = max_right
	if min_left >= min_right:
		Min = min_right
	else:
		Min = min_left
	return Max,Min


if __name__ == '__main__':
	print('Testing:[1,2,3,4,5]')
	print(getMaxMin([1,2,3,4,5]))
	print('Testing:[5,4]')
	print(getMaxMin([5,4]))
	print('Testing:[5]')
	print(getMaxMin([5]))
	print('Testing:[1,2,2,3,0]')
	print(getMaxMin([1,2,2,3,0]))
		
	
