import os
import sys
from functools import lru_cache

# 使用 lru_cache 装饰器对 dfs 函数调用的结果进行缓存
# 通过避免对相同输入的重复计算来提高性能
@lru_cache(maxsize=None)
def dfs(x, y, use):
    global fin  # 声明 'fin' 为全局变量，以便在此函数内访问和修改
    
    # 基本情况：如果当前位置 (x, y) 是目的地 (c, d)，将 'fin' 设置为 True 并返回
    if x == c and y == d:
        fin = True
        return
    # 如果 'fin' 已经是 True（意味着已经到达目的地），立即返回
    # 这将停止进一步不必要的探索
    if fin:
        return
    
    # 遍历所有 4 个可能的方向：右，左，上，下
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]  # 根据方向计算新位置
        
        # 检查新位置是否在边界内
        if 0 <= nx < n and 0 <= ny < m:
            # 如果新位置的高度较低，移动到该位置并继续搜索
            if Map[x][y] > Map[nx][ny]:
                dfs(nx, ny, use)
            # 如果使用喷气背包（use 为 True）可以移动到高度在 k 单位内的更高位置，
            # 移动到该位置并将 'use' 设置为 False，表示喷气背包已被使用
            elif use and k + Map[x][y] > Map[nx][ny]:
                dfs(nx, ny, False)

# 读取输入：n, m, k
n, m, k = map(int, input().split())
# 读取输入：起始位置 (a, b) 和目的地 (c, d)
a, b, c, d = map(int, input().split())
# 调整位置为基于 0 的索引
a, b, c, d = a - 1, b - 1, c - 1, d - 1
# 读取地形的高度图
Map = [list(map(int, input().split())) for i in range(n)]

fin = False  # 初始化 'fin' 为 False，表示目的地尚未被到达
# 定义移动方向：右，左，下，上
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 从起始位置开始深度优先搜索，喷气背包可用（True）
dfs(a, b, True)

# 如果 'fin' 为 True，打印 'Yes'，表示可以到达目的地；否则，打印 'No'
if fin:
    print('Yes')
else:
    print('No')