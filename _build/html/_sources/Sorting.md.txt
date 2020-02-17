## Sorting

Some common sorting algorithms.

```
import random
A = list(range(10))
```

### Simple sorts
Complexity - O(N^2)

**bubble sort** - pair exchange until sorted
```
random.shuffle(A)

def bubble_sort(X):
  changed = True
  while changed:
    changed = False
    for i in range(len(X) - 1):
      if X[i] > X[i+1]:
        X[i], X[i+1] = X[i+1], X[i]
        changed = True
  return X

print("Before sort: ", A)
print("After sort: ", bubble_sort(A))
```
Before sort:  [7, 5, 1, 3, 6, 9, 0, 8, 2, 4] <br/>
After sort:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

**insertion sort** - from left to right, insert next element to the sorted array
```
random.shuffle(A)

def insertion_sort(X):
  for i in range(1, len(X)):
    j = i-1
    key = X[i]
    while (X[j] > key) and (j >= 0):
      X[j+1] = X[j]
      j -= 1
      X[j+1] = key
  return X

print("Before sort: ", A)
print("After sort: ", insertion_sort(A))
```
Before sort:  [5, 0, 3, 4, 9, 8, 7, 2, 1, 6]  <br/>
After sort:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

**selection sort** - from left to right, find the minimum of the right part stack to the left
```
random.shuffle(A)
def selection_sort(X):
  for i, e in enumerate(X):
    mn = min(range(i,len(X)), key=X.__getitem__) ## find the minimum for i to len(X)
    X[i], X[mn] = X[mn], e
  return X

print("Before sort: ", A)
print("After sort: ", selection_sort(A))
```
Before sort:  [2, 0, 1, 9, 3, 4, 6, 5, 8, 7]  <br/>
After sort:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


### Efficient sorts
Complexity - O(NlogN)

**quick sort** - recursively choose pivots, put the smaller values at left and the larger at right. Worst case may cause *O(N**2)*, but normally random choose of pivot will cause *O(N*logN)*
```
def quick_sort(X):
  less = []
  pivots = []
  more = []

  if len(X) <= 1:
    return arr
  else:
    pivot = X[0]
    for i in X:
      if i < pivot:
        less.append(i)
      elif i > pivot:
        more.append(i)
      else:
        pivots.append(i)
    less = quickSort(less)
    more = quickSort(more)

  return less + pivots + more
```

**merge sort** - sequentially append maximum and minimum the two list, then append them

```
def merge_sort(X):
  start = []
  end = []
  while len(X) > 1:
    s = min(X)
    e = max(X)
    start.append(s)
    end.append(e)
    X.remove(s)
    X.remove(e)
  if X: start.append(X[0])
  end.reverse()
  return start + end
```

**heap sort** - continuesly creat max heap to find the largest value and stack it
```
def heapify(X, index, heap_size):
  mx = index
  l = 2 * index + 1
  r = 2 * index + 2
  if l < heap_size and X[l] > X[mx]:
    mx = l
  if r < heap_size and X[r] > X[mx]:
    mx = r
  if mx != index:
    X[mx], X[index] = X[index], X[mx]
    heapify(X, mx, heap_size)

def heap_sort(X):
  n = len(X)
  for i in range(n // 2 - 1, -1, -1):
    heapify(X, i, n)
  for i in range(n - 1, 0, -1):
    X[0], X[i] = X[i], X[0]
    heapify(X, 0, i)
  return X
```

**Reference**
- [https://en.wikipedia.org/wiki/Sorting_algorithm#Simple_sorts](https://en.wikipedia.org/wiki/Sorting_algorithm#Simple_sorts)
