from collections import defaultdict
def dfs(u,dep,fa):
    global sum_depth
    sum_depth+=dep
    for v in e[u]:
        if v==fa:
            continue
        dfs(v,dep+1,u)
        siz[u]+=siz[v]
def dfs2(u,fa):
    for v in e[u]:
        if v==fa:
            continue
        dp[v]=dp[u]-2*siz[v]+n
        dfs2(v,u)
n=int(input())
dp=[0]*(n+1)
siz=[1]*(n+1)
e=defaultdict(list)
for _ in range(n-1):
    u,v=map(int,input().split())
    e[u].append(v)
    e[v].append(u)
sum_depth=0
dfs(1,0,0)
dp[1]=sum_depth
dfs2(1,0)
print(max(dp))
