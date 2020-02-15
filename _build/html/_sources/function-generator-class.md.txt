## Function, generator and class

### Function
A function can be seen as executable code blocks, which is reusable.
It start with the def keyword, a function name with input parameters, and use return to output values.

- Example
```
def f(x,y):
    return x*y
```
```
f(3,4)
```
12

- Print a sequence without for loop, a function can return itself
```
def f(x,y):
    print(x)
    if x < y:
        x = x + 1
        return f(x, y)
```
```
f(1,5)
```
1<br/>
2  
3<br/>
4  
5

- Binary search
```
## binary search : only for sorted array, repeatedly dividing the search interval in half, O(logN)
def binary_search(X, x, l, r):
    if r >= l:
        mid = l + (r - l)//2
        if X[mid] == x:
            return mid
        elif X[mid] > x:
            return binary_search(X, x, l=0, r=mid-1)
        else:
            return binary_search(X, x, l=mid+1, r=len(X))
    else:
        return "Not found!"
```
```
A = list(range(10))
binary_search(A, 7, l=min(A), r=max(A))
```
7

### Generator
A generator is an iterator, but we can only iterate over them once.
It use yield instead of return in function.

- Example
```
def generator_function(a_list):
    for i in a_list:
        yield i
a_list = list(range(10))
gf = generator_function(a_list)
```
```
next(gf)
```
0
```
next(gf)
```
1
```
for i in gf:
    print(i)
```
2<br/>
3  
4

- Batch generator  
a huge data set should be loaded in chunks.
```
A = list(range(10))
def batch_generator(A, batch_size):
    n = 0
    while True:
        data = A[n*batch_size:(n+1)*batch_size]
        n = n + 1
        if not data:
            break
        yield data
```
```
for s in batch_generator(A,2):
    print(s)
```
[0, 1]  
[2, 3]  
[4, 5]  
[6, 7]  
[8, 9]  

### Class
use `class` to define a class  
*object* can be another class  
`__int__` function initialize objects, whenever an instance of a class is created its `__init__` method is called  
`self` represents the class, all instance method should start with `self` in a class.
```
class Cal(object):
    pi = 3.142

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * (self.radius ** 2)

a = Cal(32)
a.area()
```
3217.408
