'''
题目描述：给定两个单链表，链表的每个结点代表一位数(第一个有效结点数据域代表个位数)，计算两个数的和。
输入样例：
3->1->5
5->9->2
输出：
8->0->8
'''
#链表的创建和输出
class LNode(object):
	def __init__(self,x):
		self.data = x
		self.Next = None

#创建链表(带头结点)
def create_List(values):
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

#方法一：整数相加法
#先遍历两个链表，分别求出对应的整数值，然后计算二者之和,最后把和转化为单链表的形式(不提倡，仅做练习)
def add(head1,head2):
	if head1 is None or head1.data != None or head1.Next is None:
		return False
	if head2 is None or head2.data != None or head2.Next is None:
		return False
	data1 = get_int_from(head1.Next)
	data2 = get_int_from(head2.Next)
	Sum = data1 + data2
	values = get_numbers_from(Sum)
        #记住，第一个有效结点表示个位，因此要倒过来构造单链表
	values.reverse()	
	head = create_List(values)
	return head	

def get_int_from(head):
	#输入为不带头结点的非空单链表,将该链表转为整数(第一个有效结点数据域为个位)
	cur = head
	multi = 1
	head_int = 0
	while cur != None:
		tmp = cur.data * multi
		head_int += tmp
		cur = cur.Next
		multi *= 10
	return head_int

def get_numbers_from(Sum):
	#方法一：将数字转成字符串，取出每一位即可
	str_Sum = str(Sum)
	values = []
	for i in range(len(str_Sum)):
		values.append(str_Sum[i])
	return values	
	

####方法二：链表直接相加(推荐)
def add2(head1,head2):
	if head1 is None or head1.data != None or head1.Next is None:
		return False
	if head2 is None or head2.data != None or head2.Next is None:
		return False
	head = LNode(None)
	cur = head
	cur1 = head1.Next 
	cur2 = head2.Next
	#表示进位
	c = 0
	while cur1 != None and cur2!= None:
		tmp = cur1.data + cur2.data + c
		if tmp < 10:
			tmp_node = LNode(tmp)
			c = 0
		else:
			tmp_node = LNode(tmp - 10)
			c = 1
		cur.Next = tmp_node
		cur = cur.Next
		cur1 = cur1.Next
		cur2 = cur2.Next
	while cur1 != None:
		tmp = cur1.data + c
		if tmp < 10:
			tmp_node = LNode(tmp)
			c = 0
		else:
			tmp_node = LNode(tmp -10)
			c = 1
		cur.Next = tmp_node
		cur = cur.Next
		cur1 = cur1.Next	
	while cur2 != None:
		tmp = cur2.data + c
		if tmp < 10:
			tmp_node = LNode(tmp)
			c = 0
		else:
			tmp_node = LNode(tmp -10)
			c = 1
		cur.Next = tmp_node
		cur = cur.Next
		cur2 = cur2.Next
	#下面这一步很容易漏掉。。。
	if c > 0:
		tmp = LNode(c)
		cur.Next = tmp
	return head
if __name__ == '__main__':
	values1 = [3,1,5]
	values2 = [5,9,2]
	print('Testing values1:'+str(values1)+' and values2:'+str(values2))
	head1 = create_List(values1)
	head2 = create_List(values2)
	print('values1:')
	print_List(head1)
	print('values2:')
	print_List(head2)
	Sum = add(head1,head2)
	print('两个单链表数据域之和为')
	print_List(Sum)
	print('=====')
	values1 = [3,1,5,4]
	values2 = [5,9,2]
	print('Testing values1:'+str(values1)+' and values2:'+str(values2))
	head1 = create_List(values1)
	head2 = create_List(values2)
	print('values1:')
	print_List(head1)
	print('values2:')
	print_List(head2)
	Sum = add(head1,head2)
	print('两个单链表数据域之和为')
	print_List(Sum)
	print('=====')
	values1 = [3,1,5,4]
	values2 = [5,9,2,7,9]
	print('Testing values1:'+str(values1)+' and values2:'+str(values2))
	head1 = create_List(values1)
	head2 = create_List(values2)
	print('values1:')
	print_List(head1)
	print('values2:')
	print_List(head2)
	Sum = add2(head1,head2)
	print('两个单链表数据域之和为')
	print_List(Sum)
	print('=====')
