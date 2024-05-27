#二项式反演

def quickpow(a, n, mod):
    ans = 1
    while n:
        if n & 1:
            ans = ans * a % mod
        a = a * a % mod
        n >>= 1
    return ans


def C(m, n):
    return fact[n] * inv[m] % mod * inv[n - m] % mod


def fact_init():
    fact[0] = inv[0] = 1
    for i in range(1, 100001):
        fact[i] = fact[i - 1] * i % mod
        inv[i] = inv[i - 1] * quickpow(i, mod - 2, mod) % mod


n, m = map(int, input().split())
k = n // 4
ans = 0
fact = [0] * 100001
inv = [0] * 100001
mod = 998244353
fact_init()

for i in range(m, k + 1):
    ans += (-1 if (i - m) % 2 else 1) * C(m, i) * C(i, n - 3 * i) * quickpow(10, n - 4 * i, mod)
    ans %= mod
print(ans)
