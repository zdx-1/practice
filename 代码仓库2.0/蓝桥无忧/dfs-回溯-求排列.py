def dfs(depth):
    if depth==n:
        print(path)
        return
    for i in range(1,n+1):
        if vis[i]:
            continue
        vis[i] = True
        path.append(i)
        dfs(depth+1)
        vis[i] = False
        path.pop(-1)

n=int(input())
vis=[False]*(n+1)
path=[]
dfs(0)