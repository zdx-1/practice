ans=0
n=int(input())
a=list(map(int,input().split()))
while len(a)>=2:
    a.sort()
    x=a.pop(0)
    y=a.pop(0)
    ans+=x+y
    a.insert(0,x+y)

print(ans)