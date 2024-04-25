import os
import sys

# 请在此输入您的代码
# 砝码称重
n=int(input())
list1=list(map(int,input().split()))
set1=set()
set1.add(0)
for i in list1:
  for j in list(set1):
    set1.add(i+j)
    set1.add(abs(i-j))
print(len(set1)-1)