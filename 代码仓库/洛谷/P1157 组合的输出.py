n,r=map(int,input().split())
k=2
def df(i,k): 
    for j in range(i,n+1):
       print(j,end=' ')
    k-=1
for i in range(1,n+1):
    if k>0:
        df(i,k)