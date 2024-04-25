
n,m,k=map(int,input().split())
a=list(input() for i in range(n))
s=""
for i in a:
    for j in i:
        if j=="1":
            s+=j
c=s.count("1")
cout=0
if c%2==0:
    for i in range(n):
        for j in range(m):
            if a[i][j]=="1":
                cout+=1
                if cout==c//2:
                    print(i+1,j+1)
                    break
else:
    for i in range(n):
        for j in range(m):
            if a[i][j]=="1":
                cout+=1
                if cout==c//2+1:
                    print(i+1,j+1)
                    break