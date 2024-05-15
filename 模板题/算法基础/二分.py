"""
1217 解立方根
https://www.lanqiao.cn/problems/1217/learning

"""
import os
import sys
def check(x):
    return x ** 3 <= N
T = int(input())
while T:
    N = int(input())
    l, r = 0, N + 1
    while r - l > 1e-12:
        mid = (l + r) / 2
        if check(mid):
            l = mid
        else:
            r = mid
    print(f"{l:.3f}")
    T -= 1
