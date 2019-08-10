'''
题目描述：换位字符串是指组成字符串的字符相同，但位置不同。
例如'aaaabbc'与'abcbaaa'就是换位字符串

方法：用字典记录s1中字符及其频率，遍历s2中字符，若字符不存在，return False，
否则，若该字符对应的频率大于0，将频率减1，若频率为0，删除该键。最终若字典为空，return True
，否则 return False
'''

'''错误思路，badcase: ('aaaaaaabbc','abcbaaa'),组成字符相同，但数量不同，也不能算换位字符串
def compare(s1,s2):
	if type(s1) != str or type(s2) != str:
		return
	if s1 == s2:
		return False
	if set(s1) == set(s2):
		return True
	else:
		return False
'''

def compare(s1,s2):
	if type(s1) != str or type(s2) != str:
		return
	if s1 == s2:
		return False
	Dict = dict()
	Dict['b'] = 0
	for ch in s1:
		if not Dict.get(ch):
			Dict[ch] = 1
		else:
			Dict[ch] += 1
	for ch in s2:
		if not Dict.get(ch):
			return False
		if Dict[ch] > 1:
			Dict[ch] -= 1
		else:
			del(Dict[ch])
	if bool(Dict):
		return False
	else:
		return True

if __name__ == '__main__':
	print(compare('aaaaaaabbc','abcbaaa'))
	print(compare('aaaabbc','abcbaaa'))
	print(compare('aaaabbcd','abcbaaa'))

