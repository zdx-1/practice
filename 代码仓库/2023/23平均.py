n=int(input())
cnt=[[] for i in range(10)]

for _ in range(n):
    a,b=map(int,input().split())
    cnt[a].append(b)
print(cnt)

res=0

for i in range(10):
    if len(cnt[i])<=n//10:
        continue
    cnt[i].sort(reverse=True)
    print(cnt[i])
    res+=sum(cnt[i][n//10:])
    print(cnt[i][n//10:])
print(res)