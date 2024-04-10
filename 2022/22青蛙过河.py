n,x=list(map(int,input().split()))
H=[0,*list(map(int,input().split()))]
Pre_sum=[0]*(n)

for idx in range(1,n):
    Pre_sum[idx]=Pre_sum[idx-1]+H[idx]

def check(y):
    for i in range(1,n-y+1):
        r=i+y-1
        if Pre_sum[r]-Pre_sum[i-1]<2*x:
            return False
    return True
l,r=1,n
ans=-1
while l<=r:
    mid=(l+r)//2
    if check(mid):
        ans=mid
        r=mid-1
    else:
        l=mid+1
print(ans)