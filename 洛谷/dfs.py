x,n=map(int,input().split())
path=[0]*n
def dfs(depth):
    #depth为当前深度
    if depth==n:return#递归出口
    for i in range(1,x+1):
        path[depth]=i
        dfs(depth+1)
        print(path)

dfs(x)
print(path)