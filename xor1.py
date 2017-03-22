import numpy as np, matplotlib.pyplot as plt
import random

def sigmoid(z):
	return 1.0 / (1.0 + np.exp(-z))

def compute_res(x, y, W1, W2, b1, b2):
	z1 = np.dot(x, W1.T) + b1
	x1 = sigmoid(z1)
	z2 = np.dot(x1, W2.T) + b2
	x2 = sigmoid(z2)
	error = x2 - y

	Ed = 0.5 * sum(error ** 2)
	return z1, x1, z2, x2, error, Ed

x = [[0,0],[0,1],[1,0],[1,1]]
y = [[0],[1],[1],[0]]

x , y = np.array(x) , np.array(y)

W1 , W2 = np.random.randn(4,2) , np.random.randn(1,4) 
b1 , b2 = np.random.randn(1,4) , random.random()  

l= 0.1
Ed_list=[]

for i in range(100000):
	z1 , x1 , z2 , x2 , error , Ed = compute_res(x, y, W1, W2, b1, b2)
	if Ed < 0.01:
		break
	# print "i=",i,"Error:",Ed
	Ed_list.append(Ed)

	delta2 = error * sigmoid(z2) *sigmoid(1-z2)
	dw2 = np.dot(delta2.T, x1)

	delta1 = np.dot(delta2,W2) * sigmoid(z1) *sigmoid(1-z2)
	dw1 = np.dot(delta1.T,x)
	W1, W2 = W1 - l * dw1, W2 - l * dw2
	b1 , b2 = b1 - l * sum(delta1), b2 - l * sum(delta2)
	
print "Output:",compute_res(x, y, W1, W2, b1, b2)[3].T