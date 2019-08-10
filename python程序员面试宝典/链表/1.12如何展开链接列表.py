'''
题目描述：给定一个有序链表，其中每个结点也表示一个有序链表，结点包含两个类型的指针
(1)指向主链表中下一个结点的指针
(2)指向此结点头的链表
不论是从左到右的主链表还是每个从上到下的链表都已经被升序排序
要求实现一个函数将这个有序链表扁平化为单个链表，扁平化的链表也应该被排序

#方法思路：参考归并排序

此脚本中的链表无论从左到右还是从上到下，都不用头结点(事实上对于单链表如果使用递归，往往都是无头结点比较好处理)
'''
class LNode2(object):
	def __init__(self,x):
		self.data = x
		self.down_Next = None
		self.right_Next = None


def create_List2(*values_list):
	head = LNode2(None)
	cur = head
	for values in values_list:
		tmp = create_down_list(values)
		cur.right_Next = tmp
		cur = cur.right_Next
	return head.right_Next

def create_down_list(values):
	head = LNode2(None)
	cur = head
	for v in values:
		tmp = LNode2(v)
		cur.down_Next = tmp
		cur = tmp
	return head.down_Next

def print_List2(head):
	if head is None or head.data is None:
		return False
	cur = head
	while cur != None:
		print_down_list(cur)
		print('-----')
		cur = cur.right_Next

def print_down_list(node):
	if node is None or node.data is None:
		return False
	cur = node
	while cur != None:
		print(cur.data)
		cur = cur.down_Next

def flatten(head):
	if head.right_Next is None:
		return head
	res = flatten(head.right_Next)
	return merge(head,res)

def merge(node1,node2):
	#给定的两个参数是两个从上到下升序的无头结点单链表
	#返回的升序合并单链表也应当是从上到下，因为merge会被多次调用，如果返回从左到右，上层调用必然报错
	if node1 is None or node1.data is None:
		return False
	if node2 is None or node2.data is None:
		return False
	cur1 = node1
	cur2 = node2
	head = LNode2(None)
	cur = head
	while cur1 != None and cur2 != None:
		if cur1.data <= cur2.data:
			tmp = LNode2(cur1.data)
			cur.down_Next = tmp
			cur = cur.down_Next
			cur1 = cur1.down_Next
		else:
			tmp = LNode2(cur2.data)
			cur.down_Next = tmp
			cur = cur.down_Next
			cur2 = cur2.down_Next
	while cur1 != None:
		tmp = LNode2(cur1.data)
		cur.down_Next = tmp
		cur = cur.down_Next
		cur1 = cur1.down_Next
	while cur2 != None:
		tmp = LNode2(cur2.data)
		cur.down_Next = tmp
		cur = cur.down_Next
		cur2 = cur2.down_Next
	return head.down_Next		
			







if __name__ == '__main__':
	head = create_List2([3,6,8,31],[11,21],[15,22,50],[30,39,40,55])
	#print_down_list(head.right_Next)
	print_List2(head)
	head = flatten(head)
	print_down_list(head)
