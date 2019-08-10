'''
题目描述：实现字符串的反转，要求不使用任何系统方法，且时间复杂度最小
方法一：临时变量法
方法二：异或法直接交换
'''
#方法一实现
def reverseStr(string):
	if string is None or len(string) == 0:
		return 
	if type(string) is str:
		string = list(string)
	left = 0
	right = len(string) - 1
	while left < right:
		string[left],string[right] = string[right],string[left]
		left += 1
		right -= 1
	return ''.join(string)

#方法二实现
def reverseStr2(string):
	if string is None or len(string) == 0:
		return 
	if type(string) is str:
		string = list(string)
	left = 0
	right = len(string) - 1
	while left < right:
		string[left] = chr(ord(string[left]) ^ ord(string[right]))
		string[right] = chr(ord(string[left]) ^ ord(string[right]))
		string[left] = chr(ord(string[left]) ^ ord(string[right]))
		left += 1
		right -= 1
	return ''.join(string)

if __name__ == '__main__':
	print(reverseStr2('abcde'))
