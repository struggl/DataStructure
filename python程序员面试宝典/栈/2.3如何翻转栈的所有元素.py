'''
题目描述：不使用其他数据结构而翻转栈的元素
(如果使用其他结构那就直观到没有探讨的意义了)

注意概念：若一个栈依次push 1,2,3,4,5,则栈底为1，栈r为5,即最先进去的为栈底，最后进去的为栈顶(算法导论p129)

方法思路：递归
'''
class Empty(Exception):
	pass

class ArrayStack:
	def __init__(self):
		self.__data = []
	
	def push(self,val):
		self.__data.append(val)

	def pop(self):
		if self.is_empty():
			raise Empty('Stack is empty!')
		return self.__data.pop()
	
	def top(self):
		if self.is_empty():
			raise Empty('Stack is empty!')
		return self.__data[-1]

	def is_empty(self):
		return len(self.__data) == 0

	def __len__(self):
		return len(self.__data)

def print_stack(stack):
	while True:
		try:
			print(stack.pop())
		except Empty:	
			print('End')
			break			

#实现栈元素的逆序



