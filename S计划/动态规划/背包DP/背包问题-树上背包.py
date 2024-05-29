"""
1179 小明的背包6
https://www.lanqiao.cn/problems/1179/learning
"""

N, V = map(int, input().split())
g = [[] for i in range(N + 1)]
v = [0] * (N + 1)
w = [0] * (N + 1)
dp = [[0] * (V + 1) for _ in range(N + 1)]


def dfs(f):
    for i in range(v[f], V + 1):
        dp[f][i] = w[f]
    for pp in g[f]:
        dfs(pp)
        for j in range(V, v[f] + v[pp] - 1, -1):
            for k in range(v[pp], j - v[f] + 1):
                if k <= j:
                    dp[f][j] = max(dp[f][j], dp[f][j - k] + dp[pp][k])


for i in range(1, N + 1):
    v[i], w[i], x = map(int, input().split())
    g[x].append(i)
dfs(0)
print(dp[0][V])

"""
import sys
sys.setrecursionlimit(int(1e5))
n,V=map(int,input().split())
w=[0]*(n+1)
v=[0]*(n+1)
e=[[] for i in range(n+1)]
root =-1
for i in range(1,n+1):
    wi,vi,s=map(int,input().split())
    if s==0:
        root=i
    w[i]=wi
    v[i]=vi
    e[s].append(i)
dp=[[0]*(V+1) for i in range(n+1)]
def dfs(u):
    for j in range(w[u],V+1):
        dp[u][j]=v[u]
    for child in e[u]:
        dfs(child)
        for j in range(V,w[u]-1,-1):
            for k in range(w[child],min(j-w[u]+1,V+1)):
                dp[u][j]=max(dp[u][j],dp[u][j-k]+dp[child][k])
dfs(0)
print(dp[0][V])
"""
