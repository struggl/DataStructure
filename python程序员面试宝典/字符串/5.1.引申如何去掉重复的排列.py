'''
题目描述：如题
方法思路：
原来求去排列的子问题划分是，每次都将当前位置与后面位置进行交换，要想去重，只需要在交换之前判断后面的位置是否已经出现过即可
'''
def Permutation(string,start):
	if string is None or string == '':
		return 
	if start < 0:
		return
	if type(string) is str:
		string = list(string)
	#递归终止返回
	if start == len(string) - 1:
		print(''.join(string))
	else:
		Set = set()
		for i in range(start,len(string)):
			if string[i] not in Set:
				Set.add(string[i])
				swap(string,start,i)
				Permutation(string,start+1)
				swap(string,start,i)	

def swap(string,start,i):
	tmp = string[start]
	string[start] = string[i]
	string[i] = tmp

if __name__ == '__main__':
	string = 'abca'
	Permutation(string,0)	
