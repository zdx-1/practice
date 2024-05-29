n, m = map(int, input().split())
G = [[] for i in range(n + 1)]
rudu = [0] * (n + 1)
biaoji = [0] * (n + 1)
sum = [[0, i] for i in range(n + 1)]
for _ in range(n - 1):
    l, r = map(int, input().split())
    G[r].append(l)
    rudu[l] += 1
for i in range(1, n + 1):
    if rudu[i] == 0:
        root = i
def dfs(u):
    biaoji[u]=1
    sum[u][0]=-1
    for v in G[u]:
        if biaoji[v]==0:
            dfs(v)
            sum[u][0]+=sum[v][0]
dfs(root)
sum.sort()
for i,(x,y) in enumerate(sum,start=1):
    if y==m:
        print(i)
        break
