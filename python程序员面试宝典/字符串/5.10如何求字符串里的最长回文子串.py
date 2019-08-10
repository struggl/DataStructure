'''
题目描述：回文字符串是指一个字符串从左到右和从右到左遍历得到的序列是相同的。
现要求字符串里的最长回文子串

方法一：蛮力法。对字符串的所有可能的顺序子串按长度从大到小进行遍历，逐个判断它是否为回文子串。
step1:allStrs = getAllStrs(string)
复杂度为O(n**2)
step2:allStrs = sorted(allStrs,key=lambda a:len(a),reverse=True)
复杂度为O(nlogn)
step3:
	for Str in allStrs:
		if isPalindrome(Str):
			return Str
这个片段的总复杂度实际上为O(长度为n的字符串的所有子串总长度）
显然，n长的字符串包含长度为1的子串n个，长度为2的子串(n-1)个,...,长度为n的子串1个
总长度为1*n+2*(n-1)+...+n*1
可以用数学归纳法证明总和为n*(n+1)*(n+2)/6
因此此循环总复杂度为O(n**3),即为蛮力法的时间复杂度

方法二：动态规划法。如果用f[i,j]来表示从i到j的子串是否为回文子串，那么
(1)当i=j时，f(i,j)为True
(2)当j=i+1时，f(i,j)取值为S[i]==S[j]
(3)当j>i+1时，f(i,j)取值为：S[i]==S[j] and f(i+1,j-1)
时空复杂度均为O(N**2)

方法三：中心扩展法。遍历字符串所有字符，每个字符都假定为回文子串中心，向两边扩展
例如子串'aba'中，以字符'b'为中心，两端同时向两边进行扩展，这样就可以找到该字符为中心的最大回文子串。
对所有字符的结果取最大，即得到题目所求
问题在于若回文子串为'abba'这样的偶数串，则从单个字符扩展是找不到的。
因此要么遍历每个位置，以该位置字符为中心扩展一次，又以该位置与下个位置共两个字符为中心扩展一次；
要么以特殊符号填充字符串，例如'abba'变为'#a#b#b#a#',这样就只需要遍历每个位置扩展一次即可。
假设最大回文子串的中心位置为Max_pos,在此位置上对填充字符串得到的辅助数组元素值为Max_len
则从Max_pos到左右两端的距离都为Max_len-1(包含两个端点),因此
res = string([Max_pos-Max_len+1,Max_pos+Max_len])
return ''.join(res.split('#'))
时间复杂度为O(n**2),空间复杂度为O(n)(辅助数组的长)

方法四：Manacher法。此方法通过减少中心扩展法的重复而把时间优化到O(n)
对这个重复的理解：以字符串'abcba'为例，当以'c'为中心做扩展时，左边的'abc'实际上已经在index=1的位置遍历过了。
定义RL[i]为以第i个字符为中心的回文子串的最右一个字符j与字符i的距离，即j-i+1.示例：
string: # a # b # a #
index:  0 1 2 3 4 5 6
RL:	1 2 1 4 1 2 1
RL-1:	0 1 0 3 0 1 0
显然RL-1这个数组的最大值就是最大回文子串的长度,于是问题首先转化为如何快速求解RL数组。



'''
#方法一实现
def getLongestPalindrome(string):
	if type(string) != str or string == '':
		return
	#获取string的所有可能顺序子串,复杂度为
	allStrs = getAllStrs(string)
	allStrs = sorted(allStrs,key=lambda a:len(a),reverse=True)
	Max_Len = 0
	for Str in allStrs:
		if isPalindrome(Str):
			if len(Str) > Max_Len:
				Max_Str = Str
				Max_Len = len(Str)
	return Max_Str

def getAllStrs(string):
	arr = []
	for i in range(len(string)):
		for j in range(i+1,len(string)+1):
			arr.append(string[i:j])
	return arr	

def isPalindrome(Str):
	if len(Str) == 1:
		return True
	i = 0
	j = len(Str) - 1
	while i < j:
		if Str[i] == Str[j]:
			i += 1
			j -= 1
		else:
			return False
	return True	

