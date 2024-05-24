"""
https://www.lanqiao.cn/problems/1205/learning
"""
import math
def init_st(a):
    for i in range(1,n+1):
        d[i][0]=a[i]
#i,j  i,i+2^j-1
#i,j-1   i,i+2^(j-1)-1  i+2^(j-1),i+2^j-1  i+2^(j-1),j-1

#i+2^j-1<=n    i<=n+1-2^j
    for j in range(1,30):
        for i in range(1,n+1-(1<<j)+1):
            d[i][j]=max(d[i][j-1],d[i+(1<<(j-1))][j-1])

#l,r  
#2^k<=r-l+1 k取最大值
#k=int(log2(r-l+1))
#l,l+2^k-1     r-2^k+1,r
#d[l][k]    d[r-2^k+1][k]
def query(l,r):
    k=int(math.log2(r-l+1))
    return max(d[l][k],d[r-(1<<k)+1][k])

n,q=map(int,input().split())
a=[0]+list(map(int,input().split()))
d=[[0]*40 for i in range(n+1)]
init_st(a)
for i in range(q):
    li,ri=map(int,input().split())
    print(query(li,ri))



"""
import os
import sys
# 请在此输入您的代码
n,q=map(int,input().split())
N=list(map(int,input().split()))
for i in range(q):
  a=list(map(int,input().split()))
  m=a[0]
  n=a[1]
  print(max(N[m-1:n]))
"""