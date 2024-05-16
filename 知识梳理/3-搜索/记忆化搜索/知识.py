"""
记忆化搜索
1. 递归
2. 迭代
3. 迭代+记忆化搜索
4. 迭代+记忆化搜索+剪枝
5. 迭代+记忆化搜索+剪枝+动态规划
记忆化：通过记录已经遍历过的状态的信息，避免重复计算。
剪枝：通过判断当前状态是否满足条件，避免不必要的计算。
记忆化=dfs+额外存储空间
    如果状态已经计算过，直接返回结果，避免重复计算。
    如果状态没有计算过，计算结果，并记录下来，避免重复计算。
"""

# 斐波那契数列
'''使用字典'''
dic={0:1,1:1}
def fib(x):
    if x in dic.keys():
        return dic[x]
    dic[x]=fib(x-1)+fib(x-2)
    return dic[x]
print(fib(5))
'''使用装饰器注解'''
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(x):
    if x<=1:
        return 1
    return fib(x-1)+fib(x-2)
print(fib(100))