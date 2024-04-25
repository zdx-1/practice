import heapq

class Gas:
    def __init__(self, id, c):
        self.id = id
        self.c = c

    def __lt__(self, other):
        return self.c < other.c

maxn = 200005
INF = 1e18
n, m = 0, 0
dis = [0] * maxn
lim = [0] * maxn
cost = [0] * maxn
ans, vol = 0, 0

rest = [0] * (maxn << 2)
k = [0] * (maxn << 2)

def build(i, l, r):
    if l == r:
        rest[i] = 0
        return
    mid = (l + r) >> 1
    build(i << 1, l, mid)
    build(i << 1 | 1, mid + 1, r)
    rest[i] = max(rest[i << 1], rest[i << 1 | 1])

def pd(i):
    if k[i] != 0:
        k[i << 1] += k[i]
        k[i << 1 | 1] += k[i]
        rest[i << 1] += k[i]
        rest[i << 1 | 1] += k[i]
        k[i] = 0

def query(i, l, r, ll, rr):
    if ll <= l and r <= rr:
        return rest[i]
    pd(i)
    res = 0
    mid = (l + r) >> 1
    if mid >= ll:
        res = max(res, query(i << 1, l, mid, ll, rr))
    if mid < rr:
        res = max(res, query(i << 1 | 1, mid + 1, r, ll, rr))
    rest[i] = max(rest[i << 1], rest[i << 1 | 1])
    return res

def add(i, l, r, ll, rr, v):
    if ll <= l and r <= rr:
        rest[i] += v
        k[i] += v
        return
    pd(i)
    mid = (l + r) >> 1
    if mid >= ll:
        add(i << 1, l, mid, ll, rr, v)
    if mid < rr:
        add(i << 1 | 1, mid + 1, r, ll, rr, v)
    rest[i] = max(rest[i << 1], rest[i << 1 | 1])

def solve():
    global n, m, vol, ans
    n, m = map(int, input().split())
    # print(n, m)
    vol = m
    q = []
    for i in range(1, n + 1):
        dis[i], cost[i], lim[i] = map(int, input().split())
        # print(dis[i], cost[i], lim[i])
    build(1, 1, n)
    for i in range(1, n + 1):
        vol -= dis[i]
        while vol < 0:
            if len(q) == 0:
                print(-1)
                return
            a = heapq.heappop(q)
            cnt = min(m - query(1, 1, n, a.id, i - 1), lim[a.id])
            if cnt <= 0:
                continue
            if cnt <= -vol:
                ans += a.c * cnt
                vol += cnt
                lim[a.id] = 0
                add(1, 1, n, a.id, i - 1, cnt)
            else:
                ans += a.c * (-vol)
                lim[a.id] = cnt + vol
                add(1, 1, n, a.id, i - 1, -vol)
                heapq.heappush(q, Gas(a.id, a.c))
                vol = 0
        if vol > 0:
            add(1, 1, n, i, i, vol)
        lim[i] = min(lim[i], m - vol)
        heapq.heappush(q, Gas(i, cost[i]))
    print(ans)

if __name__ == "__main__":
    solve()