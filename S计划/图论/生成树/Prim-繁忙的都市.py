import os
import sys
n,m=map(int,input().split())
e=[]
for  _ in range(m):
    u,v,w=map(int,input().split())
    e.append((w,u,v))
#边按照权重进行排序
e.sort()
#需要一个并查集
p=list(range(n+1))

def findroot(x):
    if x==p[x]:return x
    else:
        p[x]=findroot(p[x])
        return p[x]
ans=0
#进行遍历所有的边，进行合并：
for w,u,v in e:
    #只要u和v不在同一集合内就可以进行合并：
    rootu=findroot(u)
    rootv=findroot(v)
    if rootu!=rootv:
        p[rootu]=rootv
        ans=max(ans,w)
print(n-1,ans)
