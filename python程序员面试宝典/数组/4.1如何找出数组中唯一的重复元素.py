'''
题目描述：给定1-1000共1001个元素,其中仅有一个重复元素，不利用辅助空间找出该元素
方法一：哈希法(或者麻烦点，用字典)
缺点：利用了辅助空间，时空复杂度皆为O(N),不合题意

方法二：累加求和，由于只有一个重复元素，并且已知所有元素都在集合{1,2,3,...,1000},则可将数组之和减去集合元素之和
缺点：和可能溢出

方法三：异或法。对于非0数字a,b,c,
a^b^c = a^c^b(交换律)
a^0 = a
a^a = 0
利用上述规律，把数组异或一遍，然后把集合{1,2,...,1000}异或一遍，所得结果即为所求的重复元素。
例如arr=[1,2,3,3]
实现过程实际为：(1^2^3^3)^(1^2^3) = (1^1)^(2^2)^(3^3)^3 = 0^0^0^3 = 3

方法四：数据映射法
把数组取值操作看做一个特殊的映射函数f:D->R,定义域为[0,1000]，值域为[1,1000]。数组从0开始遍历，若取到的元素为正数
则将该元素作为下标继续遍历，同时将该元素置为相反数。
时间复杂度为O(N),空间复杂度为O(1)
缺点:是会改变原来数组(因为list是可变类型)

方法五：用数组看做单链表，把问题转换为“判断单链表是否存在环”。
缺点：这个方法要求数组中不含0,因为如果数组有0，假设第一个元素恰好存放0，那么arr[0]得到0，以此作为下标继续取值，
就形成了一个死循环


！！！上述五种方法中，如果给定数组arr含有0，则只有第一种方法可以完成任务，其余均需额外改动
'''
#方法一哈希法实现
def findDup(arr):
	if arr is None:
		return
	if type(arr) != list:
		return
	hashTable = set()
	for i in range(len(arr)):
		if arr[i] in hashTable:
			return arr[i]
		hashTable.add(arr[i])	


#方法二累加求和法实现
def findDup2(arr):
	if arr is None:
		return
	if type(arr) != list:
		return
	arr_Sum = 0
	Sum = 0
	for i in range(len(arr)):
		arr_Sum += arr[i]
	for i in range(len(arr)):
		#本质上元素集合为{1,2,...,len(arr)-1}，但range()产生的0显然对求和无影响
		Sum += i
	res = arr_Sum - Sum
	if res > 0:
		return res

#方法三异或法实现
def findDup3(arr):
	if arr is None:
		return
	if type(arr) != list:
		return
	res = 0
	for i in range(len(arr)):
		res ^= arr[i]
	for i in range(len(arr)):
		#因为a^0=a，所以没必要一定要使遍历范围为range(1,len(arr))
		res ^= i
	return res

#方法四数据映射法实现
def findDup4(arr):
	if arr is None:
		return
	if type(arr) != list:
		return
	i = 0
	while arr[i] >= 0:
		arr[i] *= -1
		i = -arr[i]
	if arr[i] < 0:
		return -arr[i]			

#方法五实现单链表求环法实现
def findDup5(arr):
	if arr is None:
		return
	if type(arr) != list:
		return
	#初始化快慢指针为第一个有效结点
	slowP = 0
	fastP = 0
	while True:
		#快指针一次走两步
		fastP = arr[arr[fastP]]
		#慢指针一次走一步
		slowP = arr[slowP]
		if fastP == slowP:
			break
	#重新置慢指针为第一个有效结点
	slowP = 0
	#快指针此时已经指向相遇点
	#令快慢指针都以步长1进行遍历，第一个相遇点即为环入口点，该入口点即为所求
	while True:
		if slowP == fastP:
			return slowP
		slowP = arr[slowP]
		fastP = arr[fastP]
		

if __name__ == '__main__':
	arr = [1,2,3,3,4,5,6,7,8,9]
	print(arr)
	print()
	print(findDup3(arr)) 
	print()
	print(arr)
	print('=====')

	arr = [1,9,2,3,4,5,6,7,8,9]
	print(arr)
	print()
	print(findDup5(arr)) 
	print()
	print(arr)
