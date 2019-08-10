def Bubble_sort(arr):
	if arr is None or arr == []:
		return 
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if arr[j] < arr[i]:
				arr[i],arr[j] = arr[j],arr[i]
	return arr	

if __name__ == '__main__':
	arr = [2,3,4,5,4]	
	print(arr)
	print()
	print(Bubble_sort(arr))
	print('=====')
	arr = [5,4,3,2,1,7,8,9,45,32]
	print(arr)
	print()
	print(Bubble_sort(arr))
'''
选择排序与插入排序的区别：
1.选排内外循环皆从左到右，每次内循环找到最小元素，放到外循环元素位置
2.插入排序外循环从第2个元素向右，内循环从外循环前一个元素向左。
交换方式是相邻交换

选择排序与冒泡排序的区别：
1.选排每次外循环都要找到右边序列最小的位置，然后把当前位置与最小位置交换值
2.冒泡是只要右边序列的值比当前小，就立刻与当前位置交换值

'''
