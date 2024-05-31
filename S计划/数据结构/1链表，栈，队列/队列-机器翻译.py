"""
https://www.lanqiao.cn/problems/511/learning/
"""
import os
import sys
from collections import deque
# 请在此输入您的代码
m,n=map(int,input().split())
t=[int(i) for i in input().split()]
q=deque()
s=0
for i in t:
  if i not in q:
    s=s+1
    if len(q)<=m-1:
      q.append(i)
    else:
      q.popleft()
      q.append(i)
print(s)