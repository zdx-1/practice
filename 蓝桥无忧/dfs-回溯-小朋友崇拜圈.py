# 182
import sys
# 扩栈，如果递归次数过多会出现段错误
sys.setrecursionlimit(1e5)

def dfs(x,length):
    #print(x,length)
    #记录当前x,已经走了length步
    vis[x]=length

    #如果下一步已经走过，则说明当前已经进入了一个圈
    if vis[a[x]]:
        #更新最大圈
        global ans
        ans=max(ans,length-vis[a[x]]+1)
    #下一步没走过，走下一步
    else:
        dfs(a[x],length+1)

n=int(input())
a=list(map(int,input().split()))
a=[0]+a
vis=[0]*(n+1)
ans=0
for i in range(1,n+1):
    if vis[i]==0:
        dfs(i,1)
print(ans)