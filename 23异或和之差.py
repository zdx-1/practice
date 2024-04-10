n = int(input())
q = list(map(int, input().split()))

son = {}
idx = 0
mx = [0]*(n+10)
mn = [10**9]*(n+10)

def insert(x):
    global idx
    p = 0
    for i in range(20, -1, -1):
        u = (x >> i) & 1
        if (u, p) not in son:
            idx += 1
            son[(u, p)] = idx
        p = son[(u, p)]

def query1(x):
    p = 0
    res = 0
    for i in range(20, -1, -1):
        u = x >> i & 1
        if (u, p) not in son:
            u = not u
            res |= 1 << i
        p = son[(u, p)]
    return res

def query2(x):
    p = 0
    res = 0
    for i in range(20, -1, -1):
        u = x >> i & 1
        if (not u, p) in son:
            res |= 1 << i
            u = not u
        p = son[(u, p)]
    return res

sum_ = 0
insert(0)
for i in range(1, n+1):
    sum_ = sum_ ^ q[i-1]
    mx[i] = max(mx[i - 1], query2(sum_))
    mn[i] = min(mn[i - 1], query1(sum_))
    insert(sum_)

son = {}
idx = 0
sum_ = 0
insert(0)

res = 0
a = 0
b = 2e9
for i in range(n, 0, -1):
    sum_ = sum_ ^ q[i-1]
    a = max(a, query2(sum_))
    b = min(b, query1(sum_))
    res = max(res, max(mx[i - 1] - b, a - mn[i - 1]))
    insert(sum_)

print(res)