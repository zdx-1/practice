"""
https://www.lanqiao.cn/problems/3549/learning
"""
n, m = map(int, input().split())
v = [0] + list(map(int, input().split()))
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, va = map(int, input().split())
    g[u].append(va)
    g[va].append(u)

tree = [0] * (n + 1)
a = [[0, 0] for _ in range(n + 1)]  # 存dfs序
cnt = 0


def dfs(node, fa):
    global cnt
    cnt += 1
    a[node][0] = cnt
    for i in g[node]:
        if i != fa:
            dfs(i, node)
    a[node][1] = cnt


dfs(1, 0)


def lowbit(x):
    return x & (-x)


def update(x, d):
    while x <= n:
        tree[x] ^= d
        x += lowbit(x)


def query(x):
    ans = 0
    while x:
        ans ^= tree[x]
        x -= lowbit(x)
    return ans


for i in range(1, n + 1):
    update(a[i][0], v[i])

for _ in range(m):
    o = list(map(int, input().split()))
    if o[0] == 2:
        print(query(a[o[1]][1]) ^ query(a[o[1]][0] - 1))
    else:
        x, y = o[1], o[2]
        update(a[x][0], v[x] ^ y)
        v[x] = y
