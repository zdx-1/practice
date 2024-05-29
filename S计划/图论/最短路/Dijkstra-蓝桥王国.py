# 1122_蓝桥王国_Dijkstra算法
from queue import PriorityQueue  # 导入优先队列

INF = 1e18


def dijkstra(s):
    # 返回从s出发到所有点的最短路
    # d[i]表示从s到i的最短路
    d = [INF] * (n + 1)
    # vis[i]表示是否出队列（注：与传统BFS不同）
    vis = [0] * (n + 1)
    q = PriorityQueue()

    # 1.将起点入队列，更新距离
    d[s] = 0
    # 将距离放在前面，才能对距离使用优先队列
    q.put((d[s], s))  # 入队用put()
    # 当队列非空
    while not q.empty():  # 或者写为： while len(q.queue) != 0:
        dis, u = q.get()
        # 每个点只有第一次出队列是有用的
        if vis[u]: continue
        vis[u] = 1  # 出队列打标记
        # 对于从u出发，到达v，权重为w的边
        for v, w in G[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                q.put((d[v], v))
    for i in range(1, n + 1):
        if d[i] == INF:
            d[i] = -1
    # d.pop(0)
    return d[1::]  # 从1到最后


# 皇宫编号为1
# 输入
n, m = map(int, input().split())
G = [[] for i in range(n + 1)]  # 图的存储：邻接表。此题N为10^5，不能用邻接矩阵存图

for i in range(m):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
print(*dijkstra(1))  # 列表前面加星号作用是将列表解开（unpacke）成多个独立的参数，传入函数。
