'''
题目描述：单链表有环指的是单链表中某个结点的Next域指向的是链表中在它之前的某一个结点，
这样在链表的尾部形成一个环形结构。如何判断单链表是否有环的存在?
方法一：哈希法(此处也是暴力法)。遍历一次单链表，把每个结点存到哈希表中，如果当前遍历到的结点出现在哈希表中，则说明有环
方法二：快慢指针法。快慢指针都从第一个有效结点开始，快指针每次走2步，慢指针每次走1步，若二者能相等,
则说明有环。
'''
#链表的创建和输出
class LNode(object):
	def __init__(self,x):
		self.data = x
		self.Next = None

#创建链表(带头结点)
def create_List(values):
	if type(values) != list:
		print('给定参数必须为列表类型')
		return False
	head = LNode(None)
	if values is None:
		print('创建了一个仅有头结点的单链表')
		return head
	cur = head
	for v in values:
		tmp = LNode(v)
		cur.Next = tmp
		cur = tmp
	return head

#打印链表
def print_List(head):
	'''
	#啰嗦版参数边界检测
	if head is None:
		print('参数非法')
		return False
	if head.data != None:
		print('给定的单链表不带头结点')
		return False
	if head.Next is None:
		print('链表仅包含一个头结点')
		return False
	'''
	#简洁版参数边界检测
	if head is None or head.data != None or head.Next is None:
		return False
	cur = head.Next
	while cur != None:
		print(cur.data)
		cur = cur.Next

#方法一哈希法实现
def isLoop(head):
	if head is None or head.data != None or head.Next is None:
		return False
	hashTable = set()
	cur = head.Next
	while cur != None:
		if cur in hashTable:
			return True
		hashTable.add(cur)
		cur = cur.Next
	return False

#方法二快慢指针法实现
def isLoop2(head):
	if head is None or head.data != None or head.Next is None:
		return False
	'''另一种写法,这种写法在求环入口时，稍微麻烦一些,但不容易出错
	lowP = head.Next
	FastP = head.Next.Next
	while FastP != None:
		lowP = lowP.Next
		FastP = FastP.Next.Next
		if lowP is FastP:
			return True

	'''
	#这种写法很容易把循环入口写为while FastP != None，这样会引发bug
	#例如1->2->3->4->5->6
	#当lowP到结点3时，FastP到达结点6，此时FastP != None,于是循环继续，FastP.Next.Next会报错,
	#因为FastP.Next已经是None
	lowP = head.Next
	FastP = head.Next
	while FastP.Next != None:
		lowP = lowP.Next
		FastP = FastP.Next.Next
		if lowP is FastP:
			return True
	return False

if __name__ == '__main__':
	values = ['体育','NBA','詹姆斯','杜兰特',1]
	head = LNode(None)
	cur = head
	for v in values:
		tmp = LNode(v)
		cur.Next = tmp
		cur = tmp
	cur.Next = head.Next.Next
	print(isLoop2(head))
	print('=====')

	head = create_List(values)
	print(isLoop2(head))
	print('=====')
