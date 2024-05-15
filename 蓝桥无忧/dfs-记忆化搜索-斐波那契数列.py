import sys
sys.setrecursionlimit(100000)
from functools import lru_cache
@lru_cache(maxsize=None)
def f(n):
    if n==0 or n==1:
        return 1
    return f(n-1)+f(n-2)

n=int(input())
print(f(n))