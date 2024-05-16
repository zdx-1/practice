"""
1190 LCIS
https://www.lanqiao.cn/problems/1190/learning
"""
import os
import sys

n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int , input().split()))

f = [0] * (m + 1)
ans = 0
for i in range(n):
    per = 0
    for j in range(m):
        if s[i] == t[j] and f[j + 1] < per + 1: f[j + 1] = per + 1
        if s[i] > t[j] and per < f[j + 1]: per = f[j + 1]
        if ans < f[j + 1]: ans = f[j + 1]
print(ans)