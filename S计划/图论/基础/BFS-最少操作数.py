"""
https://www.lanqiao.cn/problems/1509/learning
"""
from collections import deque
import sys
input=sys.stdin.readline
def bfs(s,t):
    '''
    :param s: 起点
    :param t: 终点
    :return:
    '''
    dis = [-1]*100001
    queue = deque()
    #1、将起点塞入到队列中，打上标记
    queue.append(s)
    dis[s] = 0
    #2、当队列非空
    while len(queue) != 0:
        # 2.1 取出队首元素u
        u = queue.popleft()
        #2.2 判断u是否为终点
        if u == t:
            return dis[u]
        #2.3 将u相连的所有点v，只要v未标记，则入队列
        for v in [u-1,u+1,u*2]:
            #特判：未越界、未标记
            if 0<=v<=100000 and dis[v] == -1:
                queue.append(v)
                dis[v] = dis[u] + 1
    return -1

n,k = map(int,input().split())
print(bfs(n,k))
