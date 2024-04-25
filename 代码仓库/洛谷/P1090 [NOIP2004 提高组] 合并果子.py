n=int(input())
a=list(map(list,input().split()))
a.sort()
s=[]
for i in range(1,a):
    q=a[i]+a[i+1]
    s.append(q)