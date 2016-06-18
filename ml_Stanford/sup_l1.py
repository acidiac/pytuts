# date 15 June 2016
# Amit Chanchal
# from Coursera course on Machine Learning by Andrew NG

'''
this is a supervised learning case.
Supervised learning is based on given data and it can be of two common types:
	1> Regression: here the algorithm produces a real value output
	2> Classification: here we predict discreet value output (like 0 or 1 value)

The data provided to the algorithm in supervised learning is called training set

Regression Sample case is portland real estate prices where
 notations::
 	m = Number of training examples
 	x = "input" variable/feature ( in this case it is the size of property in sft)
 	y = "output" variable/ target (here it is the price in USD)
 	(x,y) =  single training example, ie. single row
 	(xi, yi) = i th training example or row
 How it works::
 	training set --> learning alg --> function "h"( called hypothesis)
 	input variable (size) --> function h --> output (estimated price)

 How to represent function h::
 	case1 (linear function):
 		h(x) = theta(0) + theta(1)x
 		this is straight line (linear function) representation of the fitted solution line
 		although in mnay case linear function might not be ideal but to start with it is a simple case to consider
 		Univariate linear regression =  linear regerssion in one variable (here the area/size)
	case2 (non-linear functions):

Classification sample case:
	to classify tumors as malignant or benign
	we can have single, double or even infinite variable for classification
	how to we deal with infinite variables?
	turns out we can trick the machine with something termed as Support Vector Machine
'''