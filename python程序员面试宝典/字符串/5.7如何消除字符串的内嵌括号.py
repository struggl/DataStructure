'''
题目描述：
输入样例
(1,(2,3),(4,(5,6),7))
输出结果
(1,2,3,4,5,6,7)

方法思路：
参数边界检测：
1.表达式中只有数字，逗号，括号
2.左右括号数量应该相等(用一个量表示括号数量，碰到左括号增1，右括号减1.若该量为0而遇到了右括号，则参数非法。最终该量为0，则合法)
消除括号：
除了左右端括号，其余非括号字符按顺序保存即可
'''
def removeNestedPare(string):
	if string is None:
		return
	n = 0
	if string[0] != '(' or string[-1] != ')':
		print('!')
		return False
	for i in range(len(string)):
		if string[i] < '0' or string[i] > '9':
			if string[i] != ',' and string[i] != '(' and string[i] != ')':
				print('-')
				return False
			if string[i] == '(':
				n += 1
			if string[i] == ')':
				if n == 0:
					print('=')
					return False
				n -= 1

	List = ['(']
	for i in range(1,len(string)-1):
		if string[i] != '(' and string[i] != ')':
			List.append(string[i])
	List.append(')')
	return ''.join(List)

if __name__ == '__main__':
	print(removeNestedPare('(1,(2,3),(4,(5,6),7))'))
			
			
			
