# #bfs模板题目
# from collections import deque


# n,m=map(int,input().split())
# G=[[]*(m+1) for i in range(n+1)]

# for i in range(1,n+1):
#     G[i]=[0]+list(map(int,input().split()))
# x1,y1,x2,y2=map(int,input().split())

# def bfs():
#     flag=False
#     dir=[(0,1),(0,-1),(1,0),(-1,0)]
#     q=deque()
#     q.append((x1,y1,0))
#     vis=set()

#     while q:
#         for _ in range(len(q)):
#             x,y,step=q.popleft()
#             if x==x2 and y==y2:
#                 return step
#             if (x,y) in vis:
#                 continue
#             vis.add((x,y))
#             for c in dir:
#                 dx,dy=x+c[0],y+c[1]
#                 if 1<=dx<=n and 1<=dy<=m and G[dx][dy]==1:
#                     q.append((dx,dy,step+1))
#     return -1

# print(bfs())

# #第二遍
# import collections


# n,m=map(int,input().split())
# g=[[]*(m+1) for i in range(n+1)]
# for i in range(1,n+1):
#     g[i]=[0]+list(map(int,input().split()))
# x1,y1,x2,y2=map(int,input().split())
# def bfs():
#     flag=False
#     dir=[(0,1),(0,-1),(1,0),(-1,0)]
#     q=collections.deque()
#     q.append((x1,y1,0))
#     vis=set()
#     while q:
#         for _ in range(len(q)):
#             x,y,step=q.popleft()
#             if x==x2 and y==y2:
#                 return step
#             if (x,y) in vis:
#                 continue
#             vis.add((x,y))
#             for c in dir:
#                 dx,dy=x+c[0],y+c[1]
#                 if 1<=dx<=m and 1<=dy<=m and g[dx][dy]==1:
#                     q.append((dx,dy,step+1))
#     return -1
# print(bfs())


# #第三遍
# import collections


# n,m=map(int,input().split())
# g=[[]*(m+1) for i in range(n+1)]
# for i in range(1,n+1):
#     g[i]=[0]+list(map(int,input().split()))
# x1,y1,x2,y2=map(int,input().split())
# def bfs():
#     flag=False
#     dir=[(1,0),(-1,0),(0,1),(0,-1)]
#     q=collections.deque()
#     q.append((x1,y1,0))
#     vis=set()
#     while q:
#         for _ in range(len(q)):
#             x,y,step=q.popleft()
#             if x==x2 and y==y2:
#                 return step
#             if (x,y) in vis:
#                 continue
#             vis.add((x,y))
#             for c in dir:
#                 dx,dy=x+c[0],y+c[1]
#                 if 1<=dx<=n and 1<=dy<=m and g[dx][dy]==1:
#                     q.append((dx,dy,step+1))
#     return -1
# print(bfs())

#第四遍
# import collections
# n,m=map(int,input().split())
# g=[[]*(m+1)]*(n+1)
# for i in range(1,n+1):
#     g[i]=[0]+list(map(int,input().split()))
# x1,y1,x2,y2=map(int,input().split())
# def bfs():
#     flag=False
#     dir=[(0,1),(0,-1),(1,0),(-1,0)]
#     q=collections.deque()
#     q.append((x1,y1,0))
#     vis=set()
#     while q:
#         for _ in range(len(q)):
#             x,y,step=q.popleft()
#             if x==x2 and y ==y2:
#                 return step
#             if (x,y) in vis:
#                 continue
#             vis.add((x,y))
#             for i in dir:
#                 dx,dy=x+i[0],y+i[1]
#                 if 1<=dx<=n and 1<=dy<=m and g[dx][dy]==1:
#                     q.append((dx,dy,step+1))
#     return -1
# print(bfs())


