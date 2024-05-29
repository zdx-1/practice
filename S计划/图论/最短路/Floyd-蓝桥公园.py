"""
https://www.lanqiao.cn/problems/1121/learning

Floyd 算法  多个起点--多个终点  多源最短路算法（多对多）
最简单的最短路径算法
存图:最简单的矩阵存图
效率不高，不能用于大图
动态规划：求图上两点i,j之间的最短距离，按‘从小图到全图’的步骤，在逐步扩大图的过程中计算和更新最短路
定义状态：dp[k][i][j]: i,j,k是点的编号，范围1--n
状态dp[k][i][j]表示在包含1--k点的子图上，点对i,j之间的最短路
状态转移方程 从子图1-k-1 扩展到子图 1-k
dp[k][i][j]=min(dp[k-1][i][j],dp[k-1][i][k]+dp[k-1][k][j])
初始值：i,j直连 就是他们的边长； 若不直连，赋值为无穷大 / 0x3f3f3f3f3f3f3f3f
滚动数组优化：dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
                          不经过k     经过k
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
只能用于n<300 的小规模图
"""


def floyd():
    global dp
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


n, m, q = map(int, input().split())
INF = 0x3f3f3f3f3f3f3f3f
dp = [[INF for _ in range(n + 50)] for _ in range(n + 50)]
for i in range(1, m + 1):
    u, v, w = map(int, input().split())
    dp[u][v] = dp[v][u] = min(dp[u][v], w)
floyd()
for _ in range(q):
    start, end = map(int, input().split())
    if dp[start][end] == INF:
        print(-1)
    elif start == end:
        print(0)
    else:
        print(dp[start][end])


#第二遍
def floyd():
    global dp
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


n, m, q = map(int, input().split())
INF = 0x3f3f3f3f3f3f3f3f3f
dp = [[INF for _ in range(n + 50)] for i in range(n + 50)]
for i in range(1, m + 1):
    u , v, w = map(int, input().split())
    dp[u][v] = dp[v][u] = min(dp[u][v], w)
floyd()
for _ in range(q):
    start, end = map(int, input().split())
    if dp[start][end] == INF:
        print(-1)
    elif start == end:
        print(0)
    else:
        print(dp[start][end])
