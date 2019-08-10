#链表的创建和输出
class LNode(object):
	def __init__(self,x):
		self.data = x
		self.Next = None

#创建链表(带头结点)
def create_List(values):
	head = LNode(None)
	if values is None:
		print('创建了一个仅有头结点的单链表')
		return head
	if type(values) != list:
		print('输入参数类型应为list')
		return False
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

#从尾到头打印链表
#这里是递归输出方法，也可以应用1.1如何实现链表的逆序.py将链表先逆序，然后在顺序输出
def print_List2(head):
	if head is None or head.data != None or head.Next is None:
		return False
	if head.Next.Next is None:
		print(head.Next.data)
	else:
		_print_List2(head.Next)


def _print_List2(head):
	if head.Next is None:
		print(head.data)
	else:
		_print_List2(head.Next)
		print(head.data)	

##双向链表构建
class BLNode(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None

def create_BList(values):
	#带头结点和尾结点，data属性均为None,头结点left属性为None，尾结点right属性为None
	Head = BLNode(None)
	End = BLNode(None)
	Head.right = End
	End.left = Head
	if values is None or type(values) != list or len(values) == 0:
		return Head,End
	cur_head = Head
	for v in values:
		tmp = BLNode(v)
		cur_head.right = tmp
		tmp.left = cur_head
		tmp.right = End
		End.left = tmp
		#迭代
		cur_head = tmp
	return Head,End	

def print_BList(Head,End):
	if Head is None or Head.data != None:
		pass
	else:
		cur = Head.right
		while cur != None and cur.data != None:
			print(cur.data)
			cur = cur.right
	print('---')	
	if End is None or End.data != None:
		pass
	else:
		cur = End.left
		while cur != None and cur.data != None:
			print(cur.data)
			cur = cur.left
			 
if __name__ == '__main__':
	head1 = LNode(None)
	head2 = LNode(None)
	print(head1 is head2)
	print('=====')

	values = ['体育','NBA','詹姆斯','杜兰特',1]
	print('Testing values:'+str(values))
	head = create_List(values)
	print('从头到尾输出单链表：')
	print_List(head)
	print('')
	print('从尾到头输出单链表:')
	print_List2(head)
	print('=====')

	values = None
	print('Testing values:'+str(values))
	head = create_List(values)
	print('从头到尾输出单链表：')
	print_List(head)
	print('')
	print('从尾到头输出单链表:')
	print_List2(head)
	print('=====')

	values = [1]
	print('Testing value:'+str(values))
	head = LNode(1)
	head = create_List(values)
	print('从头到尾输出单链表：')
	print_List(head)
	print('')
	print('从尾到头输出单链表:')
	print_List2(head)
	print('=====')

	values = ['体育','NBA','詹姆斯','杜兰特',1]
	print('Testing values:'+str(values))
	Head,End = create_BList(values)
	print_BList(Head,End)
	print('=====')

	
	


'''
结点类型
1.非法参数:None
2.头结点:self.data = None
3.尾结点:self.Next = None
4.实际存储值的结点:从头结点.Next开始到尾结点
迭代方式：
给定带头结点head的链表
cur = head.Next
while cur != None:
	print(cur.data)
	cur = cur.Next
'''
