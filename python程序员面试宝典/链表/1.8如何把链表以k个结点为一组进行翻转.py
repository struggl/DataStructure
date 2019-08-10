'''
题目描述：如何把链表以K个结点为一组进行翻转
方法思路：
完全对比1.7把单链表相邻元素翻转去写即可。
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

def Reverse(head):
	#输入head为不带头结点的非空单链表(由于Reverse_K的k至少为2，所以此链表长度至少为2)
	pre = head
	cur = pre.Next
	while cur != None:
		Next = cur.Next
		cur.Next = pre
		pre = cur
		cur = Next

def Find_Next_K(node,K):
	if node is None:
		return None
	count = 0
	cur = node
	while cur.Next != None:
		cur = cur.Next
		count += 1
		if count == K:
			return cur
	#若执行到这里，说明node后面没有K个有效元素了
	return None

def Reverse_K(head,K):
	if head is None or head.data != None or head.Next is None:
		return False
	if type(K) != int or K <= 1:
		return False
	pre = head.Next
	pre_pre = head
	cur = Find_Next_K(head,K)
	if cur is None:
		#说明单链表不满K个有效结点，无需翻转
		return head
	while cur != None and cur.Next != None:
		pre_pre.Next = cur
		Next = cur.Next
		cur.Next = None
		Reverse(pre)
		pre.Next = Next
		#迭代
		pre_pre = pre
		pre = Next
		cur = Find_Next_K(Next,K-1)
	if cur is None:
		return head
	pre_pre.Next = cur
	Next = cur.Next
	cur.Next = None
	Reverse(pre)
	pre.Next = Next
	return head	
		
		
	

if __name__ == '__main__':
	values = [1]
	K = 2
	print('Testing values:'+str(values)+' and K = ' + str(K))
	head = create_List(values)
	print_List(head)
	print('翻转{}个结点后，单链表为'.format(K))
	head = Reverse_K(head,K)
	print_List(head)
	print('=====')

	values = [1,2]
	K = 2
	print('Testing values:'+str(values)+' and K = ' + str(K))
	head = create_List(values)
	print_List(head)
	print('翻转{}个结点后，单链表为'.format(K))
	head = Reverse_K(head,K)
	print_List(head)
	print('=====')

	values = [1,2,3,4,5,6,7]
	K = 2
	print('Testing values:'+str(values)+' and K = ' + str(K))
	head = create_List(values)
	print_List(head)
	print('翻转{}个结点后，单链表为'.format(K))
	head = Reverse_K(head,K)
	print_List(head)
	print('=====')

	values = [1,2,3,4,5,6,7]
	K = 3
	print('Testing values:'+str(values)+' and K = ' + str(K))
	head = create_List(values)
	print_List(head)
	print('翻转{}个结点后，单链表为'.format(K))
	head = Reverse_K(head,K)
	print_List(head)
	print('=====')

	values = [1,2,3]
	K = 4
	print('Testing values:'+str(values)+' and K = ' + str(K))
	head = create_List(values)
	print_List(head)
	print('翻转{}个结点后，单链表为'.format(K))
	head = Reverse_K(head,K)
	print_List(head)
	print('=====')

	values = [1,2,3,4,5,6]
	K = 4
	print('Testing values:'+str(values)+' and K = ' + str(K))
	head = create_List(values)
	print_List(head)
	print('翻转{}个结点后，单链表为'.format(K))
	head = Reverse_K(head,K)
	print_List(head)
	print('=====')

	values = [1,2,3,4]
	K = 4
	print('Testing values:'+str(values)+' and K = ' + str(K))
	head = create_List(values)
	print_List(head)
	print('翻转{}个结点后，单链表为'.format(K))
	head = Reverse_K(head,K)
	print_List(head)
	print('=====')

	values = [1,2,3,4,5,6,7]
	K = 4
	print('Testing values:'+str(values)+' and K = ' + str(K))
	head = create_List(values)
	print_List(head)
	print('翻转{}个结点后，单链表为'.format(K))
	head = Reverse_K(head,K)
	print_List(head)
	print('=====')
	
	values = [1,2,3,4,5,6,7,8]
	K = 4
	print('Testing values:'+str(values)+' and K = ' + str(K))
	head = create_List(values)
	print_List(head)
	print('翻转{}个结点后，单链表为'.format(K))
	head = Reverse_K(head,K)
	print_List(head)
	print('=====')
