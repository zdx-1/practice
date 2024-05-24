import bisect

mxn = 1000006
pre = [0] * mxn
st = [False] * mxn
v = []
mp = {}

cnt = 0

for i in range(2, mxn):
    if not st[i]:
        pre[cnt] = i
        cnt += 1
        mp[i] = True
    j = 0
    while i * pre[j] < mxn:
        st[i * pre[j]] = True
        if i % pre[j] == 0:
            break
        j += 1

for i in range(cnt - 1, -1, -1):
    v.append(pre[i] - 2 * pre[i])

for i in range(cnt):
    v.append(pre[i])

v.sort()
pre = v
cnt = 2 * cnt

n, m = map(int, input().split())

a = [0] * (n + 1)
dp = [0] * (n + 1)

a[1:n + 1] = map(int, input().split())

for _ in range(m):
    op, k, x = map(int, input().split())
    for i in range(k, n + 1, k):
        if op == 2:
            t = abs(a[i])
            if t not in mp:
                idx = bisect.bisect_left(pre, a[i])
                if idx + x - 1 >= cnt:
                    a[i] = pre[cnt - 1]
                    dp[i] += idx + x - 1 - cnt + 1
                else:
                    a[i] = pre[idx + x - 1]
            else:
                dp[i] += x
        else:
            t = abs(a[i])
            if t not in mp:
                idx = bisect.bisect_right(pre, a[i])
                if idx - x < 0:
                    a[i] = pre[0]
                    dp[i] -= x - idx
                else:
                    a[i] = pre[idx - x]
            else:
                dp[i] -= x

for i in range(1, n + 1):
    if dp[i]:
        if dp[i] > 0:
            idx = bisect.bisect_right(pre, a[i])
            if idx + dp[i] - 1 >= cnt:
                a[i] = 1
            else:
                a[i] = pre[idx + dp[i] - 1]
        else:
            idx = bisect.bisect_left(pre, a[i])
            if idx + dp[i] < 0:
                a[i] = 0
            else:
                a[i] = pre[idx + dp[i]]

    if a[i] < 0:
        a[i] = 0
    if a[i] > 1000000:
        a[i] = 1

print(*a[1:])
