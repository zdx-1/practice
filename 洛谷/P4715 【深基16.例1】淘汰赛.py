n=int(input())
L=list(map(int,input().split()))
q=[]
for i in L:
    q.append(i)
while len(q)>2:
    a,b=q.pop(0),q.pop(0)
    if a>b:
        q.append(a)
    else:
        q.append(b)
print(L.index(min(q))+1)
