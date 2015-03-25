# version code 3ebd92e7eece+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from vec import Vec
from independence import is_independent


## 1: (Task 1) Choosing a Secret Vector
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    while(True):
      u = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
      if (a0*u == s and b0*u == t):
        return u

def getVecs():
  while(True):
    a1 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    b1 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    a2 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    b2 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    a3 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    b3 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    a4 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    b4 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])

    vecs = [a0,b0,a1,b1,a2,b2,a3,b3,a4,b4]
    result = [is_independent([vecs[x],vecs[x+1],vecs[y],vecs[y+1],vecs[z],vecs[z+1]]) 
              for x in range(0,10,2) for y in range(x+2,10,2) for z in range(y+2,10,2)]
  
    if all(result):
      return vecs
          

## 2: (Task 2) Finding Secret Sharing Vectors
# Give each vector as a Vec instance
secret_a0 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: one, 4: 0, 5: one})
secret_b0 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: 0, 4: 0, 5: one})
secret_a1 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: one, 3: 0, 4: 0, 5: one})
secret_b1 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: one, 3: one, 4: one, 5: 0})
secret_a2 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: 0, 4: 0, 5: 0})
secret_b2 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0})
secret_a3 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: one, 3: 0, 4: 0, 5: 0})
secret_b3 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: one, 3: 0, 4: one, 5: 0})
secret_a4 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: one, 3: one, 4: 0, 5: one})
secret_b4 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 0, 3: one, 4: one, 5: 0})

