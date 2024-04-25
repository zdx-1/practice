n,V=map(int,input().split())
a=[[] for i in range(n+1)]
for i in range(1,n+1):
  a[i]=[0]+list(map(int,input().split()))
cnt=0
for i in range(1,n+1):
  cnt+=a[i][1]
print(cnt)
if cnt <=V:
  print()