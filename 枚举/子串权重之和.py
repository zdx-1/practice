"""
没看懂是什么意思
题号3182
"""
n = int(input())
s = input()
mp = {}
ans = 0
for i in range(n):
    ans += mp.get(s[i], 0) * (n - i)
    mp[s[i]] = mp.get(s[i], 0) + i + 1
print(ans)