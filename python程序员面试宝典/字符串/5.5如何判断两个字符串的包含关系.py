'''
题目描述：
输入样例：
s1 = 'abcdef'
s2 = 'acf'
则s1包含s2

方法一：直接法。遍历s2每个字符，看是否在s1中。时间复杂度为O(m*n)
方法二：字典法。遍历s2每个字符，若字典不存在该键，则构建一个值为1的键值对。接着遍历s1中每个字符，如果字典中存在该键，修改值为0
最后若字典的值列表和为0，说明s1包含s2，否则不包含。时间复杂度为O(m+n)
'''
def isContain(s1,s2):
	'''判断s1是否包含s2
	'''
	if type(s1) != str or type(s2) != str:
		return
	if len(s1) == 0 or len(s2) == 0:
		return False
	if len(s1) < len(s2):
		return False
	res = True
	for v in s2:
		if v not in s1:
			#这个判断时间代价为O(len(s1))
			res = False
			break
	return res

def isContain2(s1,s2):
	if type(s1) != str or type(s2) != str:
		return
	if len(s1) == 0 or len(s2) == 0:
		return False
	if len(s1) < len(s2):
		return False
	Dict = dict()
	for v in s2:
		if not Dict.get(v):
			Dict[v] = 1
	for v in s1:
		if Dict.get(v):
			Dict[v] = 0
	if sum(Dict.values()) == 0:
		return True
	else:
		return False	


if __name__ == '__main__':
	print(isContain2('abcdef','acf'))	
	print(isContain2('abcdef','acg'))	
	print(isContain2('acf','abcdef'))	
		
