'''二叉树基础知识
一、定义
1.二叉树(Binary Tree)也称为二分树、二元树、对分树等，它是n(n>=0)个有限元素的集合，该集合或者为空、或者由一个称为根(root)的
元素及两个不相交的、被分别称为左子树和右子树的二叉树组成。当集合为空，称该树为空二叉树。

2.在二叉树中，一个元素也称为一个结点。

3.二叉树的递归定义：二叉树或者是一棵空树，或者是一棵由根结点和左右子树组成的非空树，左子树和右子树同样也是一棵二叉树。

4.二叉树的常见概念
(1)结点的度(沿用了图论中出度的定义)：结点所拥有的子树的个数
(2)叶子结点或终端结点：度为0的结点
(3)分支结点或非终端结点：度不为0的结点。
显然，一棵树的结点除了叶子结点外都是分支结点。
(4)孩子、双亲：树中一个结点的子树根结点是它的孩子，左右子树的根结点分别是它的左右孩子。这个结点是它孩子们的双亲。
(5)路径、路径长度：如果一棵树的一串结点n_1,n_2,...,n_k满足：任意结点n_i是n_(i+1)的父结点(1 <= i <= k),就把这串结点称为一条从
n_1到n_k的路径。这条路径的边数k-1称为路径的长度。
(6)祖先、子孙：在树中，如果有一条路径从结点M到结点N，那么M就称为N的祖先，N称为M的子孙。
(7)结点的层数：规定树的根结点的层数为1(很多书定义根结点所在层为第0层)，其余结点层数等于它的双亲结点的层数+1.
(8)树的深度：树中所有结点的最大层数称为树的深度。
(9)树的度：树中各结点的度的最大值称为该树的度，叶子结点度为0
(10)满二叉树:在一棵二叉树中，如果所有分支结点都存在左子树和右子树，并且所有叶子结点都在同一层上，
这棵树就称为满二叉树。
(11)完全二叉树：一棵深度为k的有n个结点的二叉树,对树中的结点按从上到下、从左到右的顺序进行编号，如果编号为i(1 <= i <= n)的结点
与满二叉树中编号为i的结点在二叉树中的位置相同，则这棵树称为完全二叉树。
*补充：完全二叉树的特点是，叶子结点只能出现在最下层和次下层，且最下层的叶子结点集中在树的左部。
*满二叉树一定是完全二叉树，反之不成立。
*满二叉树与完全二叉树高度是一致的。

二、基本性质(这里二叉树的第一层定义为根结点所在层)
1.一棵非空二叉树的第i层最多有2的(i-1)次方个结点(i >= 1)
(这个最多的数量，对应了满二叉树的结点数量)

2.一棵深度为k的二叉树中，最多具有(2的k次方)-1个结点，最少有k个结点.

3.结点数为n的树有(n-1)条边。(来自<<离散数学及其应用>>p638)

4.对于一棵非空二叉树，度为0的结点(即叶子结点)总是比度为2的结点多一个。(以2层的满二叉树作为记忆)
证明：用n0,n1,n2分别表示非空二叉树中度为0,1,2的结点总数。用n表示整个二叉树的结点总数。
根据性质3，有n-1 = n1 + 2*n2.
又显然，n = n0 + n1 + n2.
下式减去上式，有1 = n0 - n2
命题得证。

5.具有n个结点的完全二叉树的深度为math.floor(log2(n)) + 1

6.编号性质(已知第i个结点编号，求它的双亲、左右孩子编号)
对于具有n个结点的完全二叉树，如果按照从上到下和从左到右的顺序对二叉树中所有结点从1开始顺序编号，则对于任意第i个结点，有：
(1)若i = 1，则第i个结点为根结点，无双亲。
(2)若i > 1,则第i个结点的双亲编号为i//2.
(3)若2i <= n,则第i个结点的左孩子结点序号为2i
(4)若2i > n,则第i个结点无左孩子
(5)若2i + 1 <= n，则第i个结点的右孩子的序号为2i+1
(6)若2i + 1 > n,则第i个结点无右孩子。
*补充：
若从0开始给结点编号，则对编号为i(i>0)的结点，
双亲编号为(i-1)//2
左孩子编号为2i+1
右孩子编号为2i+2
(7)满二叉树的最后一层是总结点数的接近一半



三、经典问答
1.一棵完全二叉树有1001个结点，其中叶子节点有多少个？
n = n0 + n1 + n2 = n0 + n1 + (n0 - 1) = 2*n0 + n1 - 1
对于完全二叉树，显然n1要么为0，要么为1.
如果n1 = 1，则有1001 = 2*n0 + 1 - 1，所得n0不为整数，舍去。
如果n1 = 0，则有1001 = 2*n0 + 0 - 1,得到n0 = 501.

2.如果根的层次为1，具有61个结点的完全二叉树高度为多少？
根据基本性质5，得到h = match.floor(math.log(61,2)) + 1 = 6层。  

3.在具有100个结点的树中，边的数目是多少？
根据基本性质3，边的数目为99

四、树的遍历定义
1.前序遍历：先列当前结点，然后列子结点
2.中序遍历：先列左孩子，然后列当前结点，然后其他孩子
3.后序遍历：先列孩子，然后列当前结点
4.层序遍历：对树的每一层从左到右列出结点.
实现思路一：(时空均为O(N))
根结点入队列Q
while Q不为空集
	s = dequeque(Q)
	print(s.data)
	if s.left != None:
		enqueue(s.left)
	if s.right != None:
		enqueue(s.right)

实现思路二：(空间O(1))

五、画图法与树的遍历
从根结点出发，往左孩子方向画圈，沿着整个树返回根结点
1.前序遍历：第一次经过一个顶点，就列出该顶点
2.中序遍历：第一次经过叶子结点，就列出该叶子结点，第二次经过内点，就列出该内点
3.后序遍历：最后一次经过顶点而返回它的父结点时，列出该结点

'''
class BTNode(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None

def create_tree():
	#按中序构建二叉树
	node_list = []
	values = [1,2,3,4,5,6,7,8,9,10]
	for v in values:
		node_list.append(BTNode(v))
	#for i in range(11):
	#	node_list.append(BTNode(i))
	root = node_list[5]
	root.left = node_list[2]
	root.left.left = node_list[1]
	root.left.right = node_list[4]
	root.left.left.left = node_list[0]
	root.left.right.left = node_list[3]
	
	root.right = node_list[8]
	root.right.left = node_list[7]
	root.right.right = node_list[9]
	root.right.left.left = node_list[6]
	return root

#前序遍历
def preorder(root):
	#参数边界处理直到else
	if root is None:
		return False
	if root.left is None and root.right is None:
		print(root.data)
	else:
		#当前递归结点要采取的动作
		print(root.data)
		#以下两个if的相反情况实际上是递归终止条件
		if root.left:
			preorder(root.left)
		if root.right:
			preorder(root.right)

#中序遍历
def inorder(root):
	if root is None:
		return False
	if root.left is None and root.right is None:
		print(root.data)		
	else:
		if root.left:
			inorder(root.left)
		print(root.data)
		if root.right:
			inorder(root.right)

#后序遍历
def postorder(root):
	if root is None:
		return False
	if root.left is None and root.right is None:
		print(root.data)
	else:	
		#检测二叉树是否合法
		if root.left is None and root.right:
			return False
		if root.left:
			postorder(root.left)
		if root.right:
			postorder(root.right)
		print(root.data)

#层序遍历以及用层序遍历给树结点进行编号(编号性质前提是完全二叉树)
def printAtLevel(root,level):
	if root is None or level < 0:
		return 0
	if level == 0:
		print(root.data)
		return 1
	else:
		return printAtLevel(root.left,level-1) + printAtLevel(root.right,level-1)

def layerorder(root):
	level = get_height(root)
	printAtLevel(root,level)
'''
def layerorder(root):
	if root is None or root.data is None:
		return False
	print(root.data)
	_layerorder(root)

def _layerorder(root):
	#递归终止条件：叶子结点
	#原判断语句为if root.left is None and root.right is None:
	#实际上由于二叉树先有左结点后有右结点的特性(你大爷谁告诉你有这个性质的，把二叉搜索树放哪儿了！)，只需要root.left为None即可
	if root is None or root.left is None:
		return 
	if root.left:
		print(root.left.data)
	if root.right:
		print(root.right.data)
	_layerorder(root.left)
	_layerorder(root.right)
'''

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

		
#获取二叉树结点个数
def get_nums(root):
	#递归终止返回
	if root is None:
		return 0
	return get_nums(root.left) + get_nums(root.right) + 1

#获取二叉树层数(根结点所在层定义为第一层)
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
'''
#得到完全二叉树层数(根结点所在层定义为第一层)
def get_height(root):
	num = get_nums(root)
	import math
	return math.floor(math.log(num,2)) + 1
'''	
if __name__ == '__main__':
	root = create_tree()
	#root = BTNode(1)
	#root.left = BTNode(2)
	#root.right = BTNode(3)
	preorder(root)	
	print('=====')
	inorder(root)	
	print('=====')
	postorder(root)
	print('=====')
	print(get_nums(root))
	print('=====')
	print(get_height(root))
	print('=====')
	layerorder(root)	




























