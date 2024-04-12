n,m = map(int,input().split())
g = [[]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
  g[i] = [0] + list(map(int,input().split()))
x1,y1,x2,y2 = map(int,input().split())
def bfs():
  import collections
  flag = False
  dic = [(0,1),(0,-1),(1,0),(-1,0)]
  q = collections.deque()
  q.append((x1,y1,0))
  vis = set()

#判断队列是否为空
  while q:
    #遍历这个队列
    for _ in range(len(q)):
      #弹出队首值
      x,y,step = q.popleft()
      #判断条件，达到目的地，返回步数
      if x == x2 and y == y2:
        return step
      #如果当前位置走过，则continue
      if (x,y) in vis:
        continue
      #否则添加到vis
      vis.add((x,y))
      #遍历四个方向
      for c in dic:
        dx,dy = x+c[0],y+c[1]
        #判断是否越界和是否能通行
        if 1<=dx<=n and 1<=dy<=m and g[dx][dy] == 1:
          #入队
          q.append((dx,dy,step+1))
  #若队列为空了都没能返回，说明走不到目的地，返回-1
  return -1
print(bfs())



import collections
n,m=map(int,input().split())
g=[[]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    g[i]=[0]+list(map(int,input().split()))
x1,y1,x2,y2=map(int,input().split())
def bfs():
    flag=False
    dir=[(0,1),(0,-1),(1,0),(-1,0)]
    q=collections.deque()
    q.append((x1,y1,0))
    vis=set()
    while q:
        for _ in range(len(q)):
            x,y,step=q.popleft()
            if x==x2 and y==y2:
                return step
            if (x,y) in vis:
                continue
            vis.add((x,y))
            for c in dir:
                dx,dy=x+c[0],y+c[1]
                if 1<=dx<=n and 1<=dy<=m and g[dx][dy]==1:
                    q.append((dx,dy,step+1))
    return -1
print(bfs())