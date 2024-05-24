import bisect
mxn=int(1e6+5)
pre=[0]*mxn
st=[False]*mxn
v=[]
mp={}
cnt=0
for i in range(2,mxn):
    if not st[i]:
        pre[cnt]=i
        cnt+=1
        mp[i]=True
    j=0
    while i* pre[j]<mxn:
        st[i*pre[j]]=True
        if i%pre[j]==0:
            break
        j+=1
for i in range(cnt-1,-1,-1):
    v.append(pre[i]-2*pre[i])
for i in range(cnt):
    v.append(pre[i])

v.sort()
pre=v
cnt=2*cnt

n,m=map(int,input().split())

a=[0]*(n+1)
dp=[0]*(n+1)

a[1:n+1]=map(int,input().split())


for _ in range(m):
    op,k,x=map(int,input().split())
    for i in range(k,n+1,k):
        if op==2:
            t=abs(a[i])
            if t not in mp:
                idx =bisect.bisect_left(pre,a[i])
                