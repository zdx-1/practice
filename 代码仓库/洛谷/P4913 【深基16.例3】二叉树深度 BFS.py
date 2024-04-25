def bfs(n):
    q.append(n)
    G[n]=1
    while q:
        x=q.pop(0)
        for j in range(2):
            if dict[x][j]!=0:
                q.append(dict[x][j])
                G[dict[x][j]]=G[x]+1
n=int(input())
q=[]
dict={}
for i in range(n):
    l,r=map(int,input().split())
    dict[i+1]=(l,r)
G=[0 for i in range(n+1)]
bfs(1)
print(max(G))