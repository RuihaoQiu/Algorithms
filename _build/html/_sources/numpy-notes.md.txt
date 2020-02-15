## Numpy notes

Numpy is one of the most important package for data scientist. Here are some notes from my daily work.

### Import package
```
import numpy as np
```

### Create array
- create vector and matrix
```
vector = np.array([1, 2, 3, 4, 5, 6, 7, 8])
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
```
- zero and empty matrix
```
## input should be a tuple
m_zero = np.zeros((3, 3))
m_empty = np.empty((3, 3))
```
- diagonal matrix
```
np.fill_diagonal(m_zero, 5);
print(m_zero)
```
[[ 5.  0.  0.]  
 [ 0.  5.  0.]  
 [ 0.  0.  5.]]

- sequence
```
## from 0 to 2, step 0.2
np.arange(0, 2, 0.2)
```
array([ 0. ,  0.2,  0.4,  0.6,  0.8,  1. ,  1.2,  1.4,  1.6,  1.8])
```
## from 0 to 2, 10 points
np.linspace(0, 2, 10)
```
array([ 0.        ,  0.22222222,  0.44444444,  0.66666667,  0.88888889, 1.11111111,  1.33333333,  1.55555556,  1.77777778,  2.        ])


### Basic info
- number of axix
```
matrix.ndim
```
2
- shape
```
matrix.shape
```
(2, 4)
- number of elements
```
matrix.size
```
8
- data type
```
matrix.dtype
```
dtype('int64')


### Basic operations
- element-wise
```
a = np.array([[1,1], [0,1]])
b = np.array([[2,0], [3,4]])
a + b
```
array([[3, 1], [3, 5]])
```
a.add(b)
```
array([[3, 1], [3, 5]])
```
## multiple, two are same
a * b
np.multiply(a, b)
```
array([[2, 0], [0, 4]])
```
np.sqrt(b)
```
array([[ 1.41421356,  0.        ], [ 1.73205081,  2.        ]])

- matrix operator
```
np.dot(a, b)
```
array([[5, 4], [3, 4]])
```
np.matmul(a, b)
```
array([[5, 4], [3, 4]])

- sum, min, max
```
np.sum(a, axis=1)
```
array([2, 1])
```
np.min(a, axis=0)
```
array([0, 1])

### Select
```
vector[2:5]
```
array([3, 4, 5])
```
matrix[1:3, 2]
```
array([7])
```
matrix[:, 1:3]
```
array([[2, 3], [6, 7]])

### Transform
- transpose
```
print(matrix.T)
```
[[1 5]  
 [2 6]  
 [3 7]  
 [4 8]]

- reshape
```
print(vector.reshape(2,4))
```
[[1 2 3 4]  
 [5 6 7 8]]
```
## keep 2d, -1 automatically calculate dimension
matrix.reshape(-1, 8)
```
array([[1, 2, 3, 4, 5, 6, 7, 8]])
```
## covert to 1d
matrix.reshape(8)
```
array([1, 2, 3, 4, 5, 6, 7, 8])
```
## same as above
matrix.ravel()
matrix.flatten()
```
array([1, 2, 3, 4, 5, 6, 7, 8])

- stack  
```
## input should be a tuple
np.hstack((a, b))
```
array([[1, 1, 2, 0], [0, 1, 3, 4]])
```
np.vstack((a, b))
```
array([[1, 1],[0, 1],[2, 0],[3, 4]])
