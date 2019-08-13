'''
题目描述：两棵二叉树相等是指这两棵二叉树有着相同的结构，且在相同位置上的结点有相同的值。
如何判断两棵二叉树是否相等？
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

#方法实现
def isEqual(root1,root2):
	#这个递归很值得跟踪一下过程，蛮有意思的
	#写的时候仍然从子问题划分与结果归并出发，直到写完递归终止
	#递归终止返回，同时也是参数边界检测
	if root1 is None and root2 is None:
		#return True
		print('/1')
		print('True')
		print('1/')
		return True
	elif root1 is None and root2 != None:
		#return False
		print('/2')
		print('False')
		print('2/')
		return False
	elif root1 != None and root2 is None:
		#return False
		print('/3')
		print('False')
		print('3/')
		return False
	elif root1.data != root2.data:
		#return False
		print('/4')
		print('False')
		print('4/')
		return False
	bool_left = isEqual(root1.left,root2.left)
	bool_right = isEqual(root1.right,root2.right)
	if bool_left and bool_right:
		print('-----')
		print('True')
		print('-----')
		return True
	print('=')
	print('False')
	print('=')
	return False

if __name__ == '__main__':	
	root1 = inorder_create_tree([1,2,3,4,5])
	root2 = inorder_create_tree([1,2,3,4,6])
	#print(isEqual(root1,root2))
	print('判断结果为：')
	isEqual(root1,root2)









