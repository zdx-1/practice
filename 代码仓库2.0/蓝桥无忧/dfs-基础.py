x=int(input())
n=int(input())

# path[i]表示当前深度的数字
path=[0]*n

def dfs(depth):
    # depth：当前深度
    # 递归出口
    if depth==n:
        # 判断数字是否递增
        for i in range(1,n):
            if path[i]>=path[i-1]:
                continue
            else:
                return
        if sum(path)!=x:
            return
        print(path)
        return
    # 对于每一层，遍历所有可能
    for i in range(1,x+1):
        path[depth]=i
        dfs(depth+1)


dfs(0)