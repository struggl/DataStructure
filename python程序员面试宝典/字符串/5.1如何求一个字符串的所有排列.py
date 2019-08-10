'''
题目描述：输出字符串的全排列
输入样例：
abc
输出：
abc
acb
bac
bca
cba
cab

方法一：递归
方法二：非递归
'''
#方法一递归法实现
def Permutation(string,start):
	if string is None or string == '':
		return
	if start < 0:
		return
	if type(string) is str:
		string = list(string)
	#递归终止返回
	if start == len(string)-1:
		print(''.join(string))
	else:
		for i in range(start,len(string)):
			swap(string,start,i)
			Permutation(string,start+1)
			swap(string,start,i)

def swap(string,start,i):
	tmp = string[start]
	string[start] = string[i]
	string[i] = tmp


if __name__ == '__main__':
	string = 'abcd'
	Permutation(string,0)	

