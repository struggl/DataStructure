'''
题目描述：假设L=<a_1,a_2,...,a_n>是n个不同的实数序列，则L的递增子序列为<a_k1,a_k2,...,a_km>,
其中k1<k2<...<km,a_k1<a_k2<...<a_km.

方法一思路：将序列从小到大排序，于是问题转化为求排序后的序列与原序列的最大公共子序列(公共子序列不要求连续，公共子串要求连续)

方法二思路：动态规划
(思路上可以与最大连续子数组和的DP法进行对比,最大区别在于子序列不需要连续)
错误写法的原始思路：
定义c[i]为以第i个位置结尾的最大递增子序列长度，MaxRight为该子序列最右端位置
if c[i] > c[MaxRight]时，c[i] = c[MaxRight] + 1,并令MaxRight = i
但这种写法会遇到一个问题，以字符串'xbcdazabcdefghi'为例，求解'xbcdaz'这部分时，没有问题，但是后面部分就解决不了，
因为MaxRight停留在'z'对应位置，而后续的'abcdefghi'这个最优解没有一个字符比'z'大。

上述错误思路的根源在于延续了最大连续子数组和的遍历顺序，但是连续与不连续的区别导致了问题。

正确思路在于每次确定c[j]时，先令c[j]为1，然后遍历0到(j-1)的位置i，逐个判断是否小于c[j],若有，则c[j] = c[i] + 1
'''
###错误的写法
def getMaxAscendingList_(List):
	if List is None or len(List) == 0:
		return
	if type(List) is str:
		List = list(List)
	lens = len(List)
	if lens == 1:
		return List
	MaxRight = 0
	c = [1] + [None]*(lens-1)
	for i in range(1,lens):
		if List[i] <= List[MaxRight]:
			if c[MaxRight] == 1:
				MaxRight = i
				c[i] = 1
			else:
				c[i] = 1
		else:
			c[i] = c[MaxRight] + 1
			MaxRight = i
	print(c)

#正确写法
#还有一个欠缺：得到最优值，但没有给出最优解，即对应的最大递增子序列
def getMaxAscendingList(List):
	if List is None or len(List) == 0:
		return
	if type(List) is str:
		List = list(List)
	lens = len(List)
	if lens == 1:
		return 1
	maxLen = [None] * lens
	maxLen[0] = 1
	maxAscendingLen = 1
	for i in range(1,lens):
		maxLen[i] = 1
		for j in range(i):
			if List[j] < List[i] and maxLen[j] > maxLen[i] - 1:
				maxLen[i] = maxLen[j] + 1
				maxAscendingLen = maxLen[i]
	print(maxAscendingLen)


if __name__ == '__main__':
	getMaxAscendingList('xbcdaz')
	getMaxAscendingList('xbcdazabcdefghi')
	getMaxAscendingList('xbcdafabcdefaghi')
