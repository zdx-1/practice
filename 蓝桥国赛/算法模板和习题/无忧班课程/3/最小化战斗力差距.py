n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = float('inf')
for i in range(1, n):
   ans = min(ans, a[i] - a[i - 1])
print(ans)