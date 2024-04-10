n,m=map(int,input().split())
a=[]
for i in range(n):
    a.extend(list(map(int,input().split())))
for i in a:
    if a.count(i)>(m*n)//2:
        print(i)
        break