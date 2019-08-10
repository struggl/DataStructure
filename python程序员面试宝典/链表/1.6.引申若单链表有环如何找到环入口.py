'''
问题描述：如果单链表存在环，那么如何找到环的入口
思路分析：
step1:初始化快慢指针为第一个有效结点，慢指针每次走1步，快指针走2步，得到相遇点
step2:慢指针重新赋值为第一个有效结点(此时快指针指向相遇点),此时快慢指针均步长为1向后遍历，直到相遇。
返回第一个相遇点，即为环入口
假设链表长为L，起点到环入口距离为a，环入口到相遇点距离为x,环长设为r，则显然有a+x+mr = nr,其中n、m分别是快慢指针绕环的圈数
于是有a+x = (n-m)r,由于n和m都是正整数，因而可令n-m为整数c，即a+x = cr
又有r = L - a,于是a+x = (c-1)r + L - a,于是有a = (c-1)r + (L-a-x)
这个公式意思是 链表头到环入口距离 = (c-1)倍环长 + 环入口到相遇点距离
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
	values = ['体育','NBA','詹姆斯','杜兰特',1,2]
	head = LNode(None)
	cur = head
	for v in values:
		tmp = LNode(v)
		cur.Next = tmp
		cur = tmp
	cur.Next = head.Next.Next
	res = Loop_Entry(head)
	if res != False:
		print(res.data)
	else:
		print(res)
	print('=====')

	head = create_List(values)
	res = Loop_Entry(head)
	if res != False:
		print(res.data)
	else:
		print(res)
	print('=====')
