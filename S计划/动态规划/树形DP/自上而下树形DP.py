from collections import defaultdict

n = int(input())
val = [0] + [int(x) for x in input().split()]
edges = defaultdict(list)
f = [[0, val[i]] for i in range(n + 1)]


def add_egge(from_node, to_node):
    edges[from_node].append(to_node)


def dfs(u, fa):
    for v in edges[u]:
        if v == fa:
            continue
        dfs(v, u)
        f[u][0] += max(f[v][0], f[v][1])
        f[u][1] += f[v][0]


for _ in range(n - 1):
    u, v = map(int, input().split())
    add_egge(u, v)
    add_egge(v, u)

dfs(1, 0)
print(max(f[1][0], f[1][1]))
