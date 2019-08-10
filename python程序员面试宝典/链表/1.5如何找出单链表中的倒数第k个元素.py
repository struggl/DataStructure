'''
题目描述：找出单链表中的倒数第k个元素
输入样例：
1->2->3->4->5->6->7,k=3
输出：
5
#方法一：遍历一次单链表，得到有效结点个数n。然后把求倒数第k个元素转化为求顺数第n-k+1个元素,
指针从头结点开始，移动n-k+1次，即可得到倒数第k个元素
#方法二：快慢指针法。快指针从第k个有效结点开始，慢指针从第一个有效结点开始，两个指针同时以步长1向后遍历，
直到快指针到达尾结点,则慢指针所在结点即为倒数第k个元素
'''
#方法一实现
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
#实现方法一
def Find_Last_K(head,k):
	if type(k) != int or k <= 0:
		return False
	if head is None or head.data != None or head.Next is None:
		return False
	n = 0
	cur = head.Next
	while cur != None:
		n += 1
		cur = cur.Next
	if k > n:
		return None 
	seq_num = n - k + 1
	count = 0
	cur = head.Next
	while cur != None:
		count += 1
		if count == seq_num:
			return cur.data
		cur = cur.Next

#实现方法二
def Find_Last_K2(head,k):
	if type(k) != int or k <= 0:
		return False
	if head is None or head.data != None or head.Next is None:
		return False
	lowP = head.Next
	FastP = head
	count = 0
	while FastP != None:
		#循环体使得FastP到达第count个有效结点
		count += 1
		FastP = FastP.Next
		if count == k:
			break
	if FastP is None:
		#说明k值大于链表有效结点数目
		return None	
	#这里很容易错写成while FastP != None,一定要明确，遍历到尾结点即可。
	while FastP.Next != None:
		lowP = lowP.Next
		FastP = FastP.Next
	return lowP.data	

if __name__ == '__main__':
	values = [1,2,3,4,5,6,7]
	k = 3
	print('Testing value:'+str(values)+' and k = '+str(k))
	head = create_List(values)
	print_List(head)
	res = Find_Last_K2(head,k)
	print('函数返回结果：')
	print(res)
	print('=====')	
	
	values = [1,2,3,4,5,6,7]
	k = 1
	print('Testing value:'+str(values)+' and k = '+str(k))
	head = create_List(values)
	print_List(head)
	res = Find_Last_K2(head,k)
	print('函数返回结果：')
	print(res)
	print('=====')	

	values = [1,2,3,4,5,6,7]
	k = 7
	print('Testing value:'+str(values)+' and k = '+str(k))
	head = create_List(values)
	print_List(head)
	res = Find_Last_K2(head,k)
	print('函数返回结果：')
	print(res)
	print('=====')	

	values = [1,2,3,4,5,6,7]
	k = 8
	print('Testing value:'+str(values)+' and k = '+str(k))
	head = create_List(values)
	print_List(head)
	res = Find_Last_K2(head,k)
	print('函数返回结果：')
	print(res)
	print('=====')	
