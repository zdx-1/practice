ans=0
def dfs(depth,n,m):
    if depth ==7:
        if n==0 and m==0:
            global ans
            ans+=1
        return
    for i in range(0,6):
        for j in range(0,6):
            if 2<=i+j<=5 and i<=n and j<=m:
                dfs(depth+1,n-i,m-j)
dfs(0,9,16)
print(ans)