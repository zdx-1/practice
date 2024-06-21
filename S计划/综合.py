""" 综合知识考点 """

""" 线性DP """


def 破损的楼梯():
    # https://www.lanqiao.cn/problems/3367/learning
    N = int(1e5 + 10)
    mod = int(1e9 + 7)
    n, m = map(int, input())
    a = list(map(int, input().split()))
    vis = [0] * N
    for i in a:
        vis[i] = 1
    dp = [0] * N
    dp[0] = 1
    dp[1] = (1- vis[1])
    for i in range(2, n + 1):
        if vis[i]:
            continue
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    print(dp[n])


""" 二维DP """


def 数字三角形():
    # https://www.lanqiao.cn/problems/1536/learning
    import sys
    input = sys.stdin.readline
    N = int(input())
    dp = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] += dp[i - 1][j]
            elif j == i:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1])
    print(max(dp[-1]))


def 摆花():
    # https://www.lanqiao.cn/problems/389/learning
    MOD = int(1e6 + 7)
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    dp = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(min(a[i], j) + 1):
                dp[i][j] += dp[i - 1][j - k]
                dp[i][j] %= MOD
    print(dp[n][m])


def 选数异或():
    # https://www.lanqiao.cn/problems/3711/learning
    n, x = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    MOD = 998244353
    dp = [[0] * 64 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(64):
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j ^ a[i]]) % MOD
    print(dp[n][x])


""" LIS——最长上升子序列 """


def 蓝桥勇士():
    # https://www.lanqiao.cn/problems/2049/learning
    n = int(input())
    a = [0] + list(map(int, input().split()))
    dp = [1] * (n + 1)
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if a[i] < a[j]:
                dp[j] = max(dp[j], dp[i] + 1)
    print(max(dp))


def 合唱队形():
    # https://www.lanqiao.cn/problems/742/learning
    n = int(input())
    a = [0] + list(map(int, input().split()))
    dp1 = [0] * (n + 1)
    dp2 = [0] * (n + 1)
    for i in range(1, n + 1):
        dp1[i] = 1
        for j in range(1, i):
            if a[i] > a[j]:
                dp1[i] = max(dp1[i], dp1[j] + 1)
    for i in range(n, 0, -1):
        dp2[i] = 1
        for j in range(i + 1, n + 1):
            if a[i] > a[j]:
                dp2[i] = max(dp2[i], dp2[j] + 1)
    ans = max((dp1[i] + dp2[i] + 1) for i in range(1, n + 1))
    print(n - ans)


""" LCS——最长公共子序列 """


def 最长公共子序列():
    # https://www.lanqiao.cn/problems/1189/learning
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    dp = [[0] * (m + 1) for _ in range(2)]
    now = 0
    old = 1
    for i in range(1, n + 1):
        now, old = old, now
        for j in range(1, m + 1):
            dp[now][j] = max(dp[now][j - 1], dp[old][j])
            if a[i] == b[i]:
                dp[now][j] = max(dp[now][j], dp[old][j - 1] + 1)
    print(dp[now][m])


""" 01背包 """


def 小明的背包1():
    # https://www.lanqiao.cn/problems/1174/learning
    n, v = map(int, input().split())
    dp = [[0] * (v + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        wi, vi = map(int, input().split())
        for j in range(0, v + 1):
            if j >= wi:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wi] + vi)
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[n][v])


""" 完全背包 """


def 小明的背包2():
    # https://www.lanqiao.cn/problems/1175/learning
    n, v = map(int, input().split())
    dp = [[0] * (v + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        wi, vi = map(int, input().split())
        for j in range(0, v + 1):
            if (j >= wi):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - wi] + vi)
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[n][v])


""" 多重背包 """


