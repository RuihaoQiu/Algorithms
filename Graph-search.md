## Graph searching algorithm
In a m*n grid, walk from the most north-west point A to south-east point B, by taking the unit step towards either south or east in equal probability.

### Graph data structure
Following the the above rules, this code create the graph data structure.
```
import numpy as np
import random

m,n = 3,3
start = (0,0)
end = (m,n)

def make_graph(m, n):
    graph = dict()
    for i in range(m+1):
        for j in range(n+1):
            if i<m and j<n:
                graph[(i,j)] = [(i+1, j), (i, j+1)]
            elif i<m:
                graph[(i,j)] = [(i+1, j)]
            elif j<n:
                graph[(i,j)] = [(i, j+1)]
    return graph

graph = make_graph(m, n)
graph
```
{(0, 0): [(1, 0), (0, 1)],  <br/>
 (0, 1): [(1, 1), (0, 2)],  <br/>
 (0, 2): [(1, 2), (0, 3)],  <br/>
 (0, 3): [(1, 3)],  <br/>
 (1, 0): [(2, 0), (1, 1)],  <br/>
 (1, 1): [(2, 1), (1, 2)],  <br/>
 (1, 2): [(2, 2), (1, 3)],  <br/>
 (1, 3): [(2, 3)],  <br/>
 (2, 0): [(3, 0), (2, 1)],  <br/>
 (2, 1): [(3, 1), (2, 2)],  <br/>
 (2, 2): [(3, 2), (2, 3)],  <br/>
 (2, 3): [(3, 3)],  <br/>
 (3, 0): [(3, 1)],  <br/>
 (3, 1): [(3, 2)],  <br/>
 (3, 2): [(3, 3)]}

### Find a path
Randomly search for a path from all possible paths.
```
def find_a_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if len(graph[start]) == 2:
        node = graph[start][random.randint(0, 1)]
    else:
        node = graph[start][0]
    if node not in path:
        newpath = find_a_path(graph, node, end, path)
        if newpath: return newpath
    return None


a_path = find_a_path(graph, start, end)
a_path
```
[(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]

### Find all path
Greedy find all the paths.
```
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

all_paths = find_all_paths(graph, start, end)
all_paths
```

### Weighted nodes

**Assign a weight on each node**
```
## D mapping
def make_D(m, n):
    D = np.empty([m+1, n+1])
    for i in range(m+1):
        for j in range(n+1):
            D[i][j] = max(i*1./m-j*1./n, j*1./n-i*1./m)
    return D

D = make_D(m, n)
D
```
array([[ 0.        ,  0.33333333,  0.66666667,  1.        ],  <br/>
       [ 0.33333333,  0.        ,  0.33333333,  0.66666667],  <br/>
       [ 0.66666667,  0.33333333,  0.        ,  0.33333333],  <br/>
       [ 1.        ,  0.66666667,  0.33333333,  0.        ]])

**Calculate D for each path**
```
def calc_D(D, path):
    Ds = []
    for k in range(len(path)-1):
        i,j = path[k+1]
        Ds.append(D[i][j])
    return Ds

Ds = calc_D(D, a_path)
print("Total and average deviation of a path: {0:5.3f}, {1:6.2f}".format(sum(Ds), sum(Ds)/len(Ds)))

D_path = []
for path in all_paths:
    Ds = calc_D(D, path)
    D_path.append(sum(Ds)/len(Ds))

print("Average D for each path:\n", np.array(D_path))
```
Total and average deviation of a path: 1.00, 0.17  <br/>
Average D for each path: <br/>
 [ 0.5         0.38888889  0.27777778  0.27777778  0.27777778  0.16666667<br/>
  0.16666667  0.16666667  0.16666667  0.27777778  0.27777778  0.16666667<br/>
  0.16666667  0.16666667  0.16666667  0.27777778  0.27777778  0.27777778<br/>
  0.38888889  0.5       ]

**Calculate probability for each step**
```
## calculate probability
def get_prob(m, n):
    prob = dict()
    for i in range(m+1):
        for j in range(n+1):
            if i<m and j<n:
                prob[(i,j)] = 0.5
            else:
                prob[(i,j)] = 1
    return prob
```

**Calculate the mean and deviation of D**
```
## find all paths for m=3, n=3
m = 3; n = 3
D = make_D(m, n)
graph = make_graph(m,n)
prob = get_prob(m,n)
all_paths = find_all_paths(graph, start, end)

D_path = []
prob_path = []
for path in all_paths:
    D_sum = 0
    D_prob = 1
    for k in range(len(path)-1):
        i,j = path[k+1]
        D_sum = D_sum + D[i][j]
        D_prob = D_prob*prob[path[k]]
    prob_path.append(D_prob)
    D_path.append(D_sum/(len(path)-1))

mean = np.sum(np.multiply(prob_path, D_path))
std = np.sqrt(np.sum(np.multiply(prob_path, (D_path-mean)**2)))

print("The mean and standard deviation of D mean: {0:12.10f}, {1:12.10f}.".format(mean, std))
```

### Sampling method
When m, n is large, we are not able to search all path, therefore, we use random sampling method instead, to approximate the statistics we are interested in.

```
## sampling method

def sampling_method(m,n, n_steps=10000):
    D = make_D(m, n)
    graph = make_graph(m,n)
    D_all = []
    for i in range(n_steps):
        a_path = find_a_path(graph, start, (m,n))
        D_all.append(calc_D(D, a_path))

    print("Use sampling method, when m={0:2d}, n={1:2d}".format(m, n))
    print("The mean and standard deviation of D: {0:12.10f}, {1:12.10f}.".format(np.mean(D_all), np.std(D_all)))

## we can further calculate the condition probability by adding the following codes
    D_all = np.array(D_all).flatten()
    n_A = len([x for x in D_all if x>0.2])
    n_B = len([x for x in D_all if x>0.6])
    prob_BA = n_B/n_A
    print("Conditional probability that D is greater than 0.6 given that it is greater than 0.2: {0:12.10f}. \n".format(prob_BA))

sampling_method(30, 30)
```
Use sampling method, when m=30, n=30 <br/>
The mean and standard deviation of D: 0.1224730000, 0.1033561687.<br/>
Conditional probability that D is greater than 0.6 given that it is greater than 0.2: 0.0032789799.
