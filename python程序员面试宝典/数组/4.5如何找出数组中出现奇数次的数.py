'''
题目描述：数组中有N+2个数，其中N个数出现了偶数次，2个数出现了奇数次(这两个数不相等),请用O(1)的空间复杂度
找出这两个数。注意：不需要知道具体位置，只需要找出这两个数。

方法一：字典法。时空复杂度均为O(N)
方法二：异或法。时间为O(N)，空间为O(1)
假设数组为[4,8,9,9,12,12]，各元素二进制表示如下：
4: 0100
8: 1000
9: 1001
12:1100
首先把数组所有元素异或一遍，最终结果为4^8=12，记为result
接下来需要根据异或性质从result反推出所求的两个数：4和8
i = result
position = 0
while i & 1 == 0:
	position += 1
	i >>= 1
统计得到position为2。表明如果把12右移2位，则个位必为1(与操作结果为1)
(根据与操作的定义，仅当两个数的二进制各个位都相同，与结果才为1，否则为0。因此a&1要么为1要么为0)
这样一来，可以根据右移position位然后&1为1的条件，筛选得到一批数组元素。并从result开始对这批元素遍历取异或。
这一批数组元素中，可能存在出现偶数次的数，例如本例中的12，但是由于出现偶数次，因此异或操作会抵消掉。
剩下的只有所求两个数中的其中之一。
(之所以不会同时筛选得到所求的两个数，是因为result本身等价于这两个数异或的结果，result的某一位二进制取值为1，
说明两个数的二进制，只有其中一个在该位置取1，另一个取0)
这样一波操作以后，我们就得到了其中一个数，本例中为4，只需将原来的result(即为12)与4再异或一次，即可得到8.
'''
#方法一实现
def get2Num(arr):
	if arr is None or len(arr) < 1:
		return
	Dict = dict()
	for v in arr:
		if v in Dict:
			del(Dict[v])
		else:
			Dict[v] = 1
	for key in Dict.keys():
		print(key)


#方法二实现
def get2Num2(arr):
	if arr is None or len(arr) < 1:
		return
	result = 0
	position = 0
	#计算数组中所有数字的异或结果
	i = 0
	while i < len(arr):
		result ^= arr[i]
		i += 1
	tmpResult = result
	#找出异或结果中其中一个位值为1的位数(如1100，位值为1的位数为2和3)
	i = result
	while i & 1 == 0:
		position += 1
		i >>= 1	
	i = 1
	while i < len(arr):
		if ((arr[i] >> position) & 1) == 1:
			result ^= arr[i]
		i += 1
	print(result)
	print(result ^ tmpResult)

if __name__ == '__main__':
	arr = [0,5,6,6,5,-7,2,2]
	get2Num(arr)
