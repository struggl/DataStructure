'''
题目描述：给定主字符串S与模式字符串P，判断P是否为S的子串，若是，则找出P在S中第一次出现的下标。

方法一：蛮力法,O(n*m)
方法二：优化的蛮力法,O(m(n-m+1))
方法三：KMP算法，O(n+m)
'''
#方法一实现
def match(s,p):
	if type(s) != str or type(p) != str:
		return
	n,m = len(s),len(p)
	if n == 0 or m == 0 or n < m:
		return -1
	#标记模式串下标
	j = 0
	#标记主串下标
	i = 0
	while i < n and j < m:
		'''原来的错误写法：错误原因在于，暴力法本是遍历主串所有位置，逐次尝试匹配，但是这里由于主串下标i在尝试匹配过程
		中增量了，因此当前尝试失败后，将会跳过许多位置没有遍历
		while j < m and s[i] == p[j]:
			if j ==  m - 1:
				return i - m + 1
			j += 1
			i += 1
		j = 0
    		i += 1

		'''
		k = i
		while j < m and s[k] == p[j]:
			if j == m - 1:
				return i
			j += 1
			k += 1
		j = 0
		#主串偏移一个单位
		i += 1
	return -1

#方法二实现
def match2(s,p):
	if type(s) != str or type(p) != str:
		return
	n,m = len(s),len(p)
	if n == 0 or m == 0 or n < m:
		return -1
	#标记模式串下标
	j = 0
	for i in range(n-m+1):
		while j < m and s[i+j] == p[j]:
			if j == m - 1:
				return i
			j += 1
		j = 0
	return -1				

#方法三实现
def match3(s,p):
	if type(s) != str or type(p) != str:
		return
	n,m = len(s),len(p)
	if n == 0 or m == 0 or n < m:
		return -1
	fail = compute_kmp_fail(p)	
	#标记主串下标
	i = 0
	#标记模式串下标
	j = 0
	while i < n:
		if s[i] == p[j]:
			if j == m - 1:
				return i - m + 1
			i += 1
			j += 1
		elif j > 0:
			j = fail[j-1]
		else:
			i += 1
	return -1

def compute_kmp_fail(p):
	#本质上是遍历每个字符，统计前缀与后缀的公共子集大小
	#例如模式串p = 'amalgama'
	#0位置时，前后缀均为空集，因此fail[0] 为 0
	#遍历到5位置时，前缀为['a','am','ama','amal','amalg']
	#后缀为['malga','alga','lga','ga','a']
	#前后缀共有1个公共元素，因此fail[5] 为 1
	m = len(p)
	fail = [0] * m
	#标记模式串下标
	i = 1 
	#标记前缀下标
	j = 0
	while i < m:
		if p[i] == p[j]:
			fail[i] = j + 1
			i += 1
			j += 1
		elif j > 0:
			j = fail[j-1]
		else:
			i += 1
	return fail

if __name__ == '__main__':
	s = 'abcdef'
	p = 'def'
	print(match(s,p))
	print('=====')	

	s = 'abcdef'
	p = 'adef'
	print(match(s,p))
	print('=====')	
	#print(compute_kmp_fail(p='amalgama'))
	print(compute_kmp_fail(p='abcba'))
