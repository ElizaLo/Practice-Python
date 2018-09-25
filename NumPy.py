import numpy as np
import time
import sys


a = np.array([1,2,3])
print(a)

b = np.array([[1,2,3], [4,5,6]])
print(b)

S = range(1000)
print(S)
print(sys.getsizeof(5)*len(S)) # List - size of one element multiplied by the number of all elements, so we got the size of all elements
print(sys.getsizeof(5)) #size of one element

D = np.arange(1000)
print(D.size * D.itemsize) # NumPy - size of one element multiplied by the number of all elements, so we got the size of all elements

SIZE = 1000000
L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [(x,y) for x,y in zip(L1, L2)]

print ((time.time() - start) * 1000 ) #runtime of List

start = time.time()
result = A1 + A2

print ((time.time() - start) * 1000 ) #runtime of Numpy


a = np.array([(1,2,3),(2,3,4)])
print(a.ndim) #dimention of array
print(a.itemsize) #byte size of each element
print(a.dtype) #data type
print(a.size) #size of array
print(a.shape) #shape of array
a = a.reshape(3, 2) #reshape into 3 rows and 2 collums
print(a)

a = np.array([(1,2,3),(2,3,4),(5,6,8)])
print(a[0:2,1]) #slicing

a = np.linspace(1,3,10) #slicing
print(a)

a = np.array([(1,2,3),(2,3,4),(5,6,8)])
print(a.max())
print(a.min())
print(a.sum())
