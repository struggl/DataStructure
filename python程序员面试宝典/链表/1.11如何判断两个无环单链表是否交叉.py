'''
问题描述：如何判断两个无环单链表是否存在交叉，即完全重合的部分。如果相交，找出相交处的结点。
问题理解：由于每个结点都只能指向一个结点，因此从相交点开始，后面的链表都是相交的部分。


方法一：哈希法，把第一个链表结点存到哈希表中，遍历第二个链表结点，看是否已经在哈希表上,第一个出现在哈希表上的即为相交点，若没有出现
在哈希表上，则说明两个单链表不相交
时间：O(n1+n2)
空间：O(n1)

方法二：把两个单链表相连，即第一个链表的尾结点指向第二个链表的第一个有效结点。如果两个链表相交，则会构成环。环入口点即为相交点。
若不存在环，则说明不存在相交点。拼接以后，直接用1.6.引申中的Loop_Entry函数即可
step1:初始化快慢指针为第一个有效结点，慢指针每次走1步，快指针走2步，得到相遇点
step2:慢指针重新赋值为第一个有效结点(此时快指针指向相遇点),此时快慢指针均步长为1向后遍历，直到相遇。
返回第一个相遇点，即为环入口
时间：O(n1+n2)
空间：O(1)

方法三：尾结点法。根据问题理解所揭示的事实，如果两个链表相交，则最后一个有效结点一定是同一个内存，可以根据这一点判断是否相交。
如果相交，则接下来要找到相交点。假设两个单链表有效结点数分别为n1，n2.慢结点从短链表头结点开始，快结点从长链表的第|n1-n2|个有效结点开始，
快慢指针同时以步长1向后遍历，第一个相同内存的点即为相交点。
时间：O(n1+n2)
空间：O(1)

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

#方法一实现
def IsIntersect(head1,head2):
	if head1 is None or head1.data != None or head1.Next is None:
		return False
	if head2 is None or head2.data != None or head2.Next is None:
		return False	
	hashTable = set()
	cur = head1.Next
	while cur != None:
		hashTable.add(cur)
		cur = cur.Next
	cur = head2.Next
	while cur != None:
		if cur in hashTable:
			return cur
		cur = cur.Next
	return False

#方法二实现
def IsIntersect2(head1,head2):
	if head1 is None or head1.data != None or head1.Next is None:
		return False
	if head2 is None or head2.data != None or head2.Next is None:
		return False	
	cur = head1.Next
	while cur.Next != None:
		cur = cur.Next
	cur.Next = head2.Next
	#此时head1与head2已连接，头结点为head1
	res = Loop_Entry(head1)
	return res
	

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

#方法三实现
def IsIntersect3(head1,head2):
	if head1 is None or head1.data != None or head1.Next is None:
		return False
	if head2 is None or head2.data != None or head2.Next is None:
		return False	

	cur = head1
	count1 = 0
	while cur.Next != None:
		cur = cur.Next
		count1 += 1
	end1 = cur

	cur = head2
	count2 = 0
	while cur.Next != None:
		cur = cur.Next
		count2 += 1
	end2 = cur

	if end1 is not end2:
		return False

	if count1 <= count2:
		shot_List = head1
		long_List = head2
		e = count2 - count1
	else:
		shot_List = head2
		long_List = head1
		e = count1 - count2

	#初始化遍历起始点，慢指针从短链头结点开始，快指针从长链第e个有效结点开始
	cur1 = shot_List
	cur2 = long_List
	if e != 0:
		count = 0
		while cur2.Next != None:
			cur2 = cur2.Next
			count += 1
			if count == e:
				break
		
	while cur1 != None and cur2 != None:
		cur1 = cur1.Next
		cur2 = cur2.Next
		if cur1 is cur2:
			return cur1
	
			
		

if __name__ == '__main__':
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
	
	print('\n调用IsIntersect3函数得到：')
	res = IsIntersect3(head1,head2)
	if res != False:
		print(res.data)
	else:
		print(res)
	print('=====')

