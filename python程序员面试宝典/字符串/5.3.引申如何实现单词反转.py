'''
题目描述：如何实现单词反转
思路：对每个单词反转，用空格串接起来，然后整个再反转一次
'''

def reverseWord(string):
	if string is None or len(string) == 0:
		return 
	if type(string) != str:
		return
	res = []
	for Str in string.split(' '):
		res.append(reverseStr(Str))
	res = ' '.join(res)
	return reverseStr(res)		

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

if __name__ == '__main__':
	print(reverseWord('I like you'))
