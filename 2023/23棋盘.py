n,m=map(int,input().split())
s=[[0]*2010 for i in range(2010)]
for i in range(m):
    x1,y1,x2,y2=map(int,input().split())
    s[x1][y1]+=1
    s[x2+1][y2]-=1
    s[x1][y2+1]-=1
    s[x2+1][y2+1]+=1
for i in range(1,n+1):
    for j in range(1,n+1):
        s[i][j]+=s[i-1][j]+s[i][j-1]-s[i-1][j-1]
        print(s[i][j]%2,end=' ')
    print()