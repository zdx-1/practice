from collections import Counter

s = list(input())
d = Counter(s)
mark = 1
for k, v in d.items():
    if v % 2 != 0:
        mark = 0
        break
print("YES" if mark == 1 else "NO")
