"""
https://www.lanqiao.cn/problems/4385/learning
"""
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(u, fa):
    deep[u] = deep[fa] + 1
    p[u][0] = fa
    for i in range(1, 20):
        p[u][i] = p[p[u][i - 1]][i - 1]
    for v in G[u]:
        if v == fa: continue
        dfs(v, u)


def LCA(x, y):
    if deep[x] < deep[y]:
        x, y = y, x
    for i in range(20, -1, -1):
        if deep[p[x][i]] >= deep[y]:
            x = p[x][i]
    if x == y:
        return x
    for i in range(20, -1, -1):
        if p[x][i] != p[y][i]:
            x = p[x][i]
            y = p[y][i]
    return p[x][0]


n = int(input())
G = [[] for _ in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
deep = [0] * (n + 1)
p = [[0] * 21 for _ in range(n + 1)]
dfs(1, 0)
q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    print(LCA(a, b))
