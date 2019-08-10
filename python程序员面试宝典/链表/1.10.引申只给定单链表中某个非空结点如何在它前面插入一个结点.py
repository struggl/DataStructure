'''
问题描述：只给定单链表中某个非空结点p，如何在p前面插入一个结点q
方法一思路：来自<<py宝典>>.把p指向q，然后交换两个结点的值。优点是时间复杂度为O(1)，缺点是无法在None前面插入结点
因为若p is None,则p.Next = q会报错
方法二思路：使用pre = head,cur = head.Next遍历单链表，找到结点p和它的前驱，直接把q插入,这可以在None前面插入结点，
缺点是时间复杂度为O(N)
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
#方法一
def Insert_Node(p,node):
	#把node插入到给定结点p前面
	if node is None or node.data is None:
		#待插入结点必须为有效结点
		return False
	if p is None:
		return False
	Next = p.Next
	p.Next = node
	node.Next = Next
	tmp = p.data
	p.data = node.data
	node.data = tmp

#方法二
def Insert_Node2(head,p,node):
	if node is None or node.data is None:
		return False
	if head is None or head.data != None:
		return False
	pre = head
	cur = head.Next
	while cur != None:
		if cur is p:
			pre.Next = node
			node.Next = cur
			break
		pre = cur
		cur = cur.Next
	if p is None:
		pre.Next = node
		node.Next = cur	
 
if __name__ == '__main__':
	head = LNode(None)
	cur = head
	for i in range(8):
		tmp = LNode(i)
		cur.Next = tmp
		cur = tmp
		if i == 7:
			p = tmp
	node = LNode(99)
	print('单链表为')
	print_List(head) 
	print('待插入结点的数据域为')
	if node != None:
		print(node.data)
	print('被插入的结点数据域为')
	if p != None:
		print(p.data)
	print('插入该结点后，单链表变为')
	Insert_Node(p,node)
	print_List(head)
	print('=====')
	
	print('---测试Insert_Node2函数---')
	head = LNode(None)
	cur = head
	for i in range(8):
		tmp = LNode(i)
		cur.Next = tmp
		cur = tmp
		if i == 7:
			p = tmp
	p = None
	node = LNode(99)
	print('单链表为')
	print_List(head) 
	print('待插入结点的数据域为')
	if node != None:
		print(node.data)
	print('被插入的结点数据域为')
	if p != None:
		print(p.data)
	print('插入该结点后，单链表变为')
	Insert_Node2(head,p,node)
	print_List(head)
	print('=====')
