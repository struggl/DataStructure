'''
题目描述：给定一棵二叉树，它的每个阶段都是整数(可以为负数),如何找到一棵子树，使得它所有结点的和最大？
思路：遍历每棵子树，计算结点和，比较所有子树的结点和
个人感觉用前序遍历是最简洁的，因为当前子树不一定有左右结点，但是一定有当前这个结点值，无论中序还是后序，都要先
看有没有左结点，多了一层判断，会多需要一个临时变量,至于层序遍历，完全没这个必要
'''
class BTNode(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None
		self.id = None

#以中序构建二叉树
def inorder_create_BTree(arr):
	if arr is None or type(arr) != list or len(arr) == 0:
		return False
	return _inorder_create_BTree(arr,0,len(arr)-1)

def _inorder_create_BTree(arr,start,end):
	#递归终止返回
	if start > end:
		return 
	mid = (start + end + 1) // 2
	root = BTNode(arr[mid])
	root.left = _inorder_create_BTree(arr,start,mid-1)
	root.right = _inorder_create_BTree(arr,mid+1,end)
	return root

class Test(object):
	'''
	使用递归来计数时，除非是像3.1basic.py计算结点总数那样的简单情形，
	否则还是要用类来维护一个整个递归栈都可见的计数变量
	说3.1basic.py简单是因为每次递归都对最上层返回有简单的加1贡献，
	而本题获取最大子树需要对比并存储不同递归结点的加和,给树结点进行编号也需要维护一个各递归可见的变量
	'''
	def __init__(self):
		import sys
		#sys.maxsize为系统最大整数值，-sys.maxsize-1得到最小整数值
		self.maxSum = -sys.maxsize - 1
		self.maxNode = BTNode(self.maxSum)
		self.id = 1
	
	def rank_node(self,root):
		#中序遍历对全树结点进行编号
		if root is None:
			return False
		if root.left is None and root.right is None:
			root.id = self.id
			self.id += 1	
		else:
			#以下两个if的相反情况实际上是递归终止条件
			if root.left:
				self.rank_node(root.left)
			#当前递归结点返回的东西或输出的东西(相当于把返回值定向到类变量中)
			root.id = self.id
			self.id += 1
			if root.right:
				self.rank_node(root.right)
	
	def get_maxSum(self,root):
		if root is None:
			return
		if root.left is None and root.right is None:
			return root.data
		#以上皆为参数边界检测
		Sum = root.data	
		#if root.left 与 if root.right的相反情况实际上作为递归终止条件
		if root.left:
			Sum += self.get_maxSum(root.left)
		if root.right:
			Sum += self.get_maxSum(root.right)
		#维护最大
		if Sum > self.maxSum:
			self.maxSum = Sum
			#其实要想真正锁定最大子树的根结点位置，应当先用层序遍历给全树结点编号，返回最大子树根结点的编号
			self.maxNode.data = root.id
		#当前递归结点的返回
		return root.data

#中序遍历输出结点值
def inorder(root):
	if root is None:
		return False
	if root.left is None and root.right is None:
		print(root.data)		
	else:
		#以下两个if的相反情况实际上是递归终止条件
		if root.left:
			inorder(root.left)
		#当前递归结点输出或返回的东西
		print(root.data)
		if root.right:
			inorder(root.right)

#中序遍历输出结点id
def inorder2(root):
	if root is None:
		return False
	if root.left is None and root.right is None:
		print(root.id)		
	else:
		#以下两个if的相反情况实际上是递归终止条件
		if root.left:
			inorder2(root.left)
		print(root.id)
		if root.right:
			inorder2(root.right)


	

if __name__ == '__main__':
	test = Test()
	root = inorder_create_BTree([1,200,3,4,5,6,7,8,90,10])
	inorder(root)
	print('=====')
	test.rank_node(root)
	inorder2(root)
	print('=====')
	test.get_maxSum(root)
	print(test.maxSum)
	print(test.maxNode.data)
