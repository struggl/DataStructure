'''
题目描述：把一个有序数组最开始的若干个元素搬到数组的末尾，称之为数组的旋转。
输入一个排好序的数组的一个旋转，输出旋转数组的最小元素。
例如[3,4,5,1,2]为数组[1,2,3,4,5]的一个旋转，该数组的最小值为1.

方法思路：
*旋转数组性质
1.元素先递增，然后突然降到最小值，然后递增。即旋转数组的最大值和最小值是相邻的，可以产生两种充分的判定规则
(1)arr[mid] < arr[mid-1],则arr[mid]为最小值(此时旋转比例较大)
如[4,5,1(mid),2,3]

(2)arr[mid] >= arr[mid-1] & arr[mid] < arr[mid+1],则arr[mid+1]为最小值(此时旋转比例较小)
如[3,4,5(mid),1,2]

2.旋转数组的第一个元素大于最后一个元素,在性质未触发情况下，可以用来减半地确定最小值所在范围.此时有两种情况
(1)arr[low] < arr[mid],旋转数组左半边不符合性质2，则最小值只可能在右半边(此时旋转比例较大)
如[6,7,1,2(mid),3,4,5]

(2)arr[mid] < arr[high],旋转数组左半部分符合性质2,而右半部分不符合，则最小值只可能在左半边(此时因为旋转比例较小)
如[3,4,5,6,7(mid),8,9,1,2]

(3)左右半边都不符合性质2,只能在左右半边都进行搜索，取二者最小值。(此时数组存在大量相同元素或未发生旋转）
如[1,0,1,1(mid),1,1,1](旋转比例太大)
如[1,1,1,1(mid),1,0,1](旋转比例太小)
如[1,2,3,4,5(mid),6,7,8,9](数组未旋转)

'''
def get_min(arr,low,high):
	#参数边界检测
	if arr is None or arr == []:
		return
	if low < 0 or high >= len(arr) or low > high:
		return
	#递归终止返回
	if low == high:
		return arr[low]
	#进入判断流程
	mid = low + ((high - low) >> 1)
	#旋转较大的充分判定条件
	if arr[mid] < arr[mid-1]:
		return arr[mid]
	#旋转较小时的充分判定条件
	elif arr[mid+1] < arr[mid]:
		return arr[mid+1]
	#旋转较大时确定最小值范围
	elif arr[mid] < arr[high]:
		return get_min(arr,low,mid-1)
	#旋转较小时确定最小值范围
	elif arr[low] < arr[mid]:
		return get_min(arr,mid+1,high)
	else:
		return min(get_min(arr,low,mid-1),get_min(arr,mid+1,high))

if __name__ == '__main__':
	arr = [3,4,5,6,7,8,9,1,2]
	print('testing:',str(arr))
	print(get_min(arr,0,len(arr)-1))
	print('=====')	
	arr = [1,2,3,4,5,6,7,8]
	print('testing:',str(arr))
	print(get_min(arr,0,len(arr)-1))
	print('=====')	
