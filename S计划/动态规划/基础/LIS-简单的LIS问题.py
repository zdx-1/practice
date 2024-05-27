"""
8731 简单的LIS问题
https://www.lanqiao.cn/problems/8731/learning
"""
from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))[:n]
q = [-1]
chance = 1
res = 0
pre = None
for p, i in enumerate(nums):
    if pre != None:
        if i - pre > 1:
            chance -= 1
            res += 1
        pre = None
    if q[-1] < i:
        q.append(i)
    else:
        index = bisect_left(q, i)
        if chance and i - q[index - 1] > 1:
            res += 1
            chance -= 1
        elif chance and p == n - 1:
            res += 1
            chance -= 1
        elif chance and i == q[index]:
            pre = i
        q[index] = i
print(len(q) + res - 1)
