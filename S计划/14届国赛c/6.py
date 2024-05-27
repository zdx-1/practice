import os
import sys


def find(x):
    if m[i] == 1:
        if s[-1] == 2:
            s[-1] += 1
        elif s[-1] > m[i + 1] and m[i + 1] != 0:
            m[i + 1] += 1
        else:
            s[-1] += 1
    else:
        s.append(m[i])


n = int(input())
m = list(map(int, input().split()))
s = []
if m[0] == 1:
    m[1] += 1
else:
    s.append(m[0])
for i in range(1, n - 1):
    if m[i] != 0:
        find(i)
if m[-1] == 1:
    s[-1] += 1
elif m[-1] != 0:
    s.append(m[-1])
k = 1
num = 0
for j in s:
    k = k * j
num += k
print(num % 1000000007)
