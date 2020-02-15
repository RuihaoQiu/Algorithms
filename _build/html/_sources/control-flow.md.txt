## Control flow
Some basic control flow statements.

### for loop
```
a_list = ["a", "b", "c", "d"]

## print both index and item
for n, item in enumerate(a_list):
    print(n, item)
## after loop
else:
    print('done!')
```
0 a  
1 b  
2 c  
3 d  
done!

### if else
```
a_list = ["a", "b", "c", "d"]

## if/else within loop
for n, item in enumerate(a_list):
    if n % 2 == 0:
        print(n, item)
    else:
        print(item)
## after loop
else:
    print('done!')
```
0 a  
b<br/>
2 c  
d<br/>
done!

### while
```
import random

running = True
while running:
    x = random.randint(0,10)
    print(x)
    if x > 5:
        print(x, ' is over 5')
        running = False
```
0<br/>
9<br/>
9 is over 5

### break, continues
- break, breaks out of the innermost loop.
- continue, continues with the next iteration of the loop.

```
for num in range(5):
    if num < 4:
        print(num, "< 4")
    else:
        break
```
0 < 3  
1 < 3  
2 < 3  

```
for num in range(5):
    if num % 2 == 0:
        print(num, "even number")
        continue
    print(num, "odd number")
```
0 even number  
1 odd number  
2 even number  
3 odd number  
4 even number  
