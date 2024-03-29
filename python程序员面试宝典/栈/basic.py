'''
栈的实现，支持5个接口
push
pop
top
len
is_empty

思路一：数组实现
思路二：链表实现
'''
#思路一实现
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

if __name__ == '__main__':
	stack = ArrayStack()
	stack.push(1)
	stack.push(2)
	stack.push(3)
	while True:
		print('length of this stack is {}'.format(len(stack)))
		try:
			print(stack.pop())
		except Empty:
			print('End!')	
			break
