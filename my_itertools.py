from collections.abc import Iterable
from typing import TypeVar

_T = TypeVar("_T")


class _Unique:
    """
    Name from Japanese '特異'
    """
    pass

_unique = _Unique()

def zip(*ls:Iterable[_T], strict=False):
    n = len(ls)
    ls = [iter(l) for l in ls]
    try:
        while True:
            ans = ()
            for l in ls:
                ans += (next(l), )
            yield ans
    except StopIteration:
        if strict:
            if ans.__len__() == 0:
                return
            else:
                raise ValueError("All iterables should be size-equally when strict was set as True.")
        else:
            return


def _copy(a):
    return a

def count(start=0, step=1):
    while True:
        yield start
        start += step

def cycle(p):
    while True:
        for elem in p:
            yield elem

def repeat(elem, n=None):
    if n is None:
        while True:
            yield elem
    else:
        while n:=n-1:
            yield elem

def accumulate(p, func=None, *, initial=None):
    if func is None:
        func = p[0].__add__
    for elem in p:
        if initial is None:
            initial = elem
        else:
            initial = func(initial, elem)
        yield initial

def chain(*ls):
    for l in ls:
        for elem in l:
            yield elem
   

def chain_from_iteratable(ls):
    for elem in chain(*ls):
        yield elem

def compress(data, selectors):
    # TODO
    for d, s in zip(data, selectors):
        if s:
            yield d

def dropwhile(pred, seq):
    start : bool = False
    for elem in seq:
        if start:
            yield elem
        else:
            if not pred(elem):
                start = True
                yield elem


def groupby(iterable, keyfunc=None):
    """
    Warning: There are some details which should be mentioned
        when using this function
    ## Introduction
    This function is used as
    ```python
    # Example 1
    for k, l in my_itertools.groupby([1,-1,2,3,-3,3,1], keyfunc=lambda a: return a if a>=0 else -a):
        print(k, list(l))
    ```
    and result is
    ```bash
    1 [1, -1]
    2 [2]
    3 [3, -3, 3]
    1 [1]
    ``` 
    Every time the functions yields, it yields one val `k` and
    one iterable function `l`. On the Example 1, we turned the 
    iterable `l` into list. On the Example 2, we will `for` the 
    iterable `l`.
    ```python
    # Example 2
    for k,l in my_itertools.groupby([1,2,2,3,3,1]):    
        print(k)
        for e in v:
            print(' ' + str(e))
    ```
    Result is 
    ```bash
    1
     1
    2
     2
     2
    3
     3
     3
    1
     1
    ```
    Also recommend reading this blog (in Chinese)`https://blog.csdn.net/carol_in_love/article/details/81435837`
    ## Warning
    1. The iteratable function `l` can be used only once.
    You should not write as below.
    ```python
    for k,l in my_itertools.groupby([1,2,2,3,3,1]):    
        print(k)
        for e in v:
            print(' ' + str(e))
        for e in v:
            print(' ' + str(e))
 
    ```

    2. You **Should not** store the iterable function yielded as 
    the second value (such as the `l` in the example 1 and 2) 
    and use it out of the `for` clause where `my_itertools.groupby()` 
    is called. For example, you should not write your code as 
    Example 4. If you need store the data in the iterable, you
    can try other way.
    ```python
    # Example 4
    k0 = None
    l0 = None
    for k,l in my_itertools.groupby([1,2,2,3,3,1]):    
        # you can use the iterable `l` here
        if k0 is None:
            k0 = k
            l0 = l
    # but you should not use it under this line even if you 
    # stored it
    print(k)
    for elem in l0:  
        print('\t' + str(elem))
    ```
    """
    global _unique
    if keyfunc is None:
        keyfunc = _copy
    
    ls = []
    def f():
        for elem in ls:
            yield elem
    
    k = _unique
    for elem in iterable:
        cur_val = keyfunc(elem)
        if cur_val == k:
            ls.append(elem)
        else:
            if k is _unique:
                k = cur_val
            else:
                yield k, f()
                k = cur_val
            ls = [elem]
    if ls.__sizeof__() != 0:
        yield k, f()
        
def filterfalse(pred, seq):
    if pred is None:
        pred = _copy

    for elem in seq:
        if not pred(elem):
            yield elem

def islice(seq, start, stop=None, step=None):
    pass

def pairwise(s):
    pass

def starmap(fun, seq):
    pass

def tee(it, n=2):
    pass

def takewhile(pred, seq):
    pass

def zip_longest(*l):
    pass

def product(*l, repeat=1):
    pass

def permutations(p, r=None):
    pass

def combinations(p, r):
    pass

def combinations_with_replacement(p, r):
    pass