'''
方法二：动态规划法。如果用f[i,j]来表示从i到j的子串是否为回文子串，那么
(1)当i=j时，f(i,j)为True
(2)当j=i+1时，f(i,j)取值为S[i]==S[j]
(3)当j>i+1时，f(i,j)取值为：S[i]==S[j] and f(i+1,j-1)
'''
#方法二实现
#getLongestPalindrome2是正确的，
#而getLongestPalindrome2_则展示了一种容易出错的陷阱。
#即：最大回文子串DP方法在j-i>1时要使得f[i][j]为真，需要s[i] == s[j] and f[i+1][j-1],
#getLongestPalindrome2_在确定这个f[i][j]时，f[i+1][j-1]还没有计算出来，从而引发逻辑错误
#总结：最大回文子串DP方法务必按列填充表格！
def getLongestPalindrome2(string):
	if type(string) != str or string == '':
		return
	lens = len(string)		
	f = []
	for i in range(lens):
		f.append([None]*lens)
	#f是二维数组，填充过程是逐列填充
	for j in range(lens):
		for i in range(j+1):
			if j-i<2:
				f[i][j] = string[j] == string[i]
			else:
				if string[i] == string[j] and f[i+1][j-1]:
					f[i][j] = True
				else:
					f[i][j] = False
	'''f是一个二维数组，对角线必为True,从第一行遍历到最后一行，当前行可能取值如下：
	(1)全为True，则回文子串为整个string(如'aaaa')
	(2)存在None或者False,但有两个以上的True，则回文子串为最左边和最右边两个True之间(含端点)(如'habcbaw')
	(3)仅含有一个True,若已经到达最后一行，说明string不存在长度大于1的回文子串(如'abcd')
	注意：从第一行遍历到最后一行是必然要求，例如，string为'baaaa'的时候，第一行除了第一个元素，其他全为False，
	而第二行除了第一个元素，全为True
	'''
	print(f)
	#当string类似与'aaaa'这样连续重复时，会出现多个True
	st = ed = None
	for i in range(lens):
		for j in range(i,lens):
			if f[i][j]:
				if st is None:
					st = j
				else:
					ed = j
		if ed != None:
			#print(i)
			return string[st:ed+1]
		else:
			st = ed = None
	#这一步说明回文子串不大于1，返回第一个字符作为结果
	return string[0]

def getLongestPalindrome2_(s):
	if type(s) != str or s == '':
		return
	lens = len(s)
	c = []
	for i in range(lens):
		c.append([None]*lens)
	for i in range(lens):
		for j in range(i,lens):
			if j - i <= 1:
				c[i][j] = s[i] == s[j]
			else:
				if s[i] == s[j] and c[i+1][j-1]:
					c[i][j] = True
				else:
					c[i][j] = False
	st = ed = None
	print(c)
	for i in range(lens):
		for j in range(i,lens):
			if c[i][j] == True:
				if st is None:
					st = j
				else:
					ed = j
		if ed != None:
			return s[st:ed+1]
		else:
			st = ed = None
	return s[0]	
	
'''			
方法三：中心扩展法。遍历字符串所有字符，每个字符都假定为回文子串中心，向两边扩展
例如子串'aba'中，以字符'b'为中心，两端同时向两边进行扩展，这样就可以找到该字符为中心的最大回文子串。
对所有字符的结果取最大，即得到题目所求
问题在于若回文子串为'abba'这样的偶数串，则从单个字符扩展是找不到的。
因此要么遍历每个位置，以该位置字符为中心扩展一次，又以该位置与下个位置共两个字符为中心扩展一次；
要么以特殊符号填充字符串，例如'abba'变为'#a#b#b#a#',这样就只需要遍历每个位置扩展一次即可。
'''
#方法三实现
def getLongestPalindrome3(string):
	if type(string) != str or string == '':
		return
	string = '#' + '#'.join(string) +'#'
	P = []
	Max_len = 1
	Max_pos = 0
	for i in range(len(string)):
		tmp = expand(string,pos=i)
		P.append(tmp)
		if tmp > Max_len:
			Max_len = tmp
			Max_pos = i
	res = string[Max_pos-Max_len+1:Max_pos+Max_len]
	return ''.join(res.split('#'))

def expand(string,pos):
	if pos == 0:
		return 1
	left = pos
	right = pos
	cnt = 0
	while left >=0 and right <= len(string) - 1:
		if string[left] != string[right]:
			return cnt
		else:
			cnt += 1
			left -= 1
			right += 1
	return cnt

#方法四实现
def getLongestPalindrome4(s):
	#Manacher算法
	s = '#' + '#'.join(s) + '#'	 
	RL = [0] * len(s)
	MaxRight = 0
	pos = 0
	MaxLen = 0
	MaxPos = 0
	for i in range(len(s)):
		if i < MaxRight:
			RL[i] = min(RL[2*pos-i],MaxRight-i)
		else:
			RL[i] = 1
		#尝试继续扩展位置i的回文子串，注意边界
		while i-RL[i] >= 0 and i + RL[i] < len(s) and s[i-RL[i]] == s[i+RL[i]]:
			RL[i] += 1
		#更新MaxRight,pos
		if RL[i] + i - 1 > MaxRight:
			MaxRight = RL[i] + i - 1
			pos = i
		#更新MaxLen
		if RL[i] > MaxLen:
			MaxLen = RL[i]
			MaxPos = i		
	return MaxLen-1,pos

if __name__ == '__main__':
	#string = 'habcubkobcabi'
	string = 'habcbab'
	#string = 'abcba'
	#string = 'bcaaaacb'
	#print(getLongestPalindrome(string))
	print(getLongestPalindrome2(string))
	print(getLongestPalindrome2_(string))
	#print(getLongestPalindrome3(string))
	#print(getLongestPalindrome4(string))
	
