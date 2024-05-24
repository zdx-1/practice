"""
https://www.lanqiao.cn/problems/3749/learning
"""
from queue import PriorityQueue,Queue
N,X=map(int,input().split())
a=list(map(int,input().split()))
q=Queue()
pq=PriorityQueue()
for i,x in enumerate(a):
  q.put((i,x))
  pq.put(-x)
time=0
while True:
  i,x=q.get()
  if -x==pq.queue[0]:
    pq.get()
    time+=1
    if i==X:
      print(time)
      break
  else:
    q.put((i,x))