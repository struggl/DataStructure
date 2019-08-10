'''
题目描述：已知两个链表元素升序排列，合并这两个链表，使之仍然升序
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

def merge_List(head1,head2):
	if head1 is None or head1.data != None:
		return False
	if head2 is None or head2.data!= None:
		return False
	head = LNode(None)
	cur1 = head1.Next
	cur2 = head2.Next
	cur = head
	while cur1 != None and cur2 != None:
		if cur1.data <= cur2.data:
			cur.Next = cur1
			cur1 = cur1.Next
			cur = cur.Next
		else:
			cur.Next = cur2
			cur2 = cur2.Next
			cur = cur.Next
	while cur1 != None:
		cur.Next = cur1
		cur1 = cur1.Next
		cur = cur.Next
	while cur2 != None:
		cur.Next = cur2
		cur2 = cur2.Next
		cur = cur.Next
	cur.Next = None
	return head

if __name__ == '__main__':
	values1 = [1,2,3]
	values2 = [2,3,4,5]
	print('Testing values1:'+str(values1))
	head1 = create_List(values1)
	print_List(head1)
	print('and values2:'+str(values2))
	head2 = create_List(values2)
	print_List(head2)
	print('合并后，链表为')
	head = merge_List(head1,head2)
	print_List(head)
	print('=====')

	values1 = [4,5,6]
	values2 = [1,2,3]
	print('Testing values1:'+str(values1))
	head1 = create_List(values1)
	print_List(head1)
	print('and values2:'+str(values2))
	head2 = create_List(values2)
	print_List(head2)
	print('合并后，链表为')
	head = merge_List(head1,head2)
	print_List(head)
	print('=====')

	values1 = [1,2,3]
	values2 = [4,5,6]
	print('Testing values1:'+str(values1))
	head1 = create_List(values1)
	print_List(head1)
	print('and values2:'+str(values2))
	head2 = create_List(values2)
	print_List(head2)
	print('合并后，链表为')
	head = merge_List(head1,head2)
	print_List(head)
	print('=====')

	values1 = None
	values2 = [4,5,6]
	print('Testing values1:'+str(values1))
	head1 = LNode(values1)
	print('and values2:'+str(values2))
	head2 = create_List(values2)
	print_List(head2)
	print('合并后，链表为')
	head = merge_List(head1,head2)
	print_List(head)
	print('=====')

	values1 = [1,2,3]
	values2 = None
	print('Testing values1:'+str(values1))
	head1 = create_List(values1)
	print_List(head1)
	print('and values2:'+str(values2))
	head2 = LNode(values2)
	print('合并后，链表为')
	head = merge_List(head1,head2)
	print_List(head)
	print('=====')
