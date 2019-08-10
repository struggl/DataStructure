'''
题目描述：给定链表L_0->L_1->L_2->...->L_(n-1)->L_n,把链表重排序为
L_0->L_n->L_(n-1)->L_2->L_(n-2)...
要求：
(1)在原来链表的基础上进行排序，即不能申请新的结点
(2)只能修改结点的Next域，不能修改数据域。
'''
class LNode(object):
	def __init__(self,x):
		self.data = x
		self.Next = None

def create_List(values):
	if type(values) != list:
		return False
	head = LNode(None)
	if values is None:
		return head
	cur = head
	for v in values:
		tmp = LNode(v)
		cur.Next = tmp
		cur = tmp
	return head

def print_List(head):
	if head is None or head.data != None or head.Next is None:
		return False
	cur = head.Next
	while cur != None:
		print(cur.data)
		cur = cur.Next

def reverse_List(head):
	'''
	Args:
		head:不带头结点的非空单链表
	Return
		逆序后的链表
	'''
	if head.Next is None:
		return head
	res = reverse_List(head.Next)
	head.Next.Next = head
	head.Next = None
	return res
'''
方法思路：先找到单链表的中间结点，把单链表分成左右子链表，再把右边子链表逆序，然后把左子链与逆序后的右子链拼接。
最后合并
'''	
def Rerank_List(head):
	if head is None or head.data != None or head.Next is None:
		return False
	if head.Next.Next is None or head.Next.Next.Next is None:
		return head
	low_point = head.Next
	fast_point = head.Next.Next
	while fast_point != None and fast_point.Next != None:
		low_point = low_point.Next
		fast_point = fast_point.Next.Next
	right = reverse_List(low_point.Next)
	low_point.Next = right
	#此时head单链表的后半部分已经逆序
	res = rerank(head.Next,low_point)
	head.Next = res
	return head
	'''最开始的实现思路：分奇数链和偶数链分别合并，写完后发现其实两种情况下可以用同一份代码，即rerank函数
	if fast_point is None:
		#说明单链表有奇数个有效结点，low_point结点即为中间结点
		right = reverse_List(low_point.Next)
		low_point.Next = right
		#此时head单链表的后半部分已经逆序
		res = odd_rerank(head.Next,low_point)
		head.Next = res
		return head
	if fast_point.Next is None:
		#说明单链表有偶数个有效结点，low_point结点及其下一个结点为中间结点
		right = reverse_List(low_point.Next)
		low_point.Next = right
		#此时head单链表的后半部分已经逆序
		res = even_rerank(head.Next,low_point)
		head.Next = res
		return head
	'''
def rerank(head,mid):
	'''
	Args:
		head:单链表的第一个有效结点
		mid:奇数单链表的中间结点或偶数单链表的第一个中间结点
	'''
	left_cur = head
	right_cur = mid.Next
	while left_cur != mid:
		left_Next = left_cur.Next
		right_Next = right_cur.Next
		left_cur.Next = right_cur
		right_cur.Next = left_Next
		left_cur = left_Next
		right_cur = right_Next
	mid.Next = right_cur
	return head

if __name__ == '__main__':
	values = [1,2,3,4]
	print('Testing values:'+str(values))
	head = create_List(values)
	print('从头到尾输出单链表：')
	print_List(head)
	print('重排序后，单链表为：')
	head = Rerank_List(head)
	print_List(head)
	print('=====')

	values = [1,2,3,4,5]
	print('Testing values:'+str(values))
	head = create_List(values)
	print('从头到尾输出单链表：')
	print_List(head)
	print('重排序后，单链表为：')
	head = Rerank_List(head)
	print_List(head)
	print('=====')
		
	values = [1]
	print('Testing values:'+str(values))
	head = create_List(values)
	print('从头到尾输出单链表：')
	print_List(head)
	print('重排序后，单链表为：')
	head = Rerank_List(head)
	print_List(head)
	print('=====')

	values = [1,2]
	print('Testing values:'+str(values))
	head = create_List(values)
	print('从头到尾输出单链表：')
	print_List(head)
	print('重排序后，单链表为：')
	head = Rerank_List(head)
	print_List(head)
	print('=====')
