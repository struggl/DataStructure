'''
题目描述：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表(要求该链表顺序与二叉搜索树中序遍历顺序一致)
要求不能创建任何新的结点，只能调整结点的指向。
'''
class BTNode(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None

#中序构建二叉树
def inorder_create_tree(arr):
	if arr is None or type(arr) != list or len(arr) == 0:
		return False
	return _inorder_create_tree(arr,0,len(arr)-1)

def _inorder_create_tree(arr,start,end):
	if start > end:
		return
	mid = (start + end + 1) // 2
	root = BTNode(arr[mid])
	root.left = _inorder_create_tree(arr,start,mid-1)
	root.right = _inorder_create_tree(arr,mid+1,end)
	return root

def print_BList(Head,End):
	#没有头尾辅助结点，全都是有效结点
	if Head is None or End is None:
		return
	print('-从左到右遍历-')	
	cur = Head
	while cur != None:
		print(cur.data)
		cur = cur.right
	print('-从右到左遍历-')	
	cur = End
	while cur != None:
		print(cur.data)
		cur = cur.left

def Tree2BList(root):
	#参数边界检测
	if root is None:
		return
	#初始化双向链表
	Head = None
	End = None
	#把二叉树转为双向链表
	Head,End = _Tree2BList(root,Head,End)
	#返回双向链表头尾结点
	return Head,End	
			 
def _Tree2BList(root,Head,End):
	#这一行if root.left 和下面的if root.right的相反情况实际上作为递归终止条件
	#中序遍历先处理左孩子
	if root.left:
		Head,End = _Tree2BList(root.left,Head,End)
	
	#接着处理当前结点
	if Head is None:
		#当双向链表为空时，End为尾结点，数据域为None
		Head = root
		End = root 
	else:
		End.right = root
		root.left = End
		End = root

	#最后处理右孩子
	if root.right:
		Head,End = _Tree2BList(root.right,Head,End)
	return Head,End
	
	

if __name__ == '__main__':	
	root = inorder_create_tree([1,2,3,4,5,6,7])
	Head,End = Tree2BList(root)	
	print_BList(Head,End)
