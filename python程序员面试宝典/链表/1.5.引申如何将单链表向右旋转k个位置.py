'''
题目描述：给定的单链表1->2->3->4->5->6->7,k=3,则旋转后单链表变为
5->6->7->1->2->3->4

思路：快慢指针找到倒数第k个元素及其前驱，把前驱指向None，把快指针(此时到达尾结点)指向head.Next,令头结点指向慢指针,
返回head
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
#实现单链表旋转:把后面k个元素移到前面
#思路：快慢指针找到倒数第k个元素及其前驱，把前驱指向None，把快指针(此时到达尾结点)指向head.Next,令头结点指向慢指针,
#返回head
def RotateK(head,k):
	if head is None or head.data != None or head.Next is None:
		return False
	if type(k) != int or k <= 0:
		return False
	lowP = head.Next
	pre_lowP = head
	FastP = head
	count = 0
	while FastP != None:
		FastP = FastP.Next
		count += 1
		if count == k:
			break
	if FastP is None:
		#说明k大于单链表有效结点个数
		return False
	while FastP.Next != None:
		pre_lowP = lowP	
		lowP = lowP.Next
		FastP = FastP.Next
	pre_lowP.Next = None
	FastP.Next = head.Next
	head.Next = lowP
	return head


if __name__ == '__main__':
	values = [1,2,3,4,5,6,7]
	k = 3
	print('Testing values:' + str(values)+ ' and k = ' + str(k))
	head = create_List(values)
	print_List(head)
	print('单链表旋转后')
	head = RotateK(head,k)
	print_List(head)
	print('=====')
