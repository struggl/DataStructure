'''
题目描述：判断一个字符串是否包含重复字符
输入样例
good 
输出
True

方法一：蛮力法,O(N**2)
方法二：空间换时间(哈希法),O(N)
'''
#方法一实现
def isDup(string):
	if type(string) != str and type(string) != list:
		return
	if len(string) == 0:
		return
	if len(string) == 1:
		return False
	for i in range(len(string)):
		for j in range(i+1,len(string)):
			if string[i] == string[j]:
				return True
	return False

#方法二实现
def isDup2(string):
	if type(string) != str and type(string) != list:
		return
	if len(string) == 0:
		return
	if len(string) == 1:
		return False
	Set = set()
	for i in range(len(string)):
		if string[i] in Set:
			return True
		Set.add(string[i])
	return False

if __name__ == '__main__':
	string = 'good'
	string = 'best'
	print(isDup(string))
	print(isDup2(string))	
