#如何求一个字符串的所有排列
def Permutation(string):
	#参数检测处理
	if type(string) is not str:
		return False
	permutation(list(string),0)	

#递归函数部分
def permutation(string,start):
	if start == len(string) -1:
		print(''.join(string))
	else:
		i = start
		#通过依次交换string中每个位置与i位置来划分子问题
		#对每个划分出来的子问题，只需要关注start位置以后的全排序问题
		#即permutation(string,start+1)
		while i < len(string):
			swap(string,i,start)
			permutation(string,start+1)
			swap(string,i,start)
			i += 1

#辅助函数
def swap(string,i,j):
	tmp = string[i]
	string[i] = string[j]
	string[j] = tmp


if __name__ == '__main__':
	print('testing:abc')
	Permutation('abc')
	print('\ntesting:abcd')
	Permutation('abcd')
'''
这道题与前面1.merge_sort.py和2.strToint.py的主要区别在于：
1.前面两道都是先划分子问题(归并排序数组对半分和把'123'求整数转为'12'求整数)，求得子问题答案之后，显式地归并起来。
2.而这道题并没有明显的归并步骤。对每个划分处理的子问题，通过start参数指示全排列到达的位置，当到达最后一个位置时，print出来即可
'''
