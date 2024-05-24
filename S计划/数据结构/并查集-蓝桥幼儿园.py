"""
https://www.lanqiao.cn/problems/1135/learning
"""
# def Findroot(x):
#     while x!=p[x]:
#         x=p[x]
#     return x
'''使用路径压缩'''
def Findroot(x):
    if x==p[x]:return x
    #路径压缩
    p[x]=Findroot(p[x])
    return p[x]
def Merge(x,y):
    rootx,rooty=Findroot(x),Findroot(y)
    p[rootx]=rooty
def Query(x,y):
    rootx,rooty=Findroot(x),Findroot(y)
    return rootx==rooty
n,m=map(int,input().split())
p=list(range(n+1))
for _ in range(m):
    op,x,y=map(int,input().split())
    if op ==1:
        Merge(x,y)
    else:
        if Query(x,y):
            print("YES")
        else:
            print("NO")