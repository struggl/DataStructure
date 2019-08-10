#归并排序
def merge(left,right):
	i = 0;j = 0
	res = []
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			res.append(left[i])
			i += 1
		else:
			res.append(right[j])
			j += 1
	res += left[i:]
	res += right[j:]
	return res

def merge_sort(List):
	#参数边界处理 和 递归终止返回
	if List is None or len(List) <= 1:
		return List
	#划分子问题
	num = len(List) // 2
	#解决子问题
	left = merge_sort(List[:num])
	right = merge_sort(List[num:])
	#(检查是否需要)归并子问题的答案
	return merge(left,right)

if __name__ == '__main__':
	List = [1,4,5,2,3]
	print(List)
	print(merge_sort(List))

'''
递归函数一般模板
def Recursive(args):
	参数边界处理(if... elif... else)
	递归终止返回(if... else...)
	划分子问题
	调用自身解决子问题
	检查是否需要归并子问题的答案

def 解决方案(args):
	这里就不要再有边界处理问题了，应该由Recursive全部拦截完毕
	return...
	

#注意，应用于打印问题时，所谓的print 可以与 return 对等
	

'''
