n=int(input())
a=list(map(int,input().split()))
path=[]
def dfs(depth):
    if depth ==n:
        print(path)
        return
    # 选
    path.append(a[depth])
    dfs(depth+1)
    path.pop(-1)
    # 不选
    dfs(depth+1)
dfs(0)