def 小明的背包3():
    # https://www.lanqiao.cn/problems/4059/learning
    n, v = map(int, input().split())
    dp = [[0] * (v + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        wi, vi, si = map(int, input().split())
        for j in range(0, v + 1):
            for k in range(0, min(si, j // wi) + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k * wi] + k * vi)

    print(dp[n][v])


""" 二维费用背包&分组背包 """


def 小蓝的神秘行囊():
    # https://www.lanqiao.cn/problems/3937/learning
    n, v, m = map(int, input().split())
    dp = [[0] * (m + 1) for i in range(v + 1)]

    for i in range(1, n + 1):
        vi, mi, wi = map(int, input().split())
        for j in range(v, vi - 1, -1):
            for k in range(m, mi - 1, -1):
                dp[j][k] = max(dp[j][k], dp[j - vi][k - mi] + wi)

    print(dp[v][m])


""" KMP """


def 斤斤计较的小Z():
    # https://www.lanqiao.cn/problems/2047/learning
    Next = [0] * 1000010

    def get_next(T):
        for i in range(1, len(T)):
            j = Next[i]
            while j > 0 and T[i] != T[j]:
                j = Next[j]
            if T[i] == T[j]:
                Next[i + 1] = j + 1
            else:
                Next[i + 1] = 0

    def KMP(s, t):
        get_next(t)
        ans = 0
        j = 0
        for i in range(len(s)):
            while j > 0 and s[i] != t[j]:
                j = Next[j]
            if s[i] == t[j]:
                j += 1
            if j == len(t):
                ans += 1
                j = Next[j]
        return ans

    t = input()
    s = input()
    print(KMP(s, t))


""" Hash """


def 斤斤计较的小Z():
    # https://www.lanqiao.cn/problems/2047/learning
    t = input()
    s = input()
    m, n = len(t), len(s)
    B = 26
    mod = 1000000007
    hash = [0] * (n + 1)
    for i in range(1, n + 1):
        hash[i] = hash[i - 1] * B + ord(s[i - 1]) - ord('A')
        hash[i] %= mod

    numT = 0
    for c in t:
        numT = numT * B + ord(c) - ord('A')
        numT %= mod

    p = (B ** m) % mod
    ans = 0
    for l in range(1, n + 1):
        r = l + m - 1
        if r > n:
            break
        if (hash[r] - hash[l - 1] * p % mod + mod) % mod == numT:
            ans += 1
    print(ans)


""" 归并排序 """

""" 快速排序 """

""" Floyd——多源最短路 """


def 蓝桥公园():
    import sys
    input = sys.stdin.readline
    n, m, q = map(int, input().split())
    inf = int(1e18)
    dp = [[inf] * (n + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 0
    for i in range(1, m + 1):
        u, v, w = map(int, input().split())
        dp[u][v] = dp[v][u] = min(dp[u][v], w)
    #Floyd 模板
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j] == inf:
                dp[i][j] = -1

    for _ in range(q):
        s, e = map(int, input().split())
        print(dp[s][e])


""" Dijkstra——单源最短路 """


def 蓝桥王国():
    # https://www.lanqiao.cn/problems/1122/learning
    from queue import PriorityQueue  # 导入优先队列
    from collections import deque
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


""" Kruskal——最小生成树 """


def 繁忙的都市():
    # https://www.lanqiao.cn/problems/889/learning
    def kruskal():
        # 初始化
        n, m = map(int, input().split())
        Map = []
        for _ in range(m):
            u, v, w = map(int, input().split())
            Map.append([w, u, v])  # 注意第一个参数是边权
        Map.sort()

        # 并查集
        p = list(range(n + 1))

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


""" Prim——最小生成树 """


def 繁忙的都市2():
    # https://www.lanqiao.cn/problems/889/learning
    n, m = map(int, input().split())
    e = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        e.append((w, u, v))
    # 边按照权重进行排序
    e.sort()
    # 需要一个并查集
    p = list(range(n + 1))

    def findroot(x):
        if x == p[x]:
            return x
        else:
            p[x] = findroot(p[x])
            return p[x]

    ans = 0
    # 进行遍历所有的边，进行合并：
    for w, u, v in e:
        # 只要u和v不在同一集合内就可以进行合并：
        rootu = findroot(u)
        rootv = findroot(v)
        if rootu != rootv:
            p[rootu] = rootv
            ans = max(ans, w)
    print(n - 1, ans)


""" LCA——最近共同祖先 """
def 最近公共祖先LCA查询():
    # https://www.lanqiao.cn/problems/4385/learning
    #设置deep数组表示深度。
    #front数组，表示节点u,前2**i层的爹是谁？？？
    n=int(input())
    tree=[[] for _ in range(n+1)]
    fornt=[[0]*(21) for _ in range(n+1)]#如果你是0你就是孤儿。
    deep=[0]*(n+1)#0节点没有层数。
    for i in range(n-1):
        u,v=map(int,input().split())
        tree[u].append(v)

    def dfs(er,die):
        if die==0:
            deep[er]=1#这是第一层,同时，第一层也没有爹啊，也不需要更新如何层数相关节点。

        else:
            deep[er]=deep[die]+1#更新层数。
            fornt[er][0]=die#上一层的点，就是die。
            for cc in range(1,21):
                if fornt[fornt[er][cc-1]][cc-1]!=0:

                    fornt[er][cc]=fornt[fornt[er][cc-1]][cc-1]
                    #倍增法。2**i层之上的点=
                    #2**(cc-1)上面的点的上面2**(cc-1)的点。就，无限套娃。

        for i in tree[er]:
            dfs(i,er)#儿子变成新的爹。
    dfs(1,0)#儿子是根，爹不存在。

    def find(x,y):
        #第一步，拉升。将x拉到和y一个水平。一开始走2**20步，太大，就走2**19步，然后走一半，再走一半
        #就像那个乌龟与跑步哥一样。二进制原理使得这个步数遍历后一定是一个高度。
        for i in range(20,-1,-1):
            if deep[fornt[x][i]]>=deep[y] and fornt[x][i]!=0:
                x=fornt[x][i]#自动判断能走不能走，能走则走一大步。x提升到别的节点。

        #此时提升必定一样了。
        if x==y:
            return x#原来你就是我爹！

        else:#不是？我们再度提升吧！神明！
            for i in range(20,-1,-1):
                if fornt[x][i]!=fornt[y][i] and fornt[x][i]!=0 and fornt[y][i]!=0:#相等反而不能决定什么，因为可能不是最近的公共祖先
                    x=fornt[x][i]
                    y=fornt[y][i]
            return fornt[y][0]#最后，y上面的就是自己的公共祖先。
    q=int(input())
    for i in range(q):
        x,y=map(int,input().split())
        if deep[x]<deep[y]:#我们设x是深节点。
            x,y=y,x
        print(find(x,y))
