M = 12
MOD = 998244353
prefixSum = [[[[[0 for _ in range(M)] for _ in range(M)] for _ in range(M)] for _ in range(M)] for _ in range(2)]
n, m = map(int, input().split())
ans = 0
p, q = 1, 0
for a in range(p, 10, 2):
    for b in range(q, 10, 2):
        for c in range(p, 10, 2):
            for d in range(q, 10, 2):
                prefixSum[0][a+2][b][c][d] = (prefixSum[0][a][b][c][d] + (1 if a+b+c+d <= m else 0)) % MOD
for i in range(5, n+1):
    p ^= 1
    q ^= 1
    for a in range(p, 10, 2):
        for b in range(q, 10, 2):
            for c in range(p, 10, 2):
                for d in range(q, 10, 2):
                    f = m - a - b - c - d
                    if q != (f & 1): f -= 1
                    if f > 8 + p: f = 8 + q
                    prefixSum[i & 1][a + 2][b][c][d] = (prefixSum[i & 1][a][b][c][d] + (0 if f < q else prefixSum[~i & 1][f + 2][a][b][c])) % MOD
for b in range(q, 10, 2):
    for c in range(p, 10, 2):
        for d in range(q, 10, 2):
            f = m - b - c - d
            if f < p: continue
            if p != (f & 1): f -= 1
            if f > 8 + p: f = 8 + p
            ans = (ans + prefixSum[n & 1][f + 2][b][c][d]) % MOD
print(ans)