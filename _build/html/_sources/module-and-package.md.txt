## Module and package

### Module

A piece of script `example.py`

```
s = "Hello."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

if __name__ == '__main__':
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)
```

**Execute example**

```
import example
```

```
print(example.s)
print(example.a)
```
Hello.  
[100, 200, 300]

```
import example as my_module
print(my_module.s)
```
Hello.

```
from example import s
print(s)
```
Hello.

```
from example import foo
foo('abc')
```
arg = abc

```
from example import Foo
x = Foo()
x
```
<example.Foo at 0x10ecace80>

Run as standalone script
```
Python example.py
```
Hello.  
[100, 200, 300]  
arg = quux  
<\_\_main__.Foo object at 0x10ed7ed30>


**module search path**
```
import sys
sys.path
```
['',
 '/Users/qiuruihao/miniconda2/envs/py3/lib/python36.zip',
 '/Users/qiuruihao/miniconda2/envs/py3/lib/python3.6',
 '/Users/qiuruihao/miniconda2/envs/py3/lib/python3.6/lib-dynload',
 '/Users/qiuruihao/miniconda2/envs/py3/lib/python3.6/site-packages',
 '/Users/qiuruihao/miniconda2/envs/py3/lib/python3.6/site-packages/aeosa',
 '/Users/qiuruihao/miniconda2/envs/py3/lib/python3.6/site-packages/IPython/extensions',
 '/Users/qiuruihao/.ipython']

```
sys.path.append(r'C:\Users\john')
sys.path
```
['',
 '/Users/qiuruihao/miniconda2/envs/py3/lib/python36.zip',
 '/Users/qiuruihao/miniconda2/envs/py3/lib/python3.6',
 '/Users/qiuruihao/miniconda2/envs/py3/lib/python3.6/lib-dynload',
 '/Users/qiuruihao/miniconda2/envs/py3/lib/python3.6/site-packages',
 '/Users/qiuruihao/miniconda2/envs/py3/lib/python3.6/site-packages/aeosa',
 '/Users/qiuruihao/miniconda2/envs/py3/lib/python3.6/site-packages/IPython/extensions',
 '/Users/qiuruihao/.ipython', '/Users/john']

```
import example
example.__file__
```
'/Users/qiuruihao/Google Drive/Github/Python-notes/Notebooks/example.py'

**Reload module**
```
import example
import importlib
importlib.reload(example)
```


### Package
The `pkg` folder contains two scripts - `mod1.py` and `mod2.py`

*mod1.py*
```
def foo():
    print('[mod1] foo()')

class Foo:
    pass
```

*mod2.py*
```
def bar():
    print('[mod2] bar()')

class Bar:
    pass
```

execute
```
import pkg.mod1, pkg.mod2
pkg.mod1.foo()
```
[mod1] foo()
```
x = pkg.mod2.Bar()
x
```
<pkg.mod2.Bar object at 0x033F7290>

```
from pkg.mod1 import foo
foo()
```
[mod1] foo()

```
from pkg.mod2 import Bar as Qux
x = Qux()
x
```
<pkg.mod2.Bar object at 0x036DFFD0>


**package initialization**

If a file named `__init__.py` is present in a package directory, it is invoked when the package or a module in the package is imported. This can be used for execution of package initialization code, such as initialization of package-level data.

`__init__.py`
```
print(f'Invoking __init__.py for {__name__}')
A = ['quux', 'corge', 'grault']
print(f'Invoking __init__.py for {__name__}')
import pkg.mod1, pkg.mod2
```
```
import pkg
```
Invoking \_\_init__.py for pkg

```
pkg.A
```
['quux', 'corge', 'grault']

```
pkg.mod1.foo()
```
[mod1] foo()
```
pkg.mod2.bar()
```
[mod2] bar()


If `__init__.py` contains:
```
__all__ = [
        'mod1',
        'mod2',
        'mod3',
        'mod4'
        ]
```

```
dir()
```
['\_\_annotations__', '\_\_builtins__', '\_\_doc__', '\_\_loader__', '\_\_name__',
'\_\_package__', '\_\_spec__']

```
from pkg import *
dir()
```
['\_\_annotations__', '\_\_builtins__', '\_\_doc__', '\_\_loader__', '\_\_name__',
'\_\_package__', '\_\_spec__', 'mod1', 'mod2', 'mod3', 'mod4']

```
mod2.bar()
```
[mod2] bar()
```
mod4.Qux
```
<class 'pkg.mod4.Qux'>


**References**  
- https://realpython.com/python-modules-packages/
