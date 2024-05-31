t = input()
s = input()
m,n = len(t), len(s)
B = 26
mod = 1000000007
hash = [0] * (n + 1)
for i in range(1,n + 1):
    hash[i] = hash[i - 1] * B + ord(s[i - 1]) - ord('A')
    hash[i] %= mod

numT = 0
for c in t:
    numT = numT * B + ord(c) - ord('A')
    numT %= mod

p = (B ** m) % mod
ans = 0
for l in range(1,n +1):
    r = l + m - 1
    if r > n:
        break
    if (hash[r] - hash[l - 1] * p % mod + mod) % mod == numT:
        ans += 1
print(ans)
