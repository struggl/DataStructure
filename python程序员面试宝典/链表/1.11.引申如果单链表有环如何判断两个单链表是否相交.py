'''
判断两个单链表是否相交的整体方法论：
由于单链表每个有效结点能且只能指向一个其他结点，则如果两个单链表相交，从相交点往后的所有结点都相交。
a.因此如果一个单链表有环，另一个无环，必然不相交
b.如果两个单链表都无环，1.11已经解决
c.接下来需要讨论两个单链表都有环的情况(这也是本文件解决的情况)
显然，如果两个有环单链表相交，则二者必然共享环。因此
step1:先找到有环单链表head1的环入口p
step2:遍历有环单链表head2，若p不在head2内存空间中，则二者不相交，直接返回False,否则相交,进入step3
step3:把环入口点p看做尾结点，应用1.11方法三的思路去解决。

总体上可以有一个main函数，根据abc三种情况分别调用不同的函数或直接做出处理
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

def Is_Intersect(head1,head2):
	if head1 is None or head1.data != None or head1.Next is None:
		return False
	if head2 is None or head2.data != None or head2.Next is None:
		return False
	entry = Loop_Entry(head1)
	if entry == False:
		return False
	cur = head2.Next
	while cur != None:
		if cur is entry:
			break
		cur = cur.Next
	if cur is None:
		return False
	#记录entry分别是head1和head2的第几个有效结点
	cur1 = head1
	count1 = 0
	while cur1 is not entry:
		count1 += 1
		cur1 = cur1.Next
	count1 += 1
	
	cur2 = head2
	count2 = 0
	while cur2 is not entry:
		count2 += 1
		cur2 = cur2.Next
	count2 += 1
	
	#根据长度指定长短链
	if count1 <= count2:
		long_List = head2
		short_List = head1
		e = count2 - count1
	else:
		long_List = head1
		short_List = head2
		e = count1 - count2
	cur1 = short_List.Next
	cur2 = long_List.Next
	if e != 0:
		count = 0
		while cur2 != None:
			cur2 = cur2.Next
			count += 1
			if count == e:
				break

	while cur1 != None and cur2 != None:
		cur1 = cur1.Next
		cur2 = cur2.Next
		if cur1 is cur2:
			return cur1	
	

def Loop_Entry(head):
	if head is None or head.data != None or head.Next is None:
		return False
	lowP = head.Next
	FastP = head.Next
	while FastP != None and FastP.Next != None:
		lowP = lowP.Next
		FastP = FastP.Next.Next
		if lowP is FastP:
			break
	if FastP is None or FastP.Next is None:
		return False
	#仅当链表有环，才能进入以下代码
	lowP = head.Next
	while FastP != lowP:
		#注意！此时快慢指针均以步长1向后遍历!
		lowP = lowP.Next
		FastP = FastP.Next
	return FastP

if __name__ == '__main__':
	print('=====测试两个单链表无环的情况(无环应当返回False)=====')
	common_List = create_List(['链表','从这里','开始','相交'])
	head1 = create_List([1,2,3,4])
	cur = head1
	while cur.Next != None:
		cur = cur.Next
	cur.Next = common_List.Next

	head2 = create_List([7,8])
	cur = head2
	while cur.Next != None:
		cur = cur.Next
	cur.Next = common_List.Next
	print('head1链表为')
	print_List(head1)
	print('head2链表为')
	print_List(head2)
	
	print('\n调用Is_Intersect函数得到：')
	res = Is_Intersect(head1,head2)
	if res != False:
		print(res.data)
	else:
		print(res)
	print('=====')
	
	print('=====测试两个单链表有环的情况=====')
	common_List = create_List(['链表','从这里','开始','相交'])
	head1 = LNode(None)
	cur = head1
	for v in range(3):
		tmp = LNode(v)
		cur.Next = tmp
		cur = tmp
	cur.Next = common_List.Next
	cur.Next.Next.Next.Next.Next = cur.Next.Next

	head2 = LNode(None)
	cur = head2
	for v in range(4):
		tmp = LNode(v)
		cur.Next = tmp
		cur = tmp
	cur.Next = common_List.Next
	cur.Next.Next.Next.Next.Next = cur.Next.Next
		
	print('\n调用Is_Intersect函数得到：')
	res = Is_Intersect(head1,head2)
	if res != False:
		print(res.data)
	else:
		print(res)
	print('=====')
	
	
		
	
