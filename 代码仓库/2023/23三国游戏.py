n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

def getAns(a,b,c):
    #ai-bi-ci
    d=[a[i]-b[i]-c[i] for i in range(n)]
    d1=[d[i] for i in range(n) if d[i]>0]
    d2=[d[i] for i in range(n) if d[i]<=0]
    ans=len(d1)
    total=sum(d1)
    for i in d2:
        if total+i>0:
            total+=i
            ans+=1
        else:
            break
    return ans

ans1=getAns(a,b,c)
ans2=getAns(b,a,c)
ans3=getAns(c,a,b)
ans=max(ans1,ans2,ans3)
if ans==0:
    ans=-1
print(ans)