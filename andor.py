# A Perceptron for Boolean functions - AND and OR
import random

# To compute the result given w and data values of x
def compute(w,data_x):
	res=0
	# Compute the result summation(w(i)*x[i])
	#print w,data_x
	for i in range(1,len(w)):
		res+=w[i]*data_x[i]
	res+=w[0]
	# If result is >=0 return 1 else 0
	if res >=0:
		return 1
	else:
		return 0

# To Find the vector w
def perceptron(data_x,data_y,l=0.1):
	w=[]
	# Giving Random weights
	for i in range(len(data_x[0])):
		w.append(random.uniform(-1.0,1.0))
	wc=w
	w1=[i for i in w]
	while True:
		for i in range(len(data_x)):
			pred=compute(w,data_x[i])
			for j in range(len(w)):
				w[j]=w[j]+(l*(data_y[i]-pred)*data_x[i][j])
		if w==w1:
			break
		w1=[i for i in w]
	return w

# Data x is of the form [1,x1,x2]. The first 1 is to help perceptron calculate threshold
data_x=[[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
# Y-values for OR
y_or=[0,1,1,1]
# Y-values for AND
y_and=[0,0,0,1]

while True:
	print '\nSelect a Boolean Function : '
	print '1. AND\n2. OR\n3. Exit'

	ch=input()
	if ch==1:
		# Compute the weight vector
		w=perceptron(data_x,y_and)
		print 'Enter x1 and x2 :'
		x=map(int,raw_input().split(' '))
		x=[1]+x

		print '\nThe Result is : ',compute(w,x),'\n'
	elif ch==2:
		# Compute the weight vector
		w=perceptron(data_x,y_or)
		print 'Enter x1 and x2 :'
		x=map(int,raw_input().split(' '))
		x=[1]+x

		print 'The Result is : ',compute(w,x),'\n'
	else:
		break