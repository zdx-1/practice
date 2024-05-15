from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(x,y,tot,w)  :  #在（x,y)的数量tot,最大价值为w
    if x==n and y==m :
        if tot==k:
            return 1
        elif tot==k-1 and w<val[n][m]:
            return 1
        else:
            return 0

    ans=0
    for delta_x,delta_y in [(1,0),(0,1)]:
        xx,yy=x+delta_x,y+delta_y
        if 0<=xx<=n and 0<=yy<=m:
            ans+=dfs(xx,yy,tot,w)  #不选择
            if w<val[x][y]:
                ans+=dfs(xx,yy,tot+1,val[x][y])
    return ans%(10**9+7)
n,m,k=map(int,input().split())
val=[[0]*(m+1)]
for i in range(n):
    val.append([0]+list(map(int,input().split())))

print(dfs(1,1,0,-1))