#不使用开方运算，判断一个自然数n是否是某个数的平方
#法一:暴力法：从1遍历到n，求平方，看是否能等于n，时间复杂度为O(根号(n))
#法二:数学规律法:对一个数n，使它逐次减去m=1,3,5,7...，若差能等于0，则数n是某个数的平方。若差小于0，则n非某数的平方。若差大于0，则继续减。
#时间复杂度为O(根号n)，由于这里使用减法，而法一用乘法，因此实际上法二会比法一快一些
#法三:二分查找法:对1到n每次折半，以中点的平方power与n进行对比,时间复杂度为O(log(n))


#二分查找法
def isPower(n):
	#参数边界处理
	if n < 0:
		return -1
	if n == 1 or n == 0:
		return n
	low = 1
	high = n
	while low < high:
		mid = low + (high - low) // 2
		power = mid * mid
		if power > n:
			high = mid - 1
		elif power < n:
			low = mid + 1
		else:
			return mid
	return -1

if __name__ == '__main__':
	n = 16
	print('Testing:n = '+str(n))
	print(isPower(n))
	n = 15
	print('Testing:n = '+str(n))
	print(isPower(n))
