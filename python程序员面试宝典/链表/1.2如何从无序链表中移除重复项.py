'''
题目描述：给定一个没有排序的带头结点单链表，去除其重复项，并保留原顺序
输入样例：
head->1->3->1->5->5->5->7->None
输出：
head->1->3->5->7->None
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

#方法一：hash法(空间换时间的策略)
def removeDup(head):
	if head is None or head.data != None or head.Next is None:
		return False
	if head.Next.Next is None:
		return head
	pre = head
	cur = head.Next
	Next = cur.Next
	hashTable = set()
	while Next != None:
		if cur.data in hashTable:
			'''
			#有问题的写法,
			#原因在于这里的pre应当是非重复子链的最后一个结点
			#当cur已经重复，这个时候pre = cur会导致pre指向已经被判定有重复的结点,从而导致去重出bug
			pre.Next = Next
			pre = cur
			cur = Next
			Next = cur.Next
			'''
			pre.Next = Next
			cur = Next
			Next = cur.Next
		else:
			hashTable.add(cur.data)
			pre = cur
			cur = Next
			Next = cur.Next
	#这里使用Next == None作为终止条件，这个条件是在cur遍历到尾结点的时候触发的，
	#此时尾结点还没有被判定是否为重复项，因此循环后还得对尾结点专门判定一次
	if cur.data in hashTable:
		pre.Next = Next
	return head
'''
方法一的另一种遍历法，这里不用记录Next = cur.Next,避免了原来使用Next != None作为循环入口的麻烦，
并且减少了代码量
'''
def removeDup_(head):
	if head is None or head.data != None or head.Next is None:
		return False
	if head.Next.Next is None:
		return head	
	pre =  head 
	cur = head.Next
	hashTable = set()
	while cur != None:
		if cur.data in hashTable:
			pre.Next = cur.Next
			cur = cur.Next
		else:
			hashTable.add(cur.data)
			pre = cur
			cur = cur.Next
	return head
#方法二：顺序删除，外层循环遍历整个单链表，内层循环遍历剩余结点，把与外层循环遍历到的结点数据域相同的结点删掉
def removeDup2(head):
	if head is None or head.data != None or head.Next is None:
		return False
	'''
	Outcur = head.Next
	OutNext = Outcur.Next
	while OutNext != None:
		pre = Outcur
		cur = OutNext	
		Next = cur.Next
		while Next != None:
			if cur.data == pre.data:
				pre.Next = Next
				cur = Next
				Next = cur.Next
			else:
				pre = cur
				cur = Next
				Next = cur.Next
		if cur.data == pre.data:
			pre.Next = Next
		Outcur = Outcur.Next
		if Outcur != None:
			OutNext = Outcur.Next		
	return head
	'''
	Outcur = head.Next
	while Outcur != None:
		Inpre = Outcur
		Incur = Outcur.Next
		while Incur != None:
			'''有问题的写法，顺序删除每次内层循环删除的是与外层循环当前遍历的结点数据域相同的结点
			if Inpre.data == Incur.data:
				Inpre.Next = Incur.Next
				Incur = Incur.Next
			'''
			if Outcur.data == Incur.data:
				Inpre.Next = Incur.Next
				Incur = Incur.Next
			else:
				Inpre = Incur
				Incur = Incur.Next
		Outcur = Outcur.Next
	return head

#方法三：递归
def removeDup3(head):
	if head is None or head.data != None or head.Next is None:
		return False
	if head.Next.Next is None:
		return head
	res = recursive_removeDup(head.Next)
	head.Next = res
	return head

def recursive_removeDup(head):
	#递归终止返回
	if head.Next is None:
		return head
	#子问题划分与调用递归函数解决
	cur = recursive_removeDup(head.Next)
	#子问题答案的合并
	head.Next = cur
	pre = head
	while cur != None:
		'''#可能会错写为以下三行代码。
		#假设单链表为4->1->2->2->3->3->4->None,子问题为1->2->2->3->3->4->None,子问题结果为1->2->3->4->None
		#拼接head结点(原问题开头的4),得到4->1->2->3->4->None
		#如果按照这三行问题代码，则最终结果为4->None
		if head.data == cur.data:
			head.Next = cur.Next
			cur = cur.Next
		'''
		if head.data == cur.data:
			pre.Next = cur.Next
			cur = cur.Next
		else:
			pre = cur
			cur = cur.Next
	return head

'''引申：如何对有序链表去除重复项
因为链表有序，因此对于当前结点cur，重复项只可能出现在下一个，即cur.Next。
这种情况可以直接顺序删除，达到O(N)的时间，并且不需要哈希方法的O(N)内存开销
'''
def Remove_Dup(head):
	if head is None or head.data != None or head.Next is None:
		return False
	pre = head
	cur = head.Next
	while cur.Next != None:
		if cur.data == cur.Next.data:
			pre.Next = cur.Next
			cur = cur.Next
		else:
			pre = cur
			cur = cur.Next
	return head

if __name__ == '__main__':
	values = [1,1,3,1,5,5,5,7,7]
	print('Testing values:'+str(values))
	head = create_List(values)
	print('*原单链表为:')
	print_List(head)
	print('*删除重复元素以后，单链表为:')
	head = removeDup3(head)
	print_List(head)
	print('=====')
	values = [4,1,2,3,4]
	print('Testing values:'+str(values))
	head = create_List(values)
	print('*原单链表为:')
	print_List(head)
	print('*删除重复元素以后，单链表为:')
	head = removeDup3(head)
	print_List(head)
	print('=====')
	print('测试有序单链表去重')
	values = [1,1,2,2,3,4,5,6,6,6,7,8,8]
	print('Testing values:'+str(values))
	head = create_List(values)
	print('*原单链表为:')
	print_List(head)
	print('*删除重复元素以后，单链表为:')
	head = Remove_Dup(head)
	print_List(head)
	
'''
总而言之，记住：
*1.改变结点的指针域时，要考虑原来指向的内存是否还需要用到。如果要用到，可能需要使用Next = cur.Next事先保存
*2.如果采用Next != None作为循环入口，循环体先执行cur的操作，然后更新cur与Next,一定要记得循环后要追加尾结点的处理。
这也说明了Next = cur.Next并不总是带来方便的。
'''
