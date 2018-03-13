import numpy as np
import math
inputSize = 3
outputSize = 1

X = np.array([0.15,0.49,0.87],dtype=float)

dev=[]
new=[]
alpha = 0.3
targ = 1

w = np.random.rand(inputSize,outputSize)
print "weights:"
print w

ok = np.dot(X, w)
#print ok

def sigmoid(s):
    return 1/(1+np.exp(-1))

op = sigmoid(ok)
sk = alpha*(targ - op)*(op)*(1-op)
#print sk

avg = np.mean(X)

for i in X:
    dev.append(avg - i)

#print de    

for j in X:
    for k in dev:
          new.append(j - (sk*k))
          break
print new          
