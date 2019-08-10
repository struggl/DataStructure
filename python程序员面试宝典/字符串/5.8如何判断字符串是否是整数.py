'''
题目描述：如何判断字符串是否是整数
方法一：递归法
方法二：非递归法，本质与方法一相同，只是把递归改为循环罢了
'''
def Is_Num(c):
	return c >= '0' and c <= '9'

def strToint(string):
	#参数边界处理
	if string is None or len(string) == 0:#空列表不为None
		return False
	if len(string) == 1:
		if Is_Num(string):
			#此返回非递归终止返回，而仅仅是参数边界处理
			return int(string)
		else:
			return False
	#确定调用递归函数的参数状态
	else:
		if string[0] == '+':
			tmp = strtoint(string[1:])
			if tmp:
				return tmp
			else:
				return False
		if string[0] == '-':
			tmp = strtoint(string[1:])
			if tmp:
				return tmp * (-1)
			else:
				return False
		if Is_Num(string[0]):
			tmp = strtoint(string)
			if tmp:
				return tmp
			else:
				return False
		else:
			return False

#方法一实现
def strtoint_(string):
	#能进入本函数的参数，形如'123','1$3','12$',首字符必定为整数
	#递归终止返回
	if len(string) == 1:
		return int(string)
	#由于问题特性，无法将全部异常处理挡在递归函数之外，因此递归内部也要有参数检测处理
	if not Is_Num(string[-1]):
		return False
	#strtoint(string[:-1])实现了子问题划分
	tmp = strtoint(string[:-1])
	#由于异常输入以False返回为标志，因此每次调用必须判断是否为False
	#tmp * 10 + ord(string[-1]) - ord('0')实现了子问题答案的归并
	if tmp:
		return tmp * 10 + ord(string[-1]) - ord('0')
	else:
		return False

#方法二实现
def strtoint(string):
	if len(string) == 1:
		return int(string)
	for i in range(len(string)):
		if not Is_Num(string[i]):
			return False
	Sum = 0
	for i in range(len(string)):
		Sum = Sum * 10 + ord(string[i]) - ord('0')
	return Sum

if __name__ == '__main__':
	print(strToint('123'))
	print(strToint('+123'))
	print(strToint('-123'))
	print(strToint('12$'))
	print(strToint('$12'))
	print(strToint('1$2'))

'''
1.写递归函数时，先明确递归函数接收的参数状态，明确子问题划分/子问题解决 和 子问题答案的归并
2.以返回False作为异常输入的标志，则每次调用递归函数时，无论是外部调用还是内部调用自身，都应该判断返回值是否为False
'''
