'''
题目描述：把链表相邻元素翻转，例如给定链表为1->2->3->4->5->6->7，翻转后变为
2->1->4->3->6->5->7
方法一：就地逆序
方法二：交换相邻元素数据域(不提倡)
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

#方法一就地逆序实现
def Reverse(head):
	if head is None or head.data != None or head.Next is None:
		return False
	if head.Next.Next is None:
		return head
	pre = head.Next
	cur = pre.Next
	pre_pre = head
	while cur != None and cur.Next != None:
		'''
		pre_pre.Next = cur极其容易被忽视掉！
		以1->2->3->4->5->None为例，一开始pre向1，cur指向2，由于cur满足循环条件，于是链表头几个有效结点变为
		2->1->3,但是此时head依然指向结点1，最终返回head时，这里就漏掉了结点2。
		接着迭代，pre指向3，cur指向4，cur满足循环条件，于是3->4->5变为了4->3->5.我们所需要的结果是2->1->4->3->5，
		但是这里结点1并没有指向结点4，而是仍然指向结点3！于是最终返回head时，又漏掉了结点4.最终的结果就是，翻转以后
		只剩下了奇数序号的结点1->3->5->7.
		'''
		pre_pre.Next = cur
		Next = cur.Next
		pre.Next = Next
		cur.Next = pre
		#迭代
		pre_pre = pre
		pre = Next
		#循环准入条件cur.Next != None保证了以下pre.Next不会出bug
		cur = pre.Next
	if cur is None:
		return head
	#if cur.Next is None:
	pre_pre.Next = cur
	pre.Next = cur.Next
	cur.Next = pre
	return head
		 
#方法二交换值实现
def Reverse2(head):
	if head is None or head.data != None or head.Next is None:
		return False
	if head.Next.Next is None:
		return head
	pre = head.Next
	cur = pre.Next
	while cur != None and cur.Next != None:
		tmp = pre.data
		pre.data = cur.data
		cur.data = tmp
		pre = cur.Next
		cur = pre.Next
	if cur is None:
		return head
	tmp = pre.data
	pre.data = cur.data
	cur.data = tmp
	return head	

if __name__ == '__main__':
	values = [1,2,3,4,5,6,7]
	print('Testing values:'+str(values))
	head = create_List(values)
	print_List(head)
	print('翻转后，单链表为')
	head = Reverse2(head)
	print_List(head)
	print('=====')

	values = [1,2,3,4,5,6,7,8]
	print('Testing values:'+str(values))
	head = create_List(values)
	print_List(head)
	print('翻转后，单链表为')
	head = Reverse2(head)
	print_List(head)
	print('=====')
