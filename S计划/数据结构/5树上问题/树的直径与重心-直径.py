"""
https://www.lanqiao.cn/problems/1394/learning
"""
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(u, fa, pre=None):
    global S
    if d[u] > d[S]: S = u
    for v, w in G[u]:
        if v == fa: continue
        d[v] = d[u] + w
        if pre: pre[v] = u
        dfs(v, u, pre)


n = int(input())
G = [[] for i in range(n + 1)]
d = [0] + (n + 1)
pre = [0] * (n + 1)
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

S = 1
dfs(1, 0)
d[S] = 0
dfs(S, 0, pre)
L = [S]

L_list = set()
while S != 0:
    L_list.add(S)
    S = pre[S]
for u in L_list:
    for i, (v, w) in enumerate(G[u]):
        if v in L_list:
            G[u][i] = [v, w - 1]

S = 1
dfs(1, 0)
d[S] = 0
dfs(S, 0)
L2 = d[S]
print(L)
print(L - L2)
