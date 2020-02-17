## Searching

### Linear search
search from left to right, return index when match, O(N)
```
def linear_search(X, x):
  for i in range(len(X)):
    if X[i]==x:
      return i
      break
```

### Binary search
only for sorted array, repeatedly dividing the search interval in half, O(logN)
```
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
