'''
题目：给定一个带头结点的单链表，将其逆序。
输入样例
head->1->2->3->None
输出
head->3->2->1->None
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
	tmp_head = head
	for v in values:
		cur_node = LNode(v)
		tmp_head.Next = cur_node
		tmp_head = cur_node
	return head

#打印链表
def print_List(head):
	if head is None:
		print('参数非法')
		return
	if head.data != None:
		print('给定的单链表不带头结点')
		return 
	if head.data is None and head.Next is None:
		print('链表仅包含一个头结点')
		return
	cur = head.Next
	while cur != None:
		print(cur.data)
		cur = cur.Next
#方法一：递归
#对于1->2->3->...->n,子问题为2->3->...->n，子问题递归解决得到的逆序链表，在与head做对应的合并
def Reverse_List(head):
	'''
	#啰嗦版参数边界检测
	if head is None:
		print('参数非法')
		return False
	if head.data != None:
		print('输入的单链表必须有头结点')
		return False
	if head.Next is None:
		print('输入的单链表不能为空链表')
		return head
	if head.Next.Next is None:
		print('输入的单链表仅有一个有效结点，无需逆序')
		return head
	'''
	#简洁版参数边界检测
	if head is None or head.data != None:
		return False
	if head.Next is None or head.Next.Next is None:
		return head
	#调用递归函数进行逆序
	res = reverse_List(head.Next)
	head.Next = res
	return head
'''
递归法实现逆序的思路：
以单链表1->2->3-4->None为例进行分析，记录1结点为head，子问题为2->3-4->None的逆序问题。逻辑上这个子问题解决结果为
4->3->2->None(暂且不管子问题具体如何解决)。记录4结点为res。显然，下一步我们需要把1结点插入到2的后面，并令1结点为
尾结点。此时便有一个问题，那就是如何索引到2这个结点。答案是使用head.Next。理由如下：
显然子问题的解决过程中，各结点指针域的修改，不会涉及head的指针域，因此，head.Next仍然指向2这个结点。于是有代码：
head.Next.Next = head
head.Next = None
在复习这个解法的过程中，曾踩过用res.Next来索引子问题解决方案最后一个有效结点(这里即2结点)的傻坑。显然，res.Next在这里
指向3结点而非2结点。逻辑上，随着递归的逐步返回，res.Next与实际需要的最后一个有效结点，中间会间隔越来越多结点。而因为逻辑上存
在这样的漏洞，递归也不会正常地返回那些中间结点，因此这样造成的后果就是，逆序算法会漏掉大量结点，逆序完成后，链表只剩下两个有效结点。
'''


def reverse_List(head):
	#能进入此函数的单链表必须为不带头结点的非空链表
	#递归终止返回
	if head.Next is None:
		#只有一个有效结点
		return head	
	#子问题划分与递归地解决子问题
	res = reverse_List(head.Next)
	#子问题结果合并
	head.Next.Next = head
	head.Next = None
	return res

#方法二：就地逆序
#对于1->2->3->...->n,先变为1<-2->3->...->n,再变为1<-2<-3->...->n,最终会变为1<-2<-3<-...<-n，使头结点指向最终的第n个结点即可。
#核心技巧是链表的遍历与各结点的指针域更新
#容易犯错的地方在于更新指针域时，明确啥情况需要存储结点:当一个结点有后继结点时，如果要把这个结点指向它的前驱，则应当事先保存他的后继。
#简记为:要指向前驱，先保存后继,注意头尾结点特性。
def Reverse_List2(head):	
	if head is None:
		print('参数不能为None')
		return False
	if head.data != None:
		print('输入链表应有头结点')
		return False
	if head.Next is None:
		print('输入链表为空链表')		
		return head
	if head.Next.Next is None:
		print('输入链表仅有一个有效结点,无需逆序')
		return head
	#目前发现的最简单写法
	pre = None
	cur = head.Next
	while cur != None:
		Next = cur.Next
		cur.Next = pre
		pre = cur
		cur = Next
	head.Next = pre
	return head
	'''若从第一个有效结点开始迭代，循环内更新cur立刻将它指向pre，这意味着循环结束时，链表已逆序完毕，只差一个头结点。
	pre = head.Next
	cur = pre.Next
	pre.Next = None
	Next = cur.Next
	cur.Next = pre
	while Next != None:
		pre = cur
		cur = Next
		Next = cur.Next
		cur.Next = pre	
	head.Next = cur
	return head	
	'''
	'''
	#若从None结点开始迭代，循环内更新完cur以后，下一步才会把它指向pre，这意味着循环结束时，还要再补上cur的指针域修改
	pre = None
	cur = head.Next
	Next = cur.Next
	while Next != None:
		cur.Next = pre
		pre = cur
		cur = Next
		Next = cur.Next
	cur.Next = pre
	head.Next = cur
	return head
	'''	

#方法三：插入法
#遍历每个有效结点，把有效结点添加到头结点后面
#例如，head->1->2->3->None先变成head->1->2->3->None然后变成head->2->1->3->None，最后变成head->3->2->1->None
#难点类似方法二
def Reverse_List3(head):
	if head is None:
		print('参数不能为空')
		return False
	if head.data != None:
		print('输入链表应有头结点')
		return False
	if head.Next is None:
		print('输入链表为空链表')
		return head
	if head.Next.Next is None:
		print('输入链表仅有一个有效结点，无需逆序')
		return head
	cur = head.Next.Next
	head.Next.Next = None
	while cur != None:
		Next = cur.Next
		#以下两句代码次序不可乱！
		cur.Next = head.Next
		head.Next = cur
		cur = Next
	return head

if __name__ == '__main__':
	#values = ['体育','NBA','詹姆斯','杜兰特',1]
	values = ['体育','NBA','詹姆斯']
	print('Testing values:'+str(values))
	print('根据此values创建的单链表如下:')
	head = create_List(values)
	print_List(head)
	print('')
	print('逆序后单链表如下：')
	head = Reverse_List3(head)
	print_List(head)	
