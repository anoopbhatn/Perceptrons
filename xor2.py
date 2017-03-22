# Backpropagation algorithm implementation for XOR with graph
import numpy as np, matplotlib.pyplot as plt
import random

# Sigmoid Function return : 1/(1+e^-z)
def sigmoid(z):
	return 1.0 / (1.0 + np.exp(-z))

# To compute result
def compute_res(x, y, W1, W2, b1, b2):
	# Hidden Layer Pass
	z1 = np.dot(x, W1.T) + b1
	# Sigmoid Function is applied for each Output
	x1 = sigmoid(z1)
	# Output Layer Pass
	z2 = np.dot(x1, W2.T) + b2
	# Sigmoid Function is applied for each Output
	x2 = sigmoid(z2)
	# Error Calculation for every output
	error = x2 - y
	print error
	# Calulating Ed value i.e Error on Training example d
	Ed = 0.5 * sum(error ** 2)
	return z1, x1, z2, x2, error, Ed

# Training Atrributes
x = [[0,0],[0,1],[1,0],[1,1]]
# Target values
y = [[0],[1],[1],[0]]

# Convert them into arrays
x , y = np.array(x) , np.array(y)

# Initialize Random Weights
W1 , W2 = np.random.randn(4,2) , np.random.randn(1,4) 

# Initialize Random Bias : b1 for hidden layer and b2 for Output layer
b1 , b2 = np.random.randn(1,4) , random.random()  

# Learning Rate l
l= 0.1
Ed_list=[]

for i in range(100000):
	z1 , x1 , z2 , x2 , error , Ed = compute_res(x, y, W1, W2, b1, b2)
	
	# If Error is less than 0.01, break
	if Ed < 0.01:
		break
	# print "i=",i,"Error:",Ed
	Ed_list.append(Ed)
	# Delta for Outer Unit
	delta2 = error * sigmoid(z2) *sigmoid(1-z2)
	# Multiply delta to output of hidden layer
	dw2 = np.dot(delta2.T, x1)

	# Delta for Hidden Unit
	delta1 = np.dot(delta2,W2) * sigmoid(z1) *sigmoid(1-z2)
	# Multiply delta to Inputs
	dw1 = np.dot(delta1.T,x)
	# Revise Weights
	W1, W2 = W1 - l * dw1, W2 - l * dw2
	# Revise Biases
	b1 , b2 = b1 - l * sum(delta1), b2 - l * sum(delta2)
	

print "Output:",compute_res(x, y, W1, W2, b1, b2)[3].T
plt.plot([j for j in range(len(Ed_list))],Ed_list)
plt.xlabel('Iterations -->')
plt.ylabel('Ed Value -->')
plt.show()
