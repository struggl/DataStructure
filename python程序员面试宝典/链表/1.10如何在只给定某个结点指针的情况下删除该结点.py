'''
题目描述：
假设给定链表1->2->3->4->5->6->7中指向第5个元素的指针，要求把结点5删除，得到1->2->3->4->6->7
方法一：<<py宝典>>提供的思路。它认为这题无法找到给定结点的前驱，因此只能通过交换值的思路来实现。即把后面有效结点的值复制到当前结点，
通过剔除后继结点的方式来得到剔除给定结点的等价结果。缺陷很明显，如果给定结点是最后一个有效结点，则无法剔除
优点是时间空间复杂度都为O(1)
方法二：个人认为是可以找到前驱结点的，如果给定结点为None,则无需剔除。否则，只需要用pre = head和cur = pre.Next遍历一次单链表，
当cur is 给定结点时，把pre指向cur.Next即可,如果cur遍历到None仍然无法is给定结点，则说明给定结点不在这个单链表中，无需删除，返回原链表即可。
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

#方法1交换值法实现
def RemoveNode(head,node):
	if head is None or head.data != None or head.Next is None:
		return False
	if node is None or node.Next is None:
		return head
	Next = node.Next
	node.data = Next.data
	node.Next = Next.Next
	return head
	

#方法2实现(个人觉得更好)
def RemoveNode2(head,node):
	if head is None or head.data != None or head.Next is None:
		return False
	if node is None:
		return head
	pre = head
	cur = head.Next
	while cur != None:
		if cur is node:
			pre.Next = cur.Next
			return head
		pre = cur
		cur = cur.Next
	#到达这里说明node指向的内存不在单链表中
	return head



if __name__ == '__main__':
	head = LNode(None)
	cur = head
	for i in range(8):
		tmp = LNode(i)
		cur.Next = tmp
		cur = tmp
		if i == 7:
			p = tmp
	#p = None
	print('单链表为')
	print_List(head) 
	print('待删除结点的数据域为')
	if p != None:
		print(p.data)
	print('删除该结点后，单链表变为')
	head = RemoveNode2(head,p)
	print_List(head)
	print('=====')
