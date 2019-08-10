'''
题目描述：有一个由大小写字母组成的字符串，请对它重新组合，使得其中的所有小写字母排在大写字母前面
(大写或小写字母不要求顺序)
'''
def ReverseStr(string):
	if string is None:
		return
	if len(string) <= 1:
		return
	if type(string) == str:
		string = list(string)
	left = 0
	right = len(string) - 1
	while left < right:
		while string[left] >= 'a' and string[left] <= 'z':
			left += 1
		while string[right] >= 'A' and string[right] <= 'Z':
			right -= 1
		if left < right:
			string[left],string[right] = string[right],string[left]
			left,right = left + 1,right - 1
	return ''.join(string)

if __name__ == '__main__':
	print(ReverseStr('ABCDdeFGfg'))
	print(ReverseStr('AbcDef'))
