'''
求f(x) = -x_1^2 - 3*x_2^2 + 2x_1*x_2 + 6最小值,x_1和x_2取值为[-3,3]
画图可知最小解约为(2.9,-2.9)，min f(x_1,x_2)约为-44.46
'''
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt

def f(x_1,x_2):
	return -x_1**2 - 3*x_2**2 + 2*x_1*x_2 + 6

def plot(a1=-3,b1=3,a2=-3,b2=3):
	fig = plt.figure()
	ax = Axes3D(fig)
	x = np.arange(a1,b1,0.1)
	y = np.arange(a2,b2,0.1)
	X,Y = np.meshgrid(x,y)
	Z = f(X,Y)
	plt.xlabel('x1')
	plt.ylabel('x2')
	ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow')
	plt.show()
    

if __name__ == '__main__':
	plot()

