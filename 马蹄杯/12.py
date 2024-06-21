n=int(input())
a=[[0]*(n+1)]*(n+1)
for i in range(n):
    tmp=list(map(int,input().split()))
    for j in range(n):
        a[i][j]=tmp[j]
print(a)
