Maxn=200
fa=[]
def init():
    for i in range(Maxn+1):
        fa.append(i)
def find(i):
    if fa[i]==i:
        return i
    else:
        return find(fa[i])
init()
print(find(20))
#路径压缩版查询
def findx(x):
    if fa[x]==x:
        return x
    else:
        fa[x]=findx(fa[x])
        return fa[x]
    
print(findx(20))