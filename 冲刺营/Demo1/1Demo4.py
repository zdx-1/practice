#174付账问题
n,s=map(int,input().split())
a=list(map(int,input().split()))
avg=s/n
a.sort()
b=0
for i in range(n):
    if a[i]<=s/(n-i):
        b+=pow(a[i]-avg,2)
    else:
        b+=pow(s/(n-i)-avg,2)*(n-i)
        break
    s-=a[i]
print("{:.4f}".format((b/n)**0.5))