# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 1) Tuple Sum
def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    '''
    return [(x1+x2,y1+y2) for ((x1,y1),(x2,y2)) in zip(A, B)]



## 2: (Problem 2) Inverse Dictionary
def inv_dict(d):
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Examples:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'})
    {'merci':'thank you', 'au revoir':'goodbye'}]
    '''
    return {y:x for x,y in d.items()}



## 3: (Problem 3) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    return [p+i for i in range(n)]

comprehension_with_row = [row(i,20) for i in range(15)]

comprehension_without_row = [[i+p for i in range(20)] for p in range(15)]


f4 = {1:2,2:3,3:4,5:6,6:7}
p4 = {1:.5,2:.2,3:.1,5:.1,6:.1}
## 4: (Problem 4) Probability Exercise 1
Pr_f_is_even = sum([p4[k] for k,v in f4.items() if v % 2 == 0])
Pr_f_is_odd  = sum([p4[k] for k,v in f4.items() if v % 2 == 1])


f5 = {1:1,  2:2,  3:0,  4:1,  5:2,  6:0,  7:1}
p5 = {1:.2, 2:.2, 3:.2, 4:.1, 5:.1, 6:.1, 7:.1}
## 5: (Problem 5) Probability Exercise 2
Pr_g_is_1    = sum([p5[k] for k,v in f5.items() if v == 1])
Pr_g_is_0or2 = sum([p5[k] for k,v in f5.items() if v == 0 or v == 2])

