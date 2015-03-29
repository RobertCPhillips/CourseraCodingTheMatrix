# version code 0672c0a36066+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from mat import *
from vec import *
from cancer_data import *

## Task 1 ##
def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    return Vec(u.D,{k:(1 if u[k] >=0 else -1) for k in u.D})

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w 
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> fraction_wrong(A, b, w)
        0.3333333333333333
    '''
    p = signum(A*w) - b
    incorrect = -.5*p*b
    return incorrect / (b*b)
    
## Task 3 ##
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> loss(A, b, w)
        317
    '''
    p = A*w - b
    return p*p

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> find_grad(A, b, w) == Vec({'B', 'A'},{'B': -290, 'A': 60})
        True
    '''
    return 2*A.transpose()*(A*w-b)

## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> sigma = .1
        >>> gradient_descent_step(A, b, w, sigma) == Vec({'B', 'A'},{'B': 27.0, 'A': -5.0})
        True
    '''
    return w - sigma*find_grad(A, b, w)

## Ungraded task ##
def gradient_descent(A, b, w, sigma, T):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
        - T: number of iterations to run
    Output: hypothesis vector obtained after T iterations of gradient descent.
    '''
    for i in range(T):
      w = gradient_descent_step(A,b,w,sigma)
      if i % 30 == 0:
        print('loss: {0}  misclassified: {1}'.format(loss(A,b,w), fraction_wrong(A,b,w)))
    
    return w

A,b = read_training_data('train.data')

s1 = 2e-9
s2 = 1e-9
w_ones = Vec(A.D[1],{k:1 for k in A.D[1]})
w_zeros = Vec(A.D[1],{k:0 for k in A.D[1]})
T = 300

#print('test 1')
#w1a = gradient_descent(A,b,w_ones,s1,T)
#print('test 2')
#w1b = gradient_descent(A,b,w_ones,s2,T)

#print('test 3')
#w2a = gradient_descent(A,b,w_zeros,s1,T)
#print('test 4')
w2b = gradient_descent(A,b,w_zeros,s2,T)

AA,bb = read_training_data('validate.data')
print('validate:{0}'.format(fraction_wrong(AA,bb,w2b)))