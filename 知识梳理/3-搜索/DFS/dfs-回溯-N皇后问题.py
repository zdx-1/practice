def dfs(x):
    #x层的皇后
    if x==n+1:
        global ans
        ans+=1
        return
    for y in range(1,n+1):
        #当前皇后的位置
        if vis1[y] or vis2[x+y] or vis3[x-y+n]:
            continue
        # 此时皇后的位置可以放置
        # 打标记
        vis1[y]=vis2[x+y]=vis3[x-y+n]=1
        dfs(x+1)
        # 清空标记
        vis1[y]=vis2[x+y]=vis3[x-y+n]=0


n=int(input())
# 三个数组分别表示横竖斜是否被标记
vis1=[0]*(n+1)
vis2=[0]*(2*n+1)
vis3=[0]*(2*n+1)
ans=0
dfs(1)
print(ans)