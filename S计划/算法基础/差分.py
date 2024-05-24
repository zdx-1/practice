"""
1276 小明的彩灯
https://www.lanqiao.cn/problems/1276/learning
"""
import os
import sys
#一维差分是指给定一个长度为n的序列a，
#要求支持操作pro(l,r,c)表示对a[l]~a[r]区间上的每一个值都加上或减去常数c，并求修改后的序列a。
'''
N,Q=map(int,input().split())
a=list(map(int,input().split()))
for i in range(Q):
  l,r,x=map(int,input().split())
  for j in range(l-1,r,1):
    a[j]+=x
for i in range(len(a)):
  if a[i]<0:
    a[i]=0
print(" ".join(map(str,a)))
    运行超时！！！！！！！！！！
'''


num,time = map(int,input().split())#输入彩灯数量和操作次数
light = list(map(int,input().split()))#初始亮度
op = [0 for i in range(num)]
for i in range(time):
    l,r,x=map(int,input().split())
    op[l-1] += x#l-1处加x
    if r < num:
        op[r] -= x#r处减x
for i in range(1,num):
    op[i] += op[i-1]#取前缀和
for i in range(num):
    print(max(light[i]+op[i],0),end = ' ')

