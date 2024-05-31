def kruskal():
    # 初始化
    n, m = map(int, input().split())
    Map = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        Map.append([w, u, v])  # 注意第一个参数是边权
    Map.sort()

    # 4并查集
    p = list(range(n+1))
    def root(x):
        if x != p[x]:
            p[x] = root(p[x])
        return p[x]

    # 非连环时更新
    _sum, _max = 0, 0
    for w, u, v in Map:
        root_u = root(u)
        root_v = root(v)
        if root_u != root_v:
            p[root_u] = root_v
            _sum += 1
            _max = max(_max, w)
    return _sum, _max
print(*kruskal())
