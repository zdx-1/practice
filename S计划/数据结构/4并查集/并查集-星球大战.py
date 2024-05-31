"""
https://www.lanqiao.cn/problems/828/learning/
"""
import os
import sys

# 请在此输入您的代码
M = 200010; N = 2 * M
n, m = map(int, input().split())

father = [0] * (n + 10)                 #并查集板块
def init():
    for i in range(n + 10):
        father[i] = i
def find_father(x):
    if x != father[x]: father[x] = find_father(father[x])
    return father[x]
def unite(x, y):
    father[find_father(x)] = find_father(y)

come = [0] * N; to = [0] * N;   #存储每个边
g = [[] for _ in range(N)]      #邻接表
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b); g[b].append(a)
    come[i] = a; to[i] = b 

broken = [0] * (n + 10)                     #记录每个点是否被修坏
destroy = []
k = int(input())
for i in range(k):
    b = int(input())
    broken[b] = 1
    destroy.append(b)

init()
res = n - k                                 #先计算所有剩下星球的连通块数，(最后一轮的结果)
for i in range(m):
    l = come[i]; r = to[i]
    fl, fr = find_father(l), find_father(r)
    if not broken[l] and not broken[r] and fl != fr:
        res -= 1
        #unite(l, r)
        father[fl] = fr
ans = [res]
for i in range(len(destroy) - 1, -1, -1):       #顺序破坏，相当于倒序修建
    c = destroy[i]
    broken[c] = 0
    res += 1                                    #修好一个星球，连通块会多一个
    for j in g[c]:
        fc, fp = find_father(c), find_father(j)
        if not broken[j] and fc != fp:
            res -= 1
            father[fc] = fp
    ans.append(res)

for i in range(len(ans) - 1, -1, -1):           #倒序输出结果
    print(ans[i])

