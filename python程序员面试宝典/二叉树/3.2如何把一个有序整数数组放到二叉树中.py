'''
题目描述：把[1,2,3,4,5,6,7,8,9,10]放到二叉树中，使得该树的中序遍历也是这个数组

思路：取数组中间元素作为根结点，将数组分成左右两部分，对这两部分也分别递归地构建左右子树
注意：确定数组中间元素，总是(end+start+1)//2.当数组长度为奇数时，显然成立，而当数组长度为偶数时，这样做的原因是，二叉树可以有左结点
而无右结点，但不可以没有左结点而有右结点
'''
class BTNode(object):
	def __init__(self,x):
		self.data = x
		self.lchild = None
		self.rchild = None

#以中序构建二叉树
def inorder_create_BTree(arr):
	if arr is None or type(arr) != list or len(arr) == 0:
		return False
	res =  _inorder_create_BTree(arr,0,len(arr)-1) 
	return res

def _inorder_create_BTree(arr,start,end):
	#递归终止返回
	if start > end:
		return
	#或mid = start + (end-start+1)//2
	mid = (end+start+1) // 2
	root = BTNode(arr[mid])
	root.left = _inorder_create_BTree(arr,start,mid-1)
	root.right = _inorder_create_BTree(arr,mid+1,end)
	return root


		
#中序遍历
def inorder(root):
	if root is None or root.data is None:
		return False
	#递归终止条件
	if root.left is None and root.right is None:
		print(root.data)		
	else:
		#检测二叉树是否非法
		if root.left is None and root.right:
			return False
		if root.left:
			inorder(root.left)
		print(root.data)
		if root.right:
			inorder(root.right)

if __name__ == '__main__':
	values = [2,3,4,5,6,7,8,9,10]
	root = inorder_create_BTree(values)
	inorder(root)
