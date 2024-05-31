N = 2005
e = [[] for _ in range(N)]
w = [[] for _ in range(N)]
dp = [0] * N
n, m, k = 0, 0, 0
dep = [0] * N
f = [0] * N
t = []


def dfs(u):
    global dp, e, w
    for v in e[u]:
        dfs(v)
        dp[u] += dp[v]
    for t in w[u]:
        sum = dp[u]
        for nw in t['vec']:
            sum -= dp[nw]
            for v in e[nw]:
                sum += dp[v]
        dp[u] = max(dp[u], sum + t['val'])


n, m = map(int, input().split())
for i in range(2, n + 1):
    f[i] = int(input())
    e[f[i]].append(i)
    dep[i] = dep[f[i]] + 1
for i in range(1, m + 1):
    x, y, val = map(int, input().split())
    t.clear()
    while x != y:
        if dep[x] > dep[y]:
            t.append(x)
            x = f[x]
        else:
            t.append(y)
            y = f[y]
    t.append(x)
    w[x].append({'vec': list(t), 'val': val})
dfs(1)
print(dp[1])
