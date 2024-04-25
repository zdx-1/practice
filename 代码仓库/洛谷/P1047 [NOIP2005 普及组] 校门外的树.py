l,m=map(int,input().split())
a=list(list(map(int,input().split())) for i in range(m))
temp=[0 for i in range(l)]
while a:
    s1=a[0][0]
    s2=a[0][1]
    a.pop(0)
    for i in range(len(temp)):
        if i>=s1 and i <=s2:
            temp[i]=1
print(l-temp.count(1)+1) 
        