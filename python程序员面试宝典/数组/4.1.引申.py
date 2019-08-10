'''
题目描述：对于一个给定的自然数N，有一个N+M个元素的数组，其中存放了小于等于N的所有自然数，
在不申请额外空间的情况下，求重复出现的自然数序列{X}(这里所谓的自然数不包含0在内)

def findDup(array,num):
	s = set()
	if array is None:
		return s
	lens = len(array)
	index = array[0]
	num -= 1
	while True:
		if array[index] < 0:
			num -= 1
			array[index] = lens - num
			s.add(index)
		if num == 0:
			return s
		array[index] *= -1
		index = array[index] * -1
'''
def findDup(arr,num):
	if arr is None:
		return
	if type(arr) != list:
		return
	hashTable = set()
	dup = set()
	for i in range(len(arr)):
		if arr[i] in hashTable:
			dup.add(arr[i])
		else:
			hashTable.add(arr[i])
	return list(dup)
				

if __name__ == '__main__':
	array = [2,4,1,2,3,3,3,4,5,5,5,5,6]
	#array = [1,2,3,3,4,4,5,6]
	num = 6
	s = findDup(array,num)
	for i in s:
		print(i)
