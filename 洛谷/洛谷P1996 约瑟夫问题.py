n,m=map(int,input().split())
a=[int(i) for i in range(1,n+1)]
#添加一个队列，实时添加符合情况的元素
r=[]
count=0
while a:
    count += 1
    q=a.pop(0)
    if count==m:
        r.append(q)
        count=0
    else:
        a.append(q)

for i in r:
    print(i,end=" ")

    