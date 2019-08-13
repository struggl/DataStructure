'''
实现二叉搜索树的插入、查找、求最大、求最小、求后继、求前驱、删除7大操作，时间复杂度均为O(h)
定义n个关键字的一棵随机构建二叉搜索树为按随机次序插入这些关键字到一棵初始的空树中而生成的树，这里输入关键字的n!个排列每个都等可能。
定理：一棵有n个不同关键字的随机构建二叉搜索树的期望高度为O(lgn)
'''
#得到二叉树层数(根结点所在层定义为第一层)
def get_height(root):
	#参数边界检测与递归终止返回
	if root is None:
		return 0
	n_layer = 1
	left_layer = 0
	right_layer = 0
	left_layer = get_height(root.left)
	right_layer = get_height(root.right)
	return n_layer + max(left_layer,right_layer)
				

#中序遍历二叉树
def inorder(root):
	#参数边界检测
	if root is None:
		return
	#递归终止输出
	if root.left is None and root.right is None:
		print(root.data)
	else:
		if root.left:
			inorder(root.left)
		print(root.data)
		if root.right:
			inorder(root.right)
class BSTNode(object):
	def __init__(self,x):
		self.data = x
		self.p = None
		self.left = None
		self.right = None

#二叉搜索树插入操作
def Insert_tree(root,node):
	#node数据域不为空，三个指针域均为空
	if node.data is None:
		return False
	p = None
	cur = root
	while cur != None and cur.data != None:
		#当root数据域和三个指针域均为None时，bool(root)为True!因此需要cur.data != None，否则cur.data 将报错
		#而当cur迭代到叶子结点的左孩子或右孩子时，cur为None,cur.data也会报错，因此也需要cur != None
		p = cur
		if node.data < cur.data:
			cur = cur.left
		else:
			cur = cur.right
	#若p为None，说明为空树
	if p is None:
		root = node
		return root
	#若P不为None,此时p指向树中一个叶子结点
	if node.data < p.data:
		p.left = node
		node.p = p
		return root
	p.right = node
	node.p = p
	return root

#二叉搜索树查找操作
def Search_tree(root,key):
	if root is None or root.data is None or key is None:
		#之所以要求root.data != None是因为一个数据域和指针域全为None的结点，不为None
		return None
	cur = root
	while cur != None:
		if key == cur.data:
			return cur
		if key < cur.data:
			cur = cur.left
		else:
			cur = cur.right
	return None	

#二叉树求最大
def Maximum_tree(root):
	if root is None or root.data is None:
		return
	cur = root
	while cur.right != None:
		cur = cur.right
	return cur

#二叉树求最小
def Minimum_tree(root):
	if root is None or root.data is None:
		return
	cur = root
	while cur.left != None:
		cur = cur.left
	return cur

#二叉树求后继
def Successor_tree(root,node):
	if root is None or root.data is None:
		return None
	if node is None or node.data is None:
		return None

	if node.right:
		return Minimum_tree(node.right)
	#若该结点仅有左孩子，则顺延上去迭代，它的后继为第一个使得它为左孩子的结点
	cur = node
	p = cur.p
	while p != None and cur is p.right:
		cur = p
		p = cur.p
	return p	

#二叉树求前驱
def Predecessor_tree(root,node):
	if root is None or root.data is None:
		return None
	if node is None or node.data is None:
		return None
	if node.left:
		return Maximum_tree(node.left)
	cur = node
	p = cur.p
	while p != None and cur is p.left:
		cur = p
		p = cur.p
	return p

##二叉树删除结点操作
def Delete_node(root,node):
	if root is None or root.data is None:
		return None
	if node is None or node.data is None:
		return None
	#第一类情形：没有左孩子
	if node.left is None:
		root = Transplant_node(root,node,node.right)
		return root
	#第二类情形：有左孩子但没有右孩子
	if node.right is None:
		root = Transplant_node(root,node,node.left)
		return root
	#第三类情形：有左孩子和右孩子，因此后继结点必然在node.right这边,细分两种情况:后继是否为node的右孩子
	#注意，后继结点没有左孩子(否则node的后继就应该是这个左孩子，因为这个左孩子必然比node大且比这个伪后继结点小)
	successor = Successor_tree(root,node)
	if successor is not node.right:	
		root = Transplant_node(root,successor,successor.right)	
		#successor虽有左右指针域，但这里构建node右孩子与successor的双向链接时，显然是用successor.right指针域
		successor.right = node.right
		node.right.p = successor
	root = Transplant_node(root,node,successor)
	#最后构建successor与node左孩子的双向链接
	successor.left = node.left
	node.left.p = successor	
	return root

def Transplant_node(root,u,v):
	#u和v都是同一棵二叉树上的结点，(v可为None)用v替代二叉树中u的位置，本质上是构建u.p与v的双向链接
	if root is None or root.data is None:
		return None
	if u is None or u.data is None:
		return None
	if u.p is None:
		v.p = None
		return v
	if u is u.p.left:
		u.p.left = v
	else:
		u.p.right = v
	if v != None:
		v.p = u.p	
	return root	



if __name__ == '__main__':
	root = BSTNode(None)
	inorder(root)
	print('height:')
	print(get_height(root))
	print('==插入操作==')
	root = Insert_tree(root,BSTNode(3))	
	root = Insert_tree(root,BSTNode(1))	
	root = Insert_tree(root,BSTNode(2.5))	
	root = Insert_tree(root,BSTNode(2))	
	root = Insert_tree(root,BSTNode(3))	
	root = Insert_tree(root,BSTNode(4))	
	root = Insert_tree(root,BSTNode(5))	
	root = Insert_tree(root,BSTNode(0))	
	inorder(root)
	print('height:')
	print(get_height(root))
	print('==查找操作==')
	print(Search_tree(root,4))
	print(Search_tree(root,8))
	print('==求最大操作==')
	print(Maximum_tree(BSTNode(None)))
	print(Maximum_tree(root).data)
	print('==求最小操作==')
	print(Minimum_tree(root).data)
	print('==求后继操作==')
	node = root.left.right
	res = Successor_tree(root,node)
	if res:
		print(res.data)
	else:
		print(res)
	print('==求前驱操作==')
	node = root.right.right.right
	res = Predecessor_tree(root,node)
	if res:
		print(res.data)
	else:
		print(res)
	print('==子树替换操作==')
	print('原二叉树中序遍历')	
	inorder(root)
	print('子树替换后中序遍历')
	root = Transplant_node(root,root,root.left)
	#root = Transplant_node(root,root,root.right)
	inorder(root)
	print('==二叉树删除结点操作==')
	print('原二叉树中序遍历')	
	inorder(root)
	print('删除结点后中序遍历')
	root = Delete_node(root,root.left)
	inorder(root)
