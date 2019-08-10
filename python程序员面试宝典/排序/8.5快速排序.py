'''
快速排序与归并排序对比
1.均为分治策略应用的典范
2.二者区别在于子问题划分方式的不同
归并法每次都是从中间划分，合并时再比较大小
快速排序则是选定一个基准值，小于它的分到L子序列，等于它的分到E子序列，大于它的分到G子序列，合并时直接L+E+G即可
3.归并排序性能为O(nlogn)
快速排序最慢为O(n**2)。
但是随机化快速排序的期望运行时间为O(nlogn)

定义随机化快速排序：
基准值为序列中的随机元素,其余部分保持不变
'''
#随机快速排序(非就地)
def quick_sort(arr):
	#参数边界检测
	if type(arr) != list:
		return
	#递归终止返回
	if len(arr) < 2:
		return arr
	import random
	key = random.choice(arr)
	#key = arr[0]
	L = []
	E = []
	G = []
	for v in arr:
		if v < key:
			L.append(v)
		elif v == key:
			E.append(v)
		else:
			G.append(v)
	return quick_sort(L) + E + quick_sort(G)

#选定最后一个元素为基准值的就地快速排序
'''
就地快速排序通过使用元素交换的方法该表输入序列，并且隐式地创建新的子序列。
输入序列的子序列通过一个被最左索引left和最右索引right表示出来。
序列分解是通过使用向前移动的本地变量left和向后移动的本地变量right同时扫描数组，并交换逆序元素对来实现的
当两个索引相互经过时，分解步骤完成，且算法会在两个子序列上递归完成。
'''
def inplace_quick_sort(arr,a,b):
	#参数边界检测
	if type(arr) != list:
		return
	#递归终止返回	
	if a >= b:
		#当left等于right时已经排好序了
		return	
	index = b
	key = arr[index]
	right = b - 1
	left = a
	while left <= right:
		while left <= right and arr[left] < key:
			left += 1
		while left <= right and arr[right] > key:
			right -= 1
		if left <= right:
			arr[left],arr[right] = arr[right],arr[left]
			left,right = left+1,right-1
	#把key放到left位置上
	arr[index],arr[left] = arr[left],arr[index]
	inplace_quick_sort(arr,a,left-1)
	inplace_quick_sort(arr,left+1,b)		

#选定第一个元素为基准值的就地快速排序
def inplace_quick_sort2(lists,left,right):
	if left >= right:
		return lists
	key = lists[left]
	low = left
	high = right
	while left < right:
		while left < right and lists[right] >= key:
			right -= 1
		lists[left] = lists[right]
		while left < right and lists[left] <= key:
			left += 1
		lists[right] = lists[left]
	lists[right] = key
	inplace_quick_sort2(lists,low,left-1)
	inplace_quick_sort2(lists,left+1,high)
	return lists
	


if __name__ == '__main__':
	arr = [2,3,4,5,4]	
	print(arr)
	print()
	inplace_quick_sort2(arr,0,len(arr)-1)
	print(arr)
	#print(quick_sort(arr))
	print('=====')
	arr = [5,4,3,2,1,7,8,9,45,32]
	print(arr)
	print()
	inplace_quick_sort2(arr,0,len(arr)-1)
	print(arr)
	#print(quick_sort(arr))
