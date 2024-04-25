import sys 
sys.setrecursionlimit(5000)
 
 
def dfs(x, y):
    global longth
    if x == 0 or V[x] == (0, 0):
        return
    longth = max(longth, y)
    dfs(V[x][0], y + 1)
    dfs(V[x][1], y + 1)
 
 
n = int(input())
V = {}  # 建个字典
longth = 0
for i in range(n):
    l, r = map(int, input().split())
    V[i + 1] = (l, r)  # 塞键值对,节点数
 
dfs(1, 1)
print(longth + 1, end='